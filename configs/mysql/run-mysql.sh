#!/bin/bash

docker run \
    --name some-mysql \
    -e MYSQL_ROOT_PASSWORD=my-secret-pw \
    -d mysql:latest
