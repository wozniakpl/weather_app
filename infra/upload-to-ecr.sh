#!/bin/bash

set -euo pipefail

# Retrieve an authentication token and authenticate your Docker client to your registry.
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 244601572382.dkr.ecr.us-east-1.amazonaws.com

# Build your Docker image using the following command.
docker build --tag weather-ecr --target dist ../backend

# After the build completes, tag your image so you can push the image to this repository:
docker tag weather-ecr:latest 244601572382.dkr.ecr.us-east-1.amazonaws.com/weather-ecr:latest

# Run the following command to push this image to your newly created AWS repository:
docker push 244601572382.dkr.ecr.us-east-1.amazonaws.com/weather-ecr:latest