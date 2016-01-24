__author__ = 'kd'
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SECRET_KEY = 'a3yc73cu$kfw1x3lppf$)k3kv=4@&m66!7o$-qgjp5(7)hi_^x'
DEBUG = True

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, "templates"),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
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

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "assets"),

)

STATIC_ROOT = os.path.join(BASE_DIR, "../static")

MEDIA_ROOT = os.path.join(BASE_DIR, "../media")

#hello