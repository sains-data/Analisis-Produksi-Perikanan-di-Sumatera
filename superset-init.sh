#!/bin/bash

# Initialize the DB
superset db upgrade

# Create admin user
superset fab create-admin \
    --username admin \
    --firstname Superset \
    --lastname Admin \
    --email admin@superset.com \
    --password admin123

# Setup default roles and permissions
superset init