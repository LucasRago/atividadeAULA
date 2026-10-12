from django.contrib import admin
from .models import Tarefa


@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'prioridade', 'data_limite', 'concluida')
    list_filter = ('prioridade', 'concluida')
    search_fields = ('titulo', 'descricao')
