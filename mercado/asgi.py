"""Configuração ASGI do projeto (arquivo padrão gerado pelo Django)."""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mercado.settings')

application = get_asgi_application()
