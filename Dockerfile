FROM python:3.6.5-slim-stretch 
RUN python3 -m pip install flask
ADD ./dino-server.py ./ 
expose 5000
ENTRYPOINT python3 ./dino-server.py
