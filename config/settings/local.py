"""
開発環境用

"""

from .base import *

#####################
# Security settings #
#####################

DEBUG = True

# SECRET_KEY = 'secret-key'

ALLOWED_HOSTS = ['*']


#########
# Debug #
#########
# if DEBUG:
#     def show_toolbar(request):
#         return True
#
#
#     INSTALLED_APPS += (
#         'debug_toolbar',
#     )
#     MIDDLEWARE += (
#         'debug_toolbar.middleware.DebugToolbarMiddleware',
#     )
#     DEBUG_TOOLBAR_CONFIG = {
#         'SHOW_TOOLBAR_CALLBACK': show_toolbar,
#     }
#

############
# Database #
############

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


###########
# Logging #
###########

LOGGING = {
    # バージョンは「1」固定
    'version': 1,
    # 既存のログ設定を無効化しない
    'disable_existing_loggers': False,
    # ログフォーマット
    'formatters': {
        # 開発用
        'develop': {
            'format': '%(asctime)s [%(levelname)s] %(pathname)s:%(lineno)d '
                      '%(message)s'
        },
    },
    # ハンドラ
    'handlers': {
        # コンソール出力用ハンドラ
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'develop',
        },
    },
    # ロガー
    'loggers': {
        # 自作アプリケーション全般のログを拾うロガー
        '': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        # Django本体が出すログ全般を拾うロガー
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
        # 発行されるSQL文を出力するための設定
        # 'django.db.backends': {
        #     'handlers': ['console'],
        #     'level': 'DEBUG',
        #     'propagate': False,
        # },
    },
}

##########
# Caches #
##########

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'

# CACHES = {
#     'default': {
#         'BACKEND': 'django_redis.cache.RedisCache',
#         'LOCATION': 'redis://localhost:6379/',
#         'OPTIONS': {
#             'CLIENT_CLASS': 'django_redis.client.DefaultClient'
#         }
#     }
#   }


##################
# Email settings #
##################

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


##############
# whitenoise #
##############

MIDDLEWARE += {
    'whitenoise.middleware.WhiteNoiseMiddleware',
}

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


##############
# Bootstrap4 #
##############

BOOTSTRAP4 = {
    'set_placeholder': False,
}


#####################
# Django Extensions #
#####################

INSTALLED_APPS += (
    'django_extensions',
)
