#!/bin/bash

docker build -t llama-server .

# Adjust timeout and max workers as needed
docker run -p 80:80 -e MAX_WORKERS="1" -e TIMEOUT="600" llama-server
