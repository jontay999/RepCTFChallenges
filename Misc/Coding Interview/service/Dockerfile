# Build Stage
FROM ubuntu:24.04 AS build

RUN apt-get update && apt-get install -y \
    g++-13 \
    libstdc++6 \
    && apt-get clean

# COPY two_sum.cpp /usr/src/two_sum.cpp
# RUN g++-13 -o two_sum two_sum.cpp
# WORKDIR /usr/src

# Release stage
FROM pwn.red/jail

ENV JAIL_TIME=2000
ENV JAIL_MEM=20M

COPY --from=build / /srv
COPY --chmod=755 service3 /srv/app/run

# strings /srv/lib/x86_64-linux-gnu/libstdc++.so.6 | grep "GLIBC"