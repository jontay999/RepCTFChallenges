# Format 2

**Category**: Pwn

[Solution](solve/solve.py)

## Description

This feels like a bit of a step up....

## Difficulty

Medium

## Deployment

```
docker build -t repctf-pwn-5 .
docker run -d -p 2005:5000 --name pwn-fmt-2 --privileged repctf-pwn-5
```

- turn on ASLR, make sure that the libc version in the container matches the container

```
docker exec -it pwn-fmt-2 sh
docker logs pwn-fmt-2

// need to copy the libc used here to serve
docker cp 11e9471bd61b:/srv/lib/x86_64-linux-gnu/libc.so.6 .
```
