FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

WORKDIR /app

# On copie les fichiers de configuration (Docker les cherchera dans le "contexte")
COPY pyproject.toml uv.lock* ./

# Installation des dépendances
RUN uv sync --frozen --no-cache

# Copie du reste du code
COPY . .

ENV PYTHONPATH=/app
EXPOSE 8000

# On lance le module proprement
CMD ["uv", "run", "uvicorn", "app_api.main:app", "--host", "0.0.0.0", "--port", "8000"]