```
docker build -t repctf-pwn-5 .
docker run -d -p 2005:5000 --name pwn-fmt-2 --privileged repctf-pwn-5

```

IMPT TO DISABLE ASLR

```
docker exec -it pwn-fmt-2 sh
echo 0 | tee /proc/sys/kernel/randomize_va_space
```
