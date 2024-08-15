```
gcc -no-pie -o flow flow.c
```

```bash
# in the service/ directory
docker build -t repctf-pwn-flow-1 .

docker run -d -p 2001:5000 --name pwn-flow-1 --privileged repctf-pwn-flow-1

# debug
docker logs pwn-flow-1
```
