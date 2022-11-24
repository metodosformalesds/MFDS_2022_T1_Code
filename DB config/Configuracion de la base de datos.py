#Configuracion de la base de datos
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'django',
        'USER': 'jared@servicios-db',
        'PASSWORD': os.getenv("DB_PASSWORD"),
        #'PASSWORD':'Chayito6662653',
        'HOST': 'servicios-db.postgres.database.azure.com',
        'PORT': '5432',
        'OPTIONS': {"sslmode": "require"},
    }
}
