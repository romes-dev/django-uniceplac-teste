from django.db import models

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    descricao = models.TextField()
    data_publicacao = models.DateField()
    
    # Novo campo para a imagem da capa do livro
    capa = models.ImageField(upload_to='livros/capas/', null=True, blank=True)
    # Campo renomeado para armazenar o link do PDF ou ePub
    arquivo_pdf_epub = models.FileField(upload_to='livros/arquivos/', null=True, blank=True)

    def __str__(self):
        return self.titulo
