# VehicleTracker - API

![status](https://img.shields.io/badge/status-Estável-brightgreen)
<!-- Outras opções futuras:
![status](https://img.shields.io/badge/status-Em%20Desenvolvimento-yellow)
![status](https://img.shields.io/badge/status-Em%20Manutenção-red)
-->
Este é um projeto iniciante com o objetivo de exercitar e demonstrar o uso das principais funcionalidades do framework FastAPI.  

A API foi pensada como uma base para estudar conceitos como rotas REST, modelos relacionais, documentação automática, autenticação e deploy.
Para fins práticos, o projeto utiliza como exemplo a estrutura de uma plataforma de rastreamento veicular, permitindo o cadastro de veículos e rastreadores, simulando uma aplicação real com múltiplas funcionalidades.
<!--
## 🔗 API em Produção (Deploy Render)

Acesse a API em produção por este link:  
👉 [`https://tracking-api.onrender.com`](https://tracking-api.onrender.com)

Documentação interativa (Swagger UI):  
👉 [`https://tracking-api.onrender.com/docs`](https://tracking-api.onrender.com/docs) -->

## Funcionalidades
- Cadastro de usuarios
- Cadastro de rastreadores
- Cadastro veiculos
- Vinculação de rastreador com usuario
- Relacionamento 1:1 entre veículo e rastreador
- Endpoints documentados com Swagger UI
- Atualização e remoção de registros
- Banco de dados SQLite

## Tecnologias
- Python 3.x
- FastAPI
- SQLModel
- SQLite

## Como executar localmente
```bash
git clone https://github.com/0Willp/tracking-api
cd tracking-api
python -m venv venv
source venv/bin/activate - macOS
cd venv/Scripts/acticate - windows
pip install -r requirements.txt
cd app
uvicorn app:app --reload
```

Acesse a documentação interativa em:  
`http://127.0.0.1:8000/docs`

---

## Próximas Funcionalidades (em desenvolvimento)

O projeto será evoluído com foco em demonstrar o máximo das capacidades do FastAPI. Algumas melhorias previstas:

- 🔐 Autenticação e autorização com OAuth2 + JWT  
- 👥 Controle de permissões por tipo de usuário (admin, cliente, operador)    
- 📄 Validação avançada de dados com Pydantic  
- 🧪 Testes automatizados com Pytest  
- 📈 Versionamento de API (ex: `/v1/`, `/v2/`)   
- 📁 Upload de arquivos (documentos, imagens dos veículos)  
- 🧩 Integração com serviços externos (ex: mapas ou notificações)  
- 🔍 OpenAPI Tags + descrição personalizada para melhor documentação  
- 📬 Webhooks ou eventos para integração em tempo real
- 🔗 Deploy com Render
---

## Autor
Willian Machado