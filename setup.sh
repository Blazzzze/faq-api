#!/bin/sh

# This script installs Redis, sets up Python dependencies, and prepares the environment.
# This script only supports debian based linux.

# Add the repository to the APT index, update it, and install Redis.
# Source: https://redis.io/docs/latest/operate/oss_and_stack/install/install-redis/install-redis-on-linux/#connect-to-redis
sudo apt-get install lsb-release curl gpg
curl -fsSL https://packages.redis.io/gpg | sudo gpg --dearmor -o /usr/share/keyrings/redis-archive-keyring.gpg
sudo chmod 644 /usr/share/keyrings/redis-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/redis-archive-keyring.gpg] https://packages.redis.io/deb $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/redis.list
sudo apt-get update
sudo apt-get install redis

# Install relevant python modules;
# for full list of dependency modules navigate to ./requirements.txt
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
