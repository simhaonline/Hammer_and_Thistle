import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hammer_and_thistle.settings")

application = get_wsgi_application()
