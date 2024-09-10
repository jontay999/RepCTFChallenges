# Lost Modulus

**Category**: Crypto

[Solution](solve/solve.py)

## Description

I've hidden my flag as a modulus, I'm sure no one will be able to retrieve it.

## Difficulty

Medium

## Deployment

- Locally

```
docker build -t repctf-crypto-lost-modulus ./service/

docker run -d -p 1001:1337 --name lost-modulus repctf-crypto-lost-modulus

```

- possibly for afterwards
  `docker-compose up -d`

## Distributed Files

- All files under `/distrib`
