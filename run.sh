#!/bin/bash
docker-compose up -d elasticsearch
docker-compose up -d kibana
docker-compose up -d postgres
#docker-compose build mysite --no-cache
docker-compose up mysite
