import os
import dj_database_url
from environs import Env


env = Env()
env.read_env()
authentication = f'{env("DB_USER")}:{env("DB_PASSWORD")}'
database_settings = f'{env("DB_HOST")}:{env("DB_PORT")}/{env("DB_NAME")}'
database_url = f'postgres://{authentication}@{database_settings}'

DATABASES = {
    'default': dj_database_url.parse(
        database_url,
        conn_max_age=600,
        conn_health_checks=True,
    )
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = os.getenv("SECRET_KEY")

DEBUG = env.bool('DEBUG')

ROOT_URLCONF = 'project.urls'

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
