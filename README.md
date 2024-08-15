# RepCTFChallenges

## Running challenges from the `Dockerfile`

1. Building the Docker image from the Dockerfile

```bash
docker build -t <image-name> .
```

Enforce that `<image-name>` be of the format `repctf-<category>-<challenge-name>`

2. Running the Docker container

```
docker run -d --name my-container-name my-image-name
```

## Overview of Challenges

### Crypto

1. `brute1` (easy) (done)

- AES Encryption
- key of 3 random bytes
- brute force

2. `brute2` (medium) (done)

- AES Encryption
- key of 5 random hex characters
- flag and known plaintext is encrypted twice with 2 keys
- use meet in the middle attack
- encrypt known plaintext, decrypt the encrypted plaintext to derive keys

3. `rsa1` (easy) (done)

- primes are close together
- square root `n` to derive `p` and `q`

4. `rsa2` (easy) (done)

- primes are small, brute force and factorise or go online to find

5. `rsa3` (medium) (done)

- flag is hidden in the modulus
- send 2 plaintexts that are multiples of each other (cube)
- construct the equation and root it

6. `rsa4` (hard) (done)

- use groebner basis to solve polynonmial equations

7. `random1` (easy) (done)

- give 620 outputs, remaining 4 outputs can be derived from the flag
- derive mersenne twister
- xor the flag

8. `ecdsa` (medium) (done)

- nonce reuse

9. `oracle1` (hard) (done)

- CBC padding oracle

10. `oracle2` (hard) (done)

- manger's attack

### Pwn

1. `flow1` (easy) (done)

- buffer overflow, ret2win

2. `flow2` (easy) (done)

- shellcode

3. `flow3` (easy) (done)

- ret2win but use ROP to call function

4. `flow4` (medium)

- integer underflow to leak canary
- ROP chain to shell?

5. `format1` (medium)

- format string to leak canary
- do a libc leak
- then ret2win

6. `heap1` (hard)

7. `kernel1` (hard)

8. `browser1` (hard)

### Web

1. SQL Injection

- admin login screen
- basic xss sql

2. XSS

3. SSRF

4. Markdown Injection

5. Dom-clobbering

6. React stuff

7. XS-leaks

8. Prototype pollution

### RE

1. Assembly1 (easy)

- assembly instructions, what is the value of this register

2. password1 (easy)

- find the password with an if check against a server

3. password2 (easy)

- xor-encrypt the password with a special key

### Misc

1. Machine Learning1

- train a model to be bad at recognizing MNIST images

2. Machine Learning2

- adversarial image

3. Pyjail1

-

4. Pyjail2

- treebox of Google CTF

5. Blockchain1

6. Blockchain2

7. Hash tables

- slow down an operation based on primes
