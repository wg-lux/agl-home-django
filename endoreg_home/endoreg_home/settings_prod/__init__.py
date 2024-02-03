from ..settings_base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'your_prod_secret_key'

DEBUG = False


# Production database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'prod_db_name',
        'USER': 'prod_db_user',
        'PASSWORD': 'prod_db_password',
        'HOST': 'prod_db_host',
        'PORT': 'prod_db_port',
    }
}

# Static files (CSS, JavaScript, Images)
STATIC_ROOT = '/path/to/static/files'

# SSL/HTTPS settings here if needed