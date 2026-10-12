from django.test import TestCase
from django.urls import reverse
from .models import Tarefa


class PlanejamentoTestes(TestCase):
    def test_pagina_abre(self):
        resposta = self.client.get(reverse('planejamento'))
        self.assertEqual(resposta.status_code, 200)
        self.assertContains(resposta, 'Planejamento')

    def test_cadastrar_concluir_e_excluir(self):
        resposta = self.client.post(reverse('adicionar_tarefa'), {
            'titulo': 'Estudar Django', 'descricao': 'Revisar views',
            'prioridade': 'alta', 'data_limite': '2026-10-15',
        })
        self.assertEqual(resposta.status_code, 302)
        tarefa = Tarefa.objects.get(titulo='Estudar Django')
        self.client.post(reverse('alternar_conclusao', args=[tarefa.id]))
        tarefa.refresh_from_db()
        self.assertTrue(tarefa.concluida)
        self.client.post(reverse('excluir_tarefa', args=[tarefa.id]))
        self.assertEqual(Tarefa.objects.count(), 0)
