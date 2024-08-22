# this is default bound to port 5000
FROM pwn.red/jail

ENV JAIL_TIME 2000
ENV JAIL_MEM  20M

COPY --from=ubuntu:22.04 / /srv
COPY --chmod=755 two_sum /srv/app/run
COPY --chmod=744 flag.txt /srv/app/flag.txt