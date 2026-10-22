# 🛒 Mercado — CRUD em Django

Trabalho prático da disciplina de Programação Back-End — CRUD completo
desenvolvido com Django sobre o tema **estoque de produtos de um mercado**.

## Integrante

Gabriel Di Lorenzo Correa

## Tema

O sistema cadastra e gerencia os **produtos** do estoque de um mercado: é
possível cadastrar um produto novo, listar todos os produtos, ver o detalhe
de um produto específico, editar os dados e excluir um registro (com tela
de confirmação).

## Campos do model `Produto`

| Campo | Tipo | Observação |
|---|---|---|
| nome | CharField | nome do produto |
| descricao | TextField | opcional (`blank=True`) |
| categoria | CharField | lista fixa de opções (`choices`) |
| codigo_barras | CharField | código único (`unique=True`) |
| fornecedor | CharField | opcional (`blank=True`) |
| preco | DecimalField | campo numérico (valor em reais) |
| quantidade_estoque | IntegerField | campo numérico |
| validade | DateField | opcional (`blank=True, null=True`) |
| ativo | BooleanField | campo booleano, `default=True` |
| cadastrado_em | DateTimeField | preenchido automaticamente na criação |

## Tecnologias

- Python 3
- Django 5
- SQLite (banco de dados padrão do Django, não precisa instalar nada)
- Bootstrap 5 (via CDN, só para deixar as telas mais apresentáveis)

## Como rodar o projeto localmente

1. Clone o repositório:
   ```bash
   git clone <url-do-repositorio>
   cd <pasta-do-projeto>
   ```

2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv

   # Windows
   venv\Scripts\activate

   # Linux/Mac
   source venv/bin/activate
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Aplique as migrations (cria o banco de dados SQLite):
   ```bash
   python manage.py migrate
   ```

5. (Opcional, mas recomendado) Crie um usuário administrador para acessar o
   Django Admin:
   ```bash
   python manage.py createsuperuser
   ```

6. Rode o servidor de desenvolvimento:
   ```bash
   python manage.py runserver
   ```

7. Acesse no navegador:
   - Estoque de produtos: http://127.0.0.1:8000/
   - Django Admin: http://127.0.0.1:8000/admin/

## Estrutura do projeto

```
projeto_mercado/
├── manage.py
├── requirements.txt
├── mercado/            -> configurações gerais do projeto
│   ├── settings.py
│   └── urls.py
└── produtos/            -> app com o CRUD
    ├── models.py        -> model Produto
    ├── forms.py          -> formulário de cadastro/edição
    ├── views.py           -> lógica das 5 telas (listar, ver, criar, editar, excluir)
    ├── urls.py             -> rotas da app
    ├── admin.py            -> registro do model no Django Admin
    └── templates/produtos/  -> telas HTML
```

## Funcionalidades

- ✅ **Create**: cadastro de novo produto (`/produto/novo/`)
- ✅ **Read**: listagem (`/`) e detalhe de um produto (`/produto/<id>/`)
- ✅ **Update**: edição de um produto existente, formulário já preenchido (`/produto/<id>/editar/`)
- ✅ **Delete**: exclusão com tela de confirmação (`/produto/<id>/excluir/`)
- ✅ Model registrado no Django Admin, com busca e filtros
