import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'blogdb',
        'USER': 'blog',
        'PASSWORD': 'blog',
        'HOST': 'localhost',
        'PORT': ''
    }
}