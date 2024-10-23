from django.contrib import admin

from .models import Avaliacao, Curso


@admin.register(Curso)
class CursoAdmin(admin.ModelsAdmin):
    # MOstar os campos
    list_display = ('titulo', 'url', 'ciracao', 'atualizacao', 'Ativo')


@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelsAdmin):
    list_display = ('curso', 'nome', 'avaliacao',
                    'criacao', 'atualizacao', 'ativo')
