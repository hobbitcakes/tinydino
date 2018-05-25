#!/usr/bin/env bash

docker stop tinydinopy && docker rm tinydinopy
docker build -t petersonjared/tinydinopy:latest .
docker run -d -p 5000:5000 --name tinydinopy petersonjared/tinydinopy:latest
