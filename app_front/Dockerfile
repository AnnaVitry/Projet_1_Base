FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

WORKDIR /app

COPY pyproject.toml uv.lock* ./
RUN uv sync --no-cache

COPY . .

EXPOSE 8501

# On force le mode headless et le port pour Docker
CMD ["uv", "run", "streamlit", "run", "app_front/main.py", "--server.port=8501", "--server.address=0.0.0.0"]