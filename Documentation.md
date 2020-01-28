# Project Flaski Resti
**NOTE**: Still in the making, just started.
## Description
This project is an extension of the project [Flask Rest Api the TDD Way](https://scotch.io/tutorials/build-a-restful-api-with-flask-the-tdd-way)
because we are building an Rest Api with timeseries data. Therefore we use the TimescaleDB extension for a Postgresql and use docker
instead of persisting Datbases on our System, which complicates things a little bit but ultimately gives us 
more flexibility. 

# Project Setup
**TODO**: ADD VOLUME TO POSTGRES that we do not have to recreate the creation steps. Create sql script
that we can develop on different machines.
## Docker Setup
We use timescaledb and pgadimer to manage our Database. The docker containers are created with
docker compose. See docker/docker-compose.yml for the setup. Run  `docker-compose up --remove-orphans`
to create your docker containers (Note we still need to add a volume to persists data).
### Creating Databases
We can either use the pgadminer tool --> connect via localhost:5050 and fill in your credentials
or directly via the docker container. First you have to get access to the container `docker exec -it -u dbuser dbcontainerid bash`. 
Then you can use the typical postgres syntax, to create a db use `createdb dbname`

## Python Packages
** Todo: Documentation of the used Python packages
* Flask-Api: Package to create an API that can be browsed (like Django REST framework)