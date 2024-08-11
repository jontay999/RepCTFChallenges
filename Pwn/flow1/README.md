# Flow 1

**Category**: Pwn

[Solution](solve/solve.py)

## Description

Welcome to the start of binary exploitation!

## Difficulty

Easy

## Deployment

- Locally

```bash
# in the service/ directory
docker build -t repctf-pwn-flow-1 .

docker run -d -p 2001:1337 --name pwn-flow-1 repctf-pwn-flow-1

# debug
docker logs pwn-flow-1
```

## Distributed Files

- All files under `/distrib`
