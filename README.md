# 🚀 API Pizzaria

API desenvolvida com FastAPI para gerenciamento de pedidos em uma pizzaria.

## 🛠 Tecnologias

- Python 3.13.1
- FastAPI
- Uvicorn
- Pydantic
- SQLAlchemy
- Alembic

## 🐍 Ambiente Virtual

Este projeto utiliza um ambiente virtual (`.venv`) para isolamento das dependências.

Para criar o ambiente:

```
python -m venv .venv
```

Para ativar:

Windows

```
.venv\Scripts\activate
```

Linux/Mac

```
source .venv/bin/activate
```

Instalar dependências

```
pip install -r requirements.txt
```

## ▶️ Rodar a aplicação

```
uvicorn main:app --reload
```

A API estará disponível em

```
http://127.0.0.1:8000/
```

Documentação automática (Via Swagger)

```
http://127.0.0.1:8000/docs
```

## ⚙️ Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto:

```
SECRET_KEY=sua_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

## 📂 Estrutura do Projeto

```
.
├── alembic/
│   ├── versions/
│   │   └── 13a3ea60689a_adicionar_itens_ao_pedido.py
│   │   └── ab7358d5cd19_initial_migration.py
│   ├── README
│   ├── env.py
│   ├── script.py.mako
├── .env
├── .env.example
├── .gitignore
├── alembic.ini
├── auth_routes.py
├── dependencies.py
├── main.py
├── models.py
├── order_routes.py
├── README.md
├── requirements.txt
├── schemas.py
└── testes.py
```

![Python](https://img.shields.io/badge/python-3.13.1-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.128.0-green)
