from django.shortcuts import render, get_object_or_404, redirect
from .models import Produto
from .forms import ProdutoForm

# Create your views here.
def cadastrar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar-produtos')
        
    else:
        form = ProdutoForm()
    return render(request, 'estoque/cadastrar_produtos.html', {'form': form })

def listar_produtos(request):
    produtos = Produto.objects.all()

    total_produtos = sum([produto.quantidade for produto in produtos])
    valor_total_estoque = sum([produto.quantidade * produto.preco for produto in produtos])
    
    return render(request, 'estoque/listar_produtos.html',{
        'produtos': produtos,
        'total_produtos': total_produtos,
        'valor_total_estoque': valor_total_estoque,
    })

def editar_produto(request, pk):
    
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('listar-produtos')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'estoque/editar_produto.html', {'form': form})

def excluir_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)

    if request.method == "POST":
        produto.delete()
        return redirect('listar-produtos')
    return render(request, 'estoque/confirmar_excluir.html', {'produto': produto})

def visualizar_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    return render(request, 'estoque/visualizar_produto.html', {'produto': produto})