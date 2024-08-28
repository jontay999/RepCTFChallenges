## Admin

```bash
docker build -t repctf-web-4-admin .
docker run -d -p 3004:3000 --name web-4-admin repctf-web-4-admin
```

## App

```bash
docker build -t repctf-web-4-app .
docker run -d -p 3004:3000 --name web-4-app repctf-web-4-app
```
