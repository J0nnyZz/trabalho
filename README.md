# Projeto Formativo DevOps (CI/CD + Docker)

Projeto simples em Python com Flask para praticar fluxo real de CI/CD com GitHub Actions e conteinerizacao com Docker.

## Funcionalidades

- `GET /` retorna mensagem de status do projeto.
- `GET /health` retorna healthcheck.
- `GET /sum/<a>/<b>` retorna soma de dois inteiros.

## Requisitos

- Python 3.12+
- Docker Desktop (para etapa de container)

## Executar localmente

```bash
python -m venv .venv
.venv\\Scripts\\activate
pip install -r requirements.txt
python -m src.app
```

Aplicacao em `http://localhost:5000`.

## Rodar testes e lint

```bash
pytest -q
ruff check .
```

## Build e execucao com Docker

```bash
docker build -t devops-formativo:local .
docker run --rm -p 5000:5000 devops-formativo:local
```

Depois teste em `http://localhost:5000/health`.

## CI/CD configurado

- CI: `.github/workflows/ci.yml`
  - Dispara em PR para `main` e em push para `main`, `dev` e `feature/**`.
  - Executa lint (Ruff) e testes (Pytest).
- CD: `.github/workflows/cd.yml`
  - Dispara em push para `main`.
  - Builda e publica imagem Docker no GHCR: `ghcr.io/<usuario>/<repositorio>`.

