#!/usr/bin/env bash

docker stop tinydinopy && docker rm tinydinopy
docker build -t hobbitcakes/tinydinopy:latest .
docker run -d -p 5000:5000 --name tinydinopy hobbitcakes/tinydinopy:latest

echo "1" ; sleep 1 
echo "2" ; sleep 1 
echo "3" ; sleep 1 
