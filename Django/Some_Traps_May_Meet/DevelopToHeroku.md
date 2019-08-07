Something went wrong with deploying apps to Heroku.

File 'setting.py' has some problem :

 
    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/1.9/howto/static-files/
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    STATIC_URL = '/static/'
    
    # Extra places for collectstatic to find static files.
    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'static'),
    )
    
    django_heroku.settings(locals())
    
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


The "STATIC_URL" is wrong for some reason. After I created a folder named ‘’static’ in its parent directory, and put something inside that, it went normally. The problem solved.