# Docker

[Docker Cheat Sheet](https://dockerlabs.collabnix.com/docker/cheatsheet/)

## docker Befehle

```
# Build Image       
docker build -t nginx-test .
# Run Container
docker run -d -p 80:80 --name nginx-test-container nginx-test
# Delete Container
docker rm -f nginx-test-container
# Run Container + Volume
docker run -d -p 80:80 --name nginx-test-container -v $PWD/nginx-volume/:/usr/share/nginx/html/ nginx-test
# Accsess Container
docker exec -it nginx-test-container /bin/bash
```