### How to run application

```bash
docker-compose up
```



```bash

# Docker-compose related commands
docker run -it phonebook /bin/bash              # SSH into docker image 
docker-compose up               # Run all services
docker-compose build api        # Builds concrete service 
docker-compose run api yoyo     # Run concrete program (yoyo) on service api

# We have entities user and entry
docker-compose run api yoyo new ./.migrations -m "Create entry"         # create first migration when do not have yoyo.ini 
docker-compose run api yoyo new -m "Create entry"                       # For every next migration because we have yoy.ini file, do not required to specify migration path
docker-compose run api yoyo apply --database postgresql://postgres_u:postgres_p@postgres:5432/postgres_db ./.migrations
```