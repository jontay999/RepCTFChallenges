# this is default bound to port 5000
FROM pwn.red/jail

COPY --from=ubuntu:22.04 / /srv
COPY --chmod=755 fmt2 /srv/app/run
COPY --chmod=744 flag.txt /srv/app/flag.txt