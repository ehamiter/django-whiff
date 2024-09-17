SECRET_KEY = 'fake-key'

INSTALLED_APPS = [
    'django_whiff',  # note the underscore and not hyphen
    'django.contrib.contenttypes',
    'django.contrib.auth',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
            ],
        },
    },
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}
