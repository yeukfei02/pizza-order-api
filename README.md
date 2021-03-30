# pizza-order-api

pizza-order-api

documentation: https://documenter.getpostman.com/view/3827865/TzCL9UXJ

## Requirement

- install python(3.8)
- install pip3

## Testing and run

```
// use requirements.txt
$ pip3 install -r requirements.txt

// run api
$ uvicorn app:app --reload
```

## Docker

```
// build images and start container in one line
docker-compose up -d --build

// go inside container
docker exec -it <containerId> /bin/bash

// check container logs
docker logs <containerId>

// remove and stop container
docker-compose down
```

open localhost:8000
