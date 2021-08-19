#!/bin/bash
# 5. cURL POST parameters
curl -s "$1" -I --write-out "%{http_code} $LINE\n" "$LINE" | grep "HTTP/" | awk '{print $2}'

