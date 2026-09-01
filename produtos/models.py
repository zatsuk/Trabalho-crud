from django.db import models


class Produto(models.Model):
    """
    Representa um produto do estoque de um mercado.

    Contagem de campos exigidos pelo trabalho (sem contar o 'id',
    que o Django cria sozinho):

        1. nome                -> texto
        2. descricao            -> texto longo
        3. categoria             -> texto (com choices)
        4. codigo_barras        -> texto
        5. fornecedor            -> texto
        6. preco                 -> numérico (DecimalField)
        7. quantidade_estoque   -> numérico (IntegerField)
        8. validade               -> data (DateField)
        9. ativo                  -> booleano (BooleanField)

    Total: 9 campos, sendo 5 de texto, 2 numéricos, 1 de data e 1 booleano.
    """

    # Lista fixa de opções para o campo "categoria".
    # Vira automaticamente um <select> no admin e nos formulários.
    class Categoria(models.TextChoices):
        HORTIFRUTI = 'HOR', 'Hortifrúti'
        ACOUGUE = 'ACO', 'Açougue'
        PADARIA = 'PAD', 'Padaria'
        LATICINIOS = 'LAT', 'Laticínios'
        MERCEARIA = 'MER', 'Mercearia'
        BEBIDAS = 'BEB', 'Bebidas'
        LIMPEZA = 'LIM', 'Limpeza'
        HIGIENE = 'HIG', 'Higiene pessoal'
        OUTRO = 'OUT', 'Outro'

    # --- Campos de texto ---
    nome = models.CharField(
        max_length=150,
        help_text='Nome do produto.'
    )
    descricao = models.TextField(
        blank=True,
        help_text='Descrição ou observações sobre o produto (opcional).'
    )
    categoria = models.CharField(
        max_length=3,
        choices=Categoria.choices,
        default=Categoria.OUTRO,
        help_text='Categoria/setor do produto no mercado.'
    )
    codigo_barras = models.CharField(
        max_length=20,
        unique=True,
        help_text='Código de barras (EAN) do produto, deve ser único.'
    )
    fornecedor = models.CharField(
        max_length=100,
        blank=True,
        help_text='Nome do fornecedor (opcional).'
    )

    # --- Campos numéricos ---
    preco = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        help_text='Preço de venda do produto, em reais.'
    )
    quantidade_estoque = models.IntegerField(
        default=0,
        help_text='Quantidade disponível em estoque.'
    )

    # --- Campo de data ---
    validade = models.DateField(
        blank=True,
        null=True,
        help_text='Data de validade do produto (opcional, para itens perecíveis).'
    )

    # --- Campo booleano ---
    ativo = models.BooleanField(
        default=True,
        help_text='Marque se o produto está ativo para venda.'
    )

    # --- Controle automático (não conta como campo do formulário) ---
    cadastrado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['nome']  # lista sempre em ordem alfabética por nome
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        # É esse texto que aparece no admin e em qualquer lugar
        # onde o Django precisar representar o objeto como string.
        return f'{self.nome} — R$ {self.preco}'
