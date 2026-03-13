FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    POETRY_VERSION=2.2.1 \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1

WORKDIR /app

RUN pip install --no-cache-dir "poetry==$POETRY_VERSION"

COPY pyproject.toml poetry.lock ./
RUN poetry install --only main --no-root

# Install Playwright's Chromium browser and its OS dependencies
RUN poetry run playwright install --with-deps chromium

COPY sitegen/ ./sitegen/
COPY content/ ./content/

ENV PORT=8080 \
    HOST=0.0.0.0 \
    CONTENT_DIR=/app/content

EXPOSE 8080

CMD ["poetry", "run", "python", "-m", "sitegen.main"]
