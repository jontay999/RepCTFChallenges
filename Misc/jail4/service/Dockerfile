FROM pwn.red/jail

COPY --from=python:3.8.0-slim / /srv
COPY --chmod=755 jail4.py /srv/app/run