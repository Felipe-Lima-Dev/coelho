from django.urls import path
from . import views

urlpatterns = [
    path('viagens/', views.listar_viagens, name='listar_viagens'),
    path('viagem/nova/', views.nova_viagem, name='nova_viagem'),
    path('viagem/<int:viagem_id>/', views.detalhes_viagem, name='detalhes_viagem'),
    path('viagem/<int:viagem_id>/detalhes', views.infos_viagem, name='infos_viagem'),
    path('viagem/<int:viagem_id>/editar', views.editar_viagem, name='editar_viagem'),
    path('viagem/<int:viagem_id>/delete', views.delete_viagem, name='delete_viagem'),
    path('viagem/<int:viagem_id>/passageiro/novo/', views.novo_passageiro, name='novo_passageiro'),
    path('passageiro/<int:passageiro_id>/', views.detalhes_passageiro, name='detalhes_passageiro'),
    path('passageiro/<int:passageiro_id>/editar/', views.editar_passageiro, name='editar_passageiro'),
    path('passageiro/<int:passageiro_id>/delete/', views.delete_passageiro, name='delete_passageiro'),
]