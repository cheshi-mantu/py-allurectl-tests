#!/bin/bash
TIME_STAMP=$(date +%Y%m%d-%H%M)

export FREE_SPACE=$(./get/free-space.sh)
export CPU_TYPE=$(uname -p)
export TEST_HOST=$(hostname -I)
export OS_NAME=$(./get/os.sh)

ALLURECTL_VER=$(allurectl --version)
export ALLURECTL_VERSION=${ALLURECTL_VER/version/}


#connection settings
export ALLURE_ENDPOINT=$(<./set/endpoint.txt)
export ALLURE_TOKEN=$(< ./set/token.txt)
export ALLURE_PROJECT_ID=$(< ./set/project.txt)


# launch's configuration
export ALLURE_LAUNCH_NAME="${TIME_STAMP} pytest from $(TEST_HOST)"
export ALLURE_RESULTS=./allure-results
export COMMAND_USED=watch
export ALLURE_LAUNCH_TAGS="pytest, allurectl, ${COMMAND_USED}"

rm -r ./allure-results/*
sleep 3

echo "-----> ${TIME_STAMP} ${COMMAND_USED} <-----"

allurectl ${COMMAND_USED} -- pytest /home/cheshi/tests/ch1 --alluredir=/home/cheshi/tests/allure-results/

sleep 10
export COMMAND_USED=upload

echo "-----> ${TIME_STAMP} ${COMMAND_USED} <-----"

export ALLURE_LAUNCH_TAGS="pytest, allurectl, ${COMMAND_USED}"

allurectl ${COMMAND_USED} ./allure-results

