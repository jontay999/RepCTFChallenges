FROM pwn.red/jail

COPY --from=python:3.11-slim-bookworm / /srv
COPY --chmod=755 jail4.py /srv/app/run