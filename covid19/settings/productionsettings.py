from covid19.settings.basesettings import *


DEBUG = False

ALLOWED_HOSTS = ["coronaworld.site","www.coronaworld.site","37.148.210.16"]


#production database information
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}



STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
