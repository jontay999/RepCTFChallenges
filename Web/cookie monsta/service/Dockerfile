FROM node:18-buster-slim
RUN apt-get update && \
apt-get install -y chromium && \
rm -rf /var/lib/apt/lists/* && \
groupadd -r appuser && useradd -r -g appuser appuser

ENV NODE_ENV=production \
PUPPETEER_SKIP_CHROMIUM_DOWNLOAD=true \
PUPPETEER_EXECUTABLE_PATH=/usr/bin/chromium \ 
FLAG=REP{cr055_51t3_5cr1pt1ng_15_d4ng3r0u5_afbab247fce54db26764edbbbf534fb4}

WORKDIR /usr/src/app
COPY --chown=appuser:appuser package*.json ./
COPY --chown=appuser:appuser public ./public/
COPY --chown=appuser:appuser server.js ./

RUN npm ci --omit=dev --ignore-scripts --no-audit --no-fund
USER appuser

EXPOSE 3000
CMD [ "node", "server.js" ]