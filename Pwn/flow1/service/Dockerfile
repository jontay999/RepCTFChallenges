FROM ubuntu:16.04

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

EXPOSE 2001

ENTRYPOINT socat tcp-l:2001,fork,reuseaddr exec:./run.sh