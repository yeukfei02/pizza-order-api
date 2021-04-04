# pizza-order-api

pizza-order-api

documentation: <https://documenter.getpostman.com/view/3827865/TzCL9UXJ>

## Requirement

- install python(3.8)
- install pip3
- install postgres

## Testing and run

```zsh
// use requirements.txt
$ pip3 install -r requirements.txt

// run api
$ uvicorn app:app --reload
```

## Docker

```zsh
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
