#!/usr/bin/env bash

docker stop tinydinopy && docker rm tinydinopy
docker build -t petersonjared/tinydinopy:latest .
docker run -d -p 5000:5000 --name tinydinopy petersonjared/tinydinopy:latest

echo "1" ; sleep 1 
echo "2" ; sleep 1 
echo "3" ; sleep 1 
curl -k -s http://192.168.0.87:5000/GetResponse | python -m json.tool
curl -k -s http://192.168.0.87:5000/GetNextInteger/1 | python -m json.tool 
curl -k -s http://192.168.0.87:5000/GetAllCaps/upper | python -m json.tool || docker logs tinydinopy
