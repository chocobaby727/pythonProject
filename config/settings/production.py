"""
本番環境用

"""

from .base import *

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
        # 本番用
        'production': {
            'format': '%(asctime)s [%(levelname)s] %(process)d %(thread)d '
                      '%(pathname)s:%(lineno)d %(message)s'
        },
    },
    # ハンドラ
    'handlers': {
        # ファイル出力用ハンドラ
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': '/var/log/{}/app.log'.format(PROJECT_NAME),
            'formatter': 'production',
        },
    },
    # ロガー
    'loggers': {
        # 自作アプリケーション全般のログを拾うロガー
        '': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': False,
        },
        # Django本体が出すログ全般を拾うロガー
        'django': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}
