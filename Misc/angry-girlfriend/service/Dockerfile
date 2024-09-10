FROM python:3.11-slim-buster

RUN apt-get update && apt-get install -y \
  xinetd \
  python3-pip \
  python3-dev \
  && rm -rf /var/lib/apt/lists/* \
  && pip install --upgrade pip \
  && mkdir /ctf

WORKDIR /ctf
RUN useradd -M -d /ctf ctf

RUN echo "Connection blocked" > /etc/banner_fail
COPY ctf.xinetd /etc/xinetd.d/ctf
COPY ./src /ctf/

RUN chown -R ctf:ctf /ctf && chmod -R 770 /ctf \ 
  && pip3 install --no-cache-dir transformers torch --index-url https://download.pytorch.org/whl/cu118 \
  && mkdir /ctf/saved-model \
  && python setup.py \ 
  && chown -R root:ctf /ctf \
  && chmod -R 770 /ctf


ENTRYPOINT []
CMD ["/usr/sbin/xinetd", "-dontfork"]

EXPOSE 1337
