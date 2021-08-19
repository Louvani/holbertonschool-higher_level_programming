#!/bin/bash
# 3. cURL only method
curl -sI "$1" | grep "Allow" | cut -c 8-