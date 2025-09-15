# wsBackend-Fabrica25.2  
## Projeto Django - Login, Cadastro e Carrinho  

Projeto Django com funcionalidades de **login**, **cadastro de usuários** e **carrinho de compras**.  

---

## 🚀 Pré-requisitos  

- Python **3.13**  
- **pip** (gerenciador de pacotes)  

---

## ⚙️ Instalação e Configuração  

### 1. Criar e ativar o ambiente virtual  

```bash
# Criar o ambiente virtual
python -m venv venv

# Ativar no Windows
venv\Scripts\activate

# Ativar no Linux / macOS
source venv/bin/activate
```

---

### 2. Instalar dependências  

```bash
pip install django
pip install requests
```

---

### 3. Aplicar migrações  

```bash
python manage.py migrate
```

---

### 4. Criar superusuário (opcional, para acessar o Django Admin)  

```bash
python manage.py createsuperuser
```

Acesse o painel administrativo em: [http://127.0.0.1:8000/admin]  

---

### 5. Rodar o servidor de desenvolvimento  

```bash
python manage.py runserver
```

Acesse o projeto em: [http://127.0.0.1:8000]  

---

## 📌 Funcionalidades  

- Cadastro e login de usuários  
- Atualização e deleção de cadastro  
- Carrinho de compras com seleção de produtos  

---
