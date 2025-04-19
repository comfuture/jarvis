FROM python:3.12
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv
ENV UV_SYSTEM_PYTHON=1
WORKDIR /app
ADD . /app
RUN uv sync --frozen
ENTRYPOINT [ "uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000" ]
