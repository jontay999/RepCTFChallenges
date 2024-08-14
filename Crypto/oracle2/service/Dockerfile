FROM python:3
WORKDIR /app

RUN useradd -m chall
RUN pip install pycryptodome
RUN apt update
RUN apt install -y socat

COPY oracle2.py .
COPY flag.txt .

RUN chmod +r oracle2.py
RUN chmod +r flag.txt

USER chall

ENTRYPOINT socat tcp-l:1337,fork,reuseaddr exec:"python oracle2.py"