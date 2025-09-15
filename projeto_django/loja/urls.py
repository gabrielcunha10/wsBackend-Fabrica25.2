from django.urls import path, include
from . import views
from .views import cadastrarpessoa
from .views import listainformacoes
from .views import login
from .views import home
from .views import CadastroUpdateView, CadastroDeleteView

urlpatterns = [
    path('inicio', home, name='inicio'),
    path('cadastro', cadastrarpessoa, name='cadastropessoa'),
    path('', login, name="home_login"),
    path('login', login, name="login"),
    path('listainfo', listainformacoes, name='listainfo'),
    path('atualizar/<int:pk>/', CadastroUpdateView.as_view(), name='atualizar'),
    path('deletar<int:pk>', CadastroDeleteView.as_view(), name='deletar'),
    path('adicionar/<int:produto_id>/', views.adicionarcarrinho, name='adicionar'),
    path('carrinho/', views.carrinho, name='carrinho'),
    path('carrinho/selecionar/<int:produto_id>/', views.marcar_selecionado, name='marcar_selecionado'),
    path('carrinho/remover_selecionados/', views.remover_selecionados, name='remover_selecionados'),

]
