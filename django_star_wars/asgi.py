"""
ASGI config for django_star_wars project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/stable/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application

# Set the default Django settings module for the 'asgi' command.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_star_wars.settings')

# Get the ASGI application.
application = get_asgi_application()
