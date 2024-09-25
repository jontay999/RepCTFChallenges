FROM node:20-alpine

RUN apk add --no-cache dumb-init && \
    addgroup inmate && \
    adduser --disabled-password --gecos "" --ingroup inmate inmate

WORKDIR /home/inmate/app
COPY package*.json ./
COPY server.js ./
COPY public/ ./public/

ENV NODE_ENV=production 
ENV FLAG=REP{p0lluti0n_is_a_pr0bl3m_even_in_c0de}
RUN chown -R inmate:inmate . && \
npm ci --omit=dev --ignore-scripts --no-audit --no-fund
USER inmate

ENTRYPOINT ["/usr/bin/dumb-init", "--"]
CMD ["node", "./server.js"]