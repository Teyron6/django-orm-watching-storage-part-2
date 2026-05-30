# Django ORM Watching Storage

Учебный проект на Django для отслеживания активности сотрудников в дата-центре с использованием Django ORM.

## Возможности

* Просмотр активных пропусков сотрудников
* Отображение информации по конкретному пропуску
* Анализ посещений и времени пребывания
* Работа с базой данных через Django ORM
* Веб-интерфейс на Django Templates

## Технологии

* Python 3
* Django
* HTML
* Django ORM

## Структура проекта

```text
datacenter/
├── models.py
├── active_passcards_view.py
├── passcard_info_view.py
├── security_info_helper.py
├── storage_information_view.py
├── migrations/
└── templates/

project/
├── settings.py
└── urls.py

manage.py
requirements.txt
```

## Установка

Клонируйте репозиторий:

```bash
git clone https://github.com/Teyron6/django-orm-watching-storage-part-2.git
cd django-orm-watching-storage-part-2
```

Создайте виртуальное окружение:

```bash
python -m venv venv
```

### Linux / macOS

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

Установите зависимости:

```bash
pip install -r requirements.txt
```

## Настройка

Создайте файл `.env` и укажите необходимые параметры проекта.

Пример:

```env
DB_ENGINE='DB_ENGINE'
DB_HOST='DB_HOST'
DB_PORT='DB_PORT'
DB_NAME='DB_NAME'
DB_USER='DB_USER'
DB_PASSWORD='DB_PASSWORD'
SECRET_KEY='SECRET_KEY'
DEBUG=True
```

## Запуск проекта

Выполните миграции:

```bash
python manage.py migrate
```

Запустите сервер разработки:

```bash
python manage.py runserver
```

После запуска приложение будет доступно по адресу:

```text
http://127.0.0.1:8000/
```

## Основные страницы

### Активные пропуска

Отображает сотрудников, которые в данный момент находятся на территории объекта.

### Информация о пропуске

Показывает историю посещений конкретного сотрудника.

### Информация о хранилище

Предоставляет статистику и данные о посещениях.

## Цель проекта

Проект создан для практики работы с:

* Django ORM
* моделями и запросами к базе данных
* шаблонами Django
* обработкой данных о посещениях
* организацией Django-приложений

Проект был создан в целях обучния в онлайн школе "Третье место", на платформе Devman.