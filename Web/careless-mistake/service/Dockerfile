FROM python:3.9.2-slim-buster

RUN pip install flask gunicorn --no-cache-dir

WORKDIR /app
COPY server.py ./
COPY templates/ ./templates/

ENV FLASK_KEY=a25fda70d4a94ee66872cf8194243a70

CMD ["gunicorn", "-w3",  "--graceful-timeout", "0", "-unobody", "-gnogroup", "-b0.0.0.0", "app:app"]