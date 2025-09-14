from django.shortcuts import render, redirect
import requests
from .models import Cadastro
from .forms import CadastroForm
from django.contrib import messages 
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password
from django.views.generic import UpdateView, DeleteView
from django.urls import reverse_lazy

def home(request):
    response = requests.get("https://fakestoreapi.com/products/category/electronics?limit=3")
    produtos = response.json()
    return render(request, "home.html", {"produtos": produtos})

def listainformacoes(request):
    user_id = request.session.get("user_id")
    if not user_id:
        return redirect("login")
    user = Cadastro.objects.get(id=user_id)
    return render(request, 'info.html', {'informacoes': [user]})

def cadastrarpessoa(request):
    if request.method == "POST":
        form = CadastroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CadastroForm()
    return render(request, 'cadastro.html', {'form': form, "modo": "criar"})

def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        senha = request.POST.get("senha")
        try:
            user = Cadastro.objects.get(email=email)
        except Cadastro.DoesNotExist:
            messages.error(request, "Email não foi encontrado.")
            return render(request, "login.html")
        if check_password(senha,user.senha):
            request.session["user_id"] = user.id
            return redirect("inicio") 
        else: 
            messages.error(request, "Senha incorreta.") 
            return render(request, "login.html") 
    return render(request, "login.html")

class CadastroUpdateView(UpdateView):
    model = Cadastro
    form_class = CadastroForm
    template_name = 'cadastro.html'
    context_object_name = 'atualizacadastro'
    success_url = reverse_lazy('listainfo')

class CadastroDeleteView(DeleteView):
    model = Cadastro
    template_name = 'deletar.html'
    context_object_name = 'deletacadastro'
    success_url = reverse_lazy('login')

def adicionarcarrinho(request, produto_id):
    carrinho = request.session.get('carrinho', [])
    carrinho.append(produto_id)
    request.session['carrinho'] = carrinho
    return redirect('inicio')


def carrinho(request):
    ids_carrinho = request.session.get('carrinho', [])
    produtos = []
    for pid in ids_carrinho:
        response = requests.get(f'https://fakestoreapi.com/products/{pid}')
        produtos.append(response.json())
    return render(request, 'carrinho.html', {'produtos': produtos})

def marcar_selecionado(request, produto_id):
    selecionados = request.session.get('selecionados', [])  

    if produto_id in selecionados:
        selecionados.remove(produto_id)
    else:
        selecionados.append(produto_id)  

    request.session['selecionados'] = selecionados
    return redirect('carrinho')

def remover_selecionados(request):
    carrinho = request.session.get('carrinho', [])    
    selecionados = request.session.get('selecionados', [])

    novo_carrinho = []              
    for pid in carrinho:            
        if pid not in selecionados:  
            novo_carrinho.append(pid)  

    carrinho = novo_carrinho

    request.session['carrinho'] = carrinho
    request.session['selecionados'] = []

    return redirect('carrinho')
        
        