from datetime import date

from django.http import HttpResponseNotAllowed
from django.shortcuts import get_object_or_404, redirect, render

from .models import Tarefa


def home(request):
    tarefas = Tarefa.objects.all()
    contexto = {
        'tarefas': tarefas,
        'total': tarefas.count(),
        'pendentes': tarefas.filter(concluida=False).count(),
        'concluidas': tarefas.filter(concluida=True).count(),
    }
    return render(request, 'planejamento.html', contexto)


def adicionar_tarefa(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])

    titulo = request.POST.get('titulo', '').strip()
    if not titulo:
        return redirect('planejamento')

    descricao = request.POST.get('descricao', '').strip()
    prioridade = request.POST.get('prioridade', 'media')
    if prioridade not in {'baixa', 'media', 'alta'}:
        prioridade = 'media'

    prazo = request.POST.get('data_limite', '').strip()
    data_limite = None
    if prazo:
        try:
            data_limite = date.fromisoformat(prazo)
        except ValueError:
            pass

    Tarefa.objects.create(
        titulo=titulo[:120],
        descricao=descricao,
        prioridade=prioridade,
        data_limite=data_limite,
    )
    return redirect('planejamento')


def alternar_conclusao(request, tarefa_id):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])
    tarefa = get_object_or_404(Tarefa, pk=tarefa_id)
    tarefa.concluida = not tarefa.concluida
    tarefa.save(update_fields=['concluida'])
    return redirect('planejamento')


def excluir_tarefa(request, tarefa_id):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])
    tarefa = get_object_or_404(Tarefa, pk=tarefa_id)
    tarefa.delete()
    return redirect('planejamento')
