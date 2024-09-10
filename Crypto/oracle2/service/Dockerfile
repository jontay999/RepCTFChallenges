FROM python:3-slim
WORKDIR /app

RUN useradd -m chall \
&& pip install pycryptodome \
&& apt update \
&& apt install -y socat \
&& apt-get clean && rm -rf /var/lib/apt/lists/*

COPY oracle2.py .
COPY flag.txt .

RUN chmod +r oracle2.py \
&& chmod +r flag.txt

USER chall

ENTRYPOINT socat tcp-l:1337,fork,reuseaddr exec:"python oracle2.py"