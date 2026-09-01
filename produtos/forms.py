from django import forms
from .models import Produto


class ProdutoForm(forms.ModelForm):
    """
    Formulário usado tanto para CRIAR quanto para EDITAR um produto.

    Usamos um ModelForm porque ele já lê os campos direto do model
    Produto e cria automaticamente as validações (ex.: código de
    barras único, campos obrigatórios etc.).
    """

    class Meta:
        model = Produto
        # Lista explícita dos campos que aparecem no formulário.
        # 'cadastrado_em' fica de fora porque é preenchido sozinho.
        fields = [
            'nome',
            'descricao',
            'categoria',
            'codigo_barras',
            'fornecedor',
            'preco',
            'quantidade_estoque',
            'validade',
            'ativo',
        ]
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'categoria': forms.Select(attrs={'class': 'form-select'}),
            'codigo_barras': forms.TextInput(attrs={'class': 'form-control'}),
            'fornecedor': forms.TextInput(attrs={'class': 'form-control'}),
            'preco': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'quantidade_estoque': forms.NumberInput(attrs={'class': 'form-control'}),
            'validade': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'ativo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
