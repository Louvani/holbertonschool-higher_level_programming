#!/bin/bash
# 3. cURL only methods
curl -sI "$1" | grep "^Allow" | cut -c 7-