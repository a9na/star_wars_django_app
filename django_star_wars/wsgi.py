"""
WSGI config for django_star_wars project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/stable/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

# Set the default Django settings module for the 'wsgi' command.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_star_wars.settings')

# Get the WSGI application.
application = get_wsgi_application()
