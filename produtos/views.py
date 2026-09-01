from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import Produto
from .forms import ProdutoForm


def produto_list(request):
    """READ (listagem): mostra todos os produtos cadastrados."""
    produtos = Produto.objects.all()
    return render(request, 'produtos/produto_list.html', {'produtos': produtos})


def produto_detail(request, pk):
    """READ (detalhe): mostra os dados completos de um produto."""
    produto = get_object_or_404(Produto, pk=pk)
    return render(request, 'produtos/produto_detail.html', {'produto': produto})


def produto_create(request):
    """CREATE: formulário de cadastro de um novo produto."""
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produto cadastrado com sucesso!')
            return redirect('produto_list')
    else:
        # GET: só mostra o formulário vazio
        form = ProdutoForm()

    return render(request, 'produtos/produto_form.html', {
        'form': form,
        'titulo_pagina': 'Cadastrar novo produto',
    })


def produto_update(request, pk):
    """UPDATE: formulário de edição, já vem preenchido com os dados atuais."""
    produto = get_object_or_404(Produto, pk=pk)

    if request.method == 'POST':
        # instance=produto -> diz ao Django para ATUALIZAR este registro,
        # em vez de criar um novo
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produto atualizado com sucesso!')
            return redirect('produto_detail', pk=produto.pk)
    else:
        form = ProdutoForm(instance=produto)

    return render(request, 'produtos/produto_form.html', {
        'form': form,
        'titulo_pagina': f'Editar: {produto.nome}',
    })


def produto_delete(request, pk):
    """DELETE: pede confirmação antes de excluir o registro."""
    produto = get_object_or_404(Produto, pk=pk)

    if request.method == 'POST':
        # só chega aqui depois que o usuário confirmou no template
        produto.delete()
        messages.success(request, 'Produto excluído com sucesso!')
        return redirect('produto_list')

    # GET: apenas mostra a tela de confirmação, ainda não apaga nada
    return render(request, 'produtos/produto_confirm_delete.html', {'produto': produto})
