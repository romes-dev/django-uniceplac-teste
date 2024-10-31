from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Livro

@login_required
def lista_livros(request):
    query = request.GET.get('q')
    if query:
        livros = Livro.objects.filter(titulo__icontains=query) | Livro.objects.filter(autor__icontains=query)
    else:
        livros = Livro.objects.all()
    return render(request, 'livros/lista_livros.html', {'livros': livros})
