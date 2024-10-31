from django.contrib import admin
from django.utils.html import format_html  # Import necessário para exibir a imagem
from .models import Livro

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'data_publicacao', 'mostrar_capa')  # Adiciona a imagem ao display
    fields = ('titulo', 'autor', 'descricao', 'data_publicacao', 'capa', 'arquivo_pdf_epub')  # Campos para edição

    def mostrar_capa(self, obj):
        if obj.capa:
            return format_html('<img src="{}" style="width: 50px; height: auto;" />', obj.capa.url)
        return "-"
    mostrar_capa.short_description = "Capa"
