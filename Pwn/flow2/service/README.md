```bash
# in the service/ directory
docker build -t repctf-pwn-flow-2 .

docker run -d -p 2002:5000 --name pwn-flow-2 --privileged repctf-pwn-flow-2

# debug
docker logs pwn-flow-2
```
