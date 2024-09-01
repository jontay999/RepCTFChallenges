# Flow 3

**Category**: Pwn

[Solution](solve/solve.py)

## Description

How do I even pass this check?

## Difficulty

Medium

## Deployment

```
docker build -t repctf-pwn-3 .
docker run -d -p 2003:5000 --name pwn-flow-3 --privileged repctf-pwn-3

```

- Disable ASLR for this challenge

```
docker exec -it pwn-flow-3 sh
echo 0 | tee /proc/sys/kernel/randomize_va_space
```
