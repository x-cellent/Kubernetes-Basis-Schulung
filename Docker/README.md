# Docker

[Docker Cheat Sheet](https://dockerlabs.collabnix.com/docker/cheatsheet/)

## docker Befehle

```
# Build
docker build -t nginx-test .
# Run
docker run -d -p 80:80 --name nginx-test-container nginx-test
# Delete
docker rm -f nginx-test-container
# Run + Volume
docker run -d -p 80:80 --name nginx-test-container -v $PWD/nginx-volume/:/usr/share/nginx/html/ nginx-test
```