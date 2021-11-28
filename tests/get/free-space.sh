#!/bin/bash

ARR=$(df -h --total | grep "total" | xargs)
ARR=(${ARR//' '/ })
echo "${ARR[3]}"