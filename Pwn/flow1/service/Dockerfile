FROM ubuntu:22.04

RUN useradd -m test

WORKDIR /home/test

COPY flow .
COPY flag.txt .
COPY run.sh .

RUN chmod 755 run.sh
RUN chmod 755 flow
RUN chmod +r flag.txt
RUN apt update
RUN apt install -y socat

USER test

EXPOSE 1337

ENTRYPOINT socat tcp-l:1337,fork,reuseaddr exec:./run.sh