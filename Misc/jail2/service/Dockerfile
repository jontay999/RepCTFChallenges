FROM pwn.red/jail

COPY --from=python:3.12-slim-bookworm / /srv
COPY --chmod=755 jail2.py /srv/app/run
COPY flag.txt /srv/app/flag.txt