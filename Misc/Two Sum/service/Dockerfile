# Build Stage
FROM ubuntu:24.04 AS build

RUN apt-get update && apt-get install -y \
    g++-13 \
    libstdc++6 \
    && apt-get clean

# Release stage
FROM pwn.red/jail

ENV JAIL_TIME=2000
ENV JAIL_MEM=20M

COPY --from=build / /srv
COPY --chmod=755 two_sum /srv/app/run