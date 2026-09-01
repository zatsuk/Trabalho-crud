"""
Rotas principais do projeto.

- /admin/  -> painel administrativo do Django
- ''       -> tudo mais é delegado para produtos/urls.py
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('produtos.urls')),
]
