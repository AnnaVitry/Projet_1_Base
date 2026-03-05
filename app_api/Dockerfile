FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

WORKDIR /app

# Copie des fichiers de configuration uv
COPY pyproject.toml ./
RUN uv sync --no-cache

# Copie du code source
COPY . .

# IMPORTANT : On expose le port 8000
EXPOSE 8000

# On lance uvicorn sur 0.0.0.0 pour être visible par les autres conteneurs
CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]