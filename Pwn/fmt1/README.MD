# Format 1

**Category**: Pwn

[Solution](solve/solve.py)

## Description

No more buffer overflows!

## Difficulty

Easy

## Deployment

```
docker build -t repctf-pwn-4 .
docker run -d -p 2004:5000 --name pwn-fmt-1 --privileged repctf-pwn-4

```

- Disable ASLR

```
docker exec -it pwn-fmt-1 sh
echo 0 | tee /proc/sys/kernel/randomize_va_space
```
