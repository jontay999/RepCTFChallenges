FROM node:20-alpine

RUN apt-get update && \
apt-get install -y dumb-init && \
rm -rf /var/lib/apt/lists/* && \
addgroup inmate && \
adduser --disabled-password --gecos "" --ingroup inmate inmate

WORKDIR /home/inmate/app
COPY package*.json ./
COPY server.js ./

ENV NODE_ENV=production 
RUN chown -R inmate:inmate . && \
RUN npm ci --omit=dev --ignore-scripts --no-audit --no-fund
USER inmate

ENTRYPOINT ["/usr/bin/dumb-init", "--"]
CMD ["node", "./server.js"]