Веб-приложения "Доска объявлений".
Автор: Петрова Ю.В.

Технологии:
python 3.11, postgresql, git, API

Используемые библиотеки:
Django, djangorestframework, djangorestframework-simplejwt, djoser, django_filters,
pillow, psycopg2-binary, python-dotenv, django-cors-headers, drf-yasg

Задача проекта - разработать backend-часть для сайта объявлений.
Проект предполагает предполагает реализацию следующего функционала:

- Авторизация и аутентификация пользователей.
- Распределение ролей между пользователями (пользователь и админ).
- Восстановление пароля через электронную почту.
- CRUD для объявлений на сайте (админ может удалять или редактировать все объявления, 
а пользователи только свои).
- Под каждым объявлением пользователи могут оставлять отзывы.
- В заголовке сайта можно осуществлять поиск объявлений по названию.

Инструкция для развертывания проекта:
1. Клонировать проект: https://github.com/juliana6k6/adtableproject
2. Создать виртуальное окружение  - 
python -m venv env
Активировать его. Для этого в терминале запустить команды:
env\Scripts\activate
3. Установить зависимости. Для установки всех зависимостей в терминале запустить команду:
pip install -r requirements.txt
4. Cоздать базу данных. Для этого в терминале введите команду:
CREATE DATABASE database_name
5. Применить миграции. Для этого в терминале введите команды:
python3 manage.py migrate
6. Заполнить файл .env по образцу env_example.
7. Cоздать суперпользователя. Для этого необходимо применить команду:
python3 manage.py csu
8. Чтобы запустить проект локально:
- Раскомментировать в случаи необходимости настойки БД в настройках.
- Запустить проект через терминал следующей командой:
python manage.py runserver
9. Для работы с приложением необходима регистрация, обязательные поля: password, email.
После регистрации вы сможете добавить свои объявления, просмотреть любые объявления в приложении, 
10. Документация API:
Swagger http://127.0.0.1:8000/docs/
Redoc http://127.0.0.1:8000/redoc/
11. Чтобы запустить тесты нужно в терминале ввести команду - python manage.py test. 
Для подсчета покрытия тестами используется специальный пакет - coverage. 
Чтобы его установить, вводим команду - pip install coverage.
После установки важно запустить подсчет покрытия и вывести отчет:
coverage run --source='.' manage.py test
coverage report
12. Для запуска проекта с помощью Docker необходимо:
1. Раскомментировать в случаи необходимости настройки для БД в настойках.
2. Установить Docker Desktop.
2. Перейти в корневую директорию проекта и ввести в терминале команду "docker-compose up -d --build" 
либо поочередно:
docker-compose build
docker-compose up
3. Открыть браузер и адрес по адресу http://localhost:800
Проект предполагает:
- Создание модели пользователя:
    - Необходимые поля:
        - first_name — имя пользователя (строка).
        - last_name — фамилия пользователя (строка).
        - phone — телефон для связи (строка).
        - email — электронная почта пользователя (email) **(используется в качестве логина).**
        - role — роль пользователя, доступные значения: user, admin.
        - image — аватарка пользователя.
- Настройка авторизации и аутентификации:
    - Настроить авторизацию пользователя с помощью библиотеки simple_jwt.
    - Сброс и восстановление пароля через почту.
- Модель объявления должна содержать следующие поля:
    - title — название товара.
    - price — цена товара (целое число).
    - description — описание товара.
    - author — пользователь, который создал объявление.
    - created_at — время и дата создания объявления.
    - Объявления должны быть отсортированы по дате создания (чем новее, тем выше).
- Модель отзыва должна содержать следующие поля:
    - text — текст отзыва.
    - author — пользователь, который оставил отзыв.
    - ad — объявление, под которым оставлен отзыв.
    - created_at — время и дата создания отзыва.
- Создание views и эндпоинтов:
   - Создать эндпоинты для всех необходимых операций с использованием DRF.
   - Реализовать поиск товаров по названию с использованием библиотеки `django-filter`. 
   - Эндпоинт `/ads/` должен поддерживать пагинацию с ограничением не более 4 объектов на странице.
- Определение permissions к views:
   - Анонимный пользователь может:
    - получать список объявлений.
   - Пользователь может:
    - получать список объявлений,
    - получать одно объявление,
    - создавать объявление,
    - редактировать и удалять свое объявление,
    - получать список комментариев,
    - создавать комментарии,
    - редактировать/удалять свои комментарии.
   - Администратор может:
    - дополнительно к правам пользователя редактировать или удалять объявления и комментарии любых других пользователей.
- Упаковка в Docker:
  - Создать `Dockerfile` для сборки образа приложения.
  - Создать `docker-compose.yml` для запуска приложения и базы данных PostgreSQL.
- Написать тесты для всех основных функций платформы.
