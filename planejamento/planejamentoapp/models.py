from django.db import models


class Tarefa(models.Model):
    PRIORIDADES = [
        ('baixa', 'Baixa'),
        ('media', 'Média'),
        ('alta', 'Alta'),
    ]

    titulo = models.CharField(max_length=120)
    descricao = models.TextField(blank=True)
    data_limite = models.DateField(blank=True, null=True)
    prioridade = models.CharField(max_length=5, choices=PRIORIDADES, default='media')
    concluida = models.BooleanField(default=False)
    criada_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['concluida', 'data_limite', '-criada_em']
        verbose_name = 'Tarefa'
        verbose_name_plural = 'Tarefas'

    def __str__(self):
        return self.titulo
