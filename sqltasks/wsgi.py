import os
from django.core.wsgi import get_wsgi_application
# from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sqltasks.settings')

application = get_wsgi_application()
# application = WhiteNoise(application)
# application.add_files('/home/ubuntu/sql_task_website/staticfiles', prefix='static/')
