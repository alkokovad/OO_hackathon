# Веб-сервис "Оракул Недвижимость" был создан в рамках хакатона "Optimize & Organize"

## Инструкция по запуску

1. Накатить PostreSQL 15.2 и любой Python 3.10 на вашу машину.
2. Создать через psql базу данных на дефолтных значениях, исключая NAME:OO_hack, PASSWORD:OO_hack.
3. Скачать наш проект.
4. Накатить на ваше окружение pipenv.
5. Выполнить в терминале проекта следующие команды
    - `pipenv run pip install -r requirements.txt`
    - `pipenv shell` (если venv от pipenv по какой-то причине не создался)
6. Запускаем проект из главной директории
    - `python manage.py makemigrations` (если не появляются новые - проверьте и удалите OO_hack_page/migrations/0001...py)
    - `python manage.py migrate`
    - `python manage.py createsuperuser`
    - `python manage.py runserver`
7. Список карточек по `url/cards_list`
8. Дэшборд по `url/dashboard`
9. Админ панель по `url/admin`
