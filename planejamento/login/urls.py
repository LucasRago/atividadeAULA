"""URLs do projeto Planejamento."""
from django.contrib import admin
from django.urls import path
from planejamentoapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='inicio'),
    path('planejamento/', views.home, name='planejamento'),
    path('planejamento/adicionar/', views.adicionar_tarefa, name='adicionar_tarefa'),
    path('planejamento/<int:tarefa_id>/concluir/', views.alternar_conclusao, name='alternar_conclusao'),
    path('planejamento/<int:tarefa_id>/excluir/', views.excluir_tarefa, name='excluir_tarefa'),
]
