###### YaMDB Учебный проект Яндекс Практикум

**Описание проекта:**
Django REST API

**Для старта с нуля:**
Для начала нужно поставить Docker
Затем зайти в корневую паку YaMDB и создать файл .env содержания:

DB_ENGINE=django.db.backends.postgresql
DB_NAME=yamdb_user
POSTGRES_USER=yamdb_user
POSTGRES_PASSWORD=###password###
DB_HOST=db
DB_PORT=5432
SECRET_KEY='######'

Затем там же в паке выполнить `docker-compose up`


Найти контейнер web (скорее всего будет называться apiyamdb_web_1) `docker container ls` 
Зайти в контейнер `docker exec -it apiyamdb_web_1 bash`
и внутри него выполнить:
`python3 manage.py migrate
python3 manage.py createsuperuser (по желанию, чтоб управлять через админку)
python3 manage.py loaddata fixtures.json`

Сервис будет доступен по адресу 127.0.0.1:8000