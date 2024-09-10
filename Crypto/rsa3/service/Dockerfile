FROM python:3-slim
WORKDIR /app

RUN useradd -m chall \
&& pip install pycryptodome \
&& apt update \
&& apt install -y socat

COPY encrypt.py .
COPY flag.txt .

RUN chmod +r encrypt.py && chmod +r flag.txt

USER chall

ENTRYPOINT socat tcp-l:1337,fork,reuseaddr exec:"python encrypt.py"