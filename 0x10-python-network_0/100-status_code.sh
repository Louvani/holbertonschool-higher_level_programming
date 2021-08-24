#!/bin/bash
# 5. cURL POST parameters
curl -s -o /dev/null --head --write-out '%{http_code}' $1
