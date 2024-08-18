```bash
docker build -t repctf-web-0 .
# note that nginx by default serves it on port 80
docker run -d -p 3000:80 --name web-0 repctf-web-0
```

```
REP{th3_f1r5t_5t3p_t0_s0lv1ng_w3b_cH4ll3ng3s_i5_r34d1ng_c0de_c4r3fully_bda07aac53a72bebbb7c95f6b31f8fae}
```
