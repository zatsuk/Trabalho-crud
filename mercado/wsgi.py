"""Configuração WSGI do projeto (arquivo padrão gerado pelo Django)."""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mercado.settings')

application = get_wsgi_application()
