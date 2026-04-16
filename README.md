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

## Roteiro para cumprir a atividade

1. Crie repositório publico no GitHub.
2. Suba este projeto no branch `main`.
3. Crie ao menos um branch extra (ex.: `dev` ou `feature/inicial`).
4. Faça pelo menos 5 commits no total nesses branches.
5. Abra uma PR para `main` e faça merge.
6. Verifique os workflows CI e CD passando com sucesso.
7. Rode o container localmente com Docker.
8. Tire os 4 prints obrigatorios.

## Checklist dos 4 prints obrigatorios

1. Print do repositorio com URL visivel e conteudo.
2. Print da PR com CI e CD passando.
3. Print do `docker ps` mostrando o container em execucao.
4. Print do Dockerfile no repositorio (ou enviar o arquivo Dockerfile).
