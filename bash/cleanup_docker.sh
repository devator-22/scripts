#!/bin/bash

# This script removes all stopped Docker containers and dangling images.
## USAGE:
# chmod +x cleanup_docker.sh to change the permissions to executable
# ./cleanup_docker.sh to run the script

echo "Removing stopped containers..."
docker ps -a -f status=exited -q | xargs -r docker rm

echo "Removing dangling images..."
docker images -f dangling=true -q | xargs -r docker rmi

echo "Docker cleanup complete."