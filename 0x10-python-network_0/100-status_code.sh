#!/bin/bash
# 5. cURL POST parameters
curl -s "$1" | grep HTTP/ | awk '{print $2}'
