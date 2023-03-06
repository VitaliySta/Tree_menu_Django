from django import template
from django.utils.safestring import mark_safe

from ..models import Menu

register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):

    main_menu = Menu.objects.all()
    main_menu_item = main_menu.get(title=menu_name)
    request = context["request"]
    url_name = request.path.strip("/").split("/")[-1]
    submenu_items = []

    def collect_child_items(item, item_list):
        for child_item in item.children.all():
            item_list.append(child_item)

    def get_menu_hierarchy(menu_item):
        if menu_item.parent is None:
            return collect_child_items(menu_item, submenu_items)
        collect_child_items(menu_item, submenu_items)
        return get_menu_hierarchy(main_menu.get(title=menu_item.parent))

    if url_name:
        try:
            get_menu_hierarchy(main_menu.get(slug=url_name))
        except Exception:
            pass

    categories_by_parent = {
        None: [
            {
                "id": main_menu_item.id,
                "parent_id": None,
                "title": main_menu_item.title,
                "url": main_menu_item.slug
            }
        ]
    }

    for row in submenu_items:
        category = {
            "id": row.id,
            "parent_id": row.parent.id,
            "title": row.title,
            "url": row.slug
        }
        if category["parent_id"] not in categories_by_parent:
            categories_by_parent[category["parent_id"]] = []
        categories_by_parent[category["parent_id"]].append(category)

    return mark_safe(
        build_menu(
            categories_by_parent,
            context["request"],
            main_menu_item.parent
        )
    )


def build_menu(categories_by_parent, request, parent_id=None):

    html = ""

    url_name = request.path

    if len(categories_by_parent) > 1:
        url_name = request.path.replace(
            url_name.strip("/").split("/")[-1] + "/", ""
        )

    if parent_id in categories_by_parent:
        html += "<ul>"

        for category in categories_by_parent[parent_id]:
            html += "<li>"
            href = (
                f"{request.scheme}://"
                f"{request.get_host()}{url_name}{category['url']}"
            )
            html += (
                f"<a href='{href}' "
                f"class='{get_active_class(category['url'], request)}'>"
                f"{category['title']}</a>"
            )
            subtree = build_menu(categories_by_parent, request, category["id"])

            if subtree:
                html += subtree
            html += "</li>"
        html += "</ul>"

    return html


def get_active_class(url, request):

    if request.path.strip("/") == url:
        return "active"
    return ""
