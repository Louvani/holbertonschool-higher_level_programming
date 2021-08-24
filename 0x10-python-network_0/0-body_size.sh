#!/bin/bash
# 0. cURL body size
curl -sI "$1" | grep "^Content-Length" | cut -c 17-
