from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Nome do produto.', max_length=150)),
                ('descricao', models.TextField(blank=True, help_text='Descrição ou observações sobre o produto (opcional).')),
                ('categoria', models.CharField(choices=[('HOR', 'Hortifrúti'), ('ACO', 'Açougue'), ('PAD', 'Padaria'), ('LAT', 'Laticínios'), ('MER', 'Mercearia'), ('BEB', 'Bebidas'), ('LIM', 'Limpeza'), ('HIG', 'Higiene pessoal'), ('OUT', 'Outro')], default='OUT', help_text='Categoria/setor do produto no mercado.', max_length=3)),
                ('codigo_barras', models.CharField(help_text='Código de barras (EAN) do produto, deve ser único.', max_length=20, unique=True)),
                ('fornecedor', models.CharField(blank=True, help_text='Nome do fornecedor (opcional).', max_length=100)),
                ('preco', models.DecimalField(decimal_places=2, help_text='Preço de venda do produto, em reais.', max_digits=8)),
                ('quantidade_estoque', models.IntegerField(default=0, help_text='Quantidade disponível em estoque.')),
                ('validade', models.DateField(blank=True, help_text='Data de validade do produto (opcional, para itens perecíveis).', null=True)),
                ('ativo', models.BooleanField(default=True, help_text='Marque se o produto está ativo para venda.')),
                ('cadastrado_em', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
                'ordering': ['nome'],
            },
        ),
    ]
