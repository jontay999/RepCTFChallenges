FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
  xinetd \
  python3-pip \
  && rm -rf /var/lib/apt/lists/* \
  && mkdir /ctf

WORKDIR /ctf

RUN useradd -M -d /ctf ctf \
&& echo "Connection blocked" > /etc/banner_fail

COPY ctf.xinetd /etc/xinetd.d/ctf
COPY ./src /ctf/

RUN chown -R ctf:ctf /ctf && chmod -R 770 /ctf \ 
  && pip3 install --no-cache-dir torch --index-url https://download.pytorch.org/whl/cpu \
  && pip3 install --no-cache-dir transformers \
  && mkdir /ctf/saved-model \
  && python setup.py \ 
  && chown -R root:ctf /ctf \
  && chmod -R 770 /ctf


ENTRYPOINT ["/usr/sbin/xinetd", "-dontfork"]

EXPOSE 1337
