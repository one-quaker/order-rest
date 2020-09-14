# REST API application

edit `env.example` and save as `env`

create `.env` file and add this line `DEBUG=1` into it

setup docker container `make force_rebuild_docker`

`make` - enter inside docker container

inside docker container run `make` again

### Available urls

http://localhost:8300/doc/ # API documentation

http://localhost:8300/api/v1/order/ # order list

http://localhost:8300/api/v1/table/ # table list

http://localhost:8300/api/v1/customer/ # customer list

http://localhost:8300/api/v1/table-order-date/12-09-2020 # table is reserved for specified date?
