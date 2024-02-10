LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'debug.log',
            'formatter': 'verbose',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
        # 'mozilla_django_oidc': {
        #     'handlers': ['console', 'file'],
        #     'level': 'DEBUG',
        #     'propagate': False,
        # },
        # 'my_oidc_backend': {
        #     'handlers': ['console', 'file'],
        #     'level': 'DEBUG',
        #     'propagate': False,
        # },
    },
}
