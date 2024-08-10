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
