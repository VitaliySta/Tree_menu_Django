# Тестовое задание - Меню в Django


### Описание задания:
Сделать django app, который будет реализовывать древовидное меню, соблюдая
следующие условия:
1) Меню реализовано через template tag
2) Все, что над выделенным пунктом - развернуто. Первый уровень вложенности под
выделенным пунктом тоже развернут.
3) Хранится в БД.
4) Редактируется в стандартной админке Django
5) Активный пункт меню определяется исходя из URL текущей страницы
6) Меню на одной странице может быть несколько. Они определяются по названию.
7) При клике на меню происходит переход по заданному в нем URL. URL может быть 
задан как явным образом, так и через named URL.
8) На отрисовку каждого меню требуется ровно 1 запрос к БД

Нужен django-app, который позволяет вносить в БД меню (одно или несколько) через
админку, и нарисовать на любой нужной странице меню по названию.   
{% draw_menu 'main_menu' %}   
При выполнении задания из библиотек следует использовать только Django и стандартную библиотеку Python.

### Используемые технологии
- Django

### Подготовка к запуску проекта
- Клонируйте проект с помощью git clone или скачайте ZIP-архив.
- Установите и активируйте виртуальное окружение  
``` python -m venv venv ```
- Установите зависимости из файла requirements.txt  
``` pip install -r requirements.txt ```
- Перейдите в папку tree_menu
- Создайте и примените миграции  
``` python manage.py makemigrations ```  
``` python manage.py migrate ```
- Создайте суперпользователя:   
``` python manage.py createsuperuser ```

### Запуск проекта
- В папке tree_menu выполните команду:  
``` python manage.py runserver ```
- В браузере перейдите на сраницу администратора http://127.0.0.1:8000/admin/
- Перейдите в закладку - Элемент меню
- Создайте новый пункт меню без указания родительской категории - это будет основное меню
- Далее создайте новые пункты меню с указанием родительской категории
- В файле tree_menu\templates\menu.html измените 'main_menu' на название основного меню, которое вы создали
- Перейдите на страницу http://127.0.0.1:8000/, чтобы увидеть меню

#### Автор:
Стацюк Виталий - [https://github.com/VitaliySta](https://github.com/VitaliySta)