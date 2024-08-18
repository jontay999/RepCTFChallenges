```
docker build -t repctf-pwn-5 .
docker run -d -p 2005:5000 --name pwn-fmt-2 --privileged repctf-pwn-5
```

NOTE THAT ASLR IS TURNED ON FOR THIS CHALLENGE

```
docker exec -it pwn-fmt-2 sh
docker logs pwn-fmt-2

// need to copy the libc used here to serve
docker cp 11e9471bd61b:/srv/lib/x86_64-linux-gnu/libc.so.6 .
```
