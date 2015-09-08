import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = 'a3yc73cu$kfw1x3lppf$)k3kv=4@&m66!7o$-qgjp5(7)hi_^x'
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'folio',
        'USER': 'root',
        'PASSWORD': 'calloser',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

