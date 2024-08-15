```bash
# in the service/ directory
docker build -t repctf-pwn-flow-2 .

docker run -d -p 2002:1337 --name pwn-flow-2 repctf-pwn-flow-2

# debug
docker logs pwn-flow-2
```
