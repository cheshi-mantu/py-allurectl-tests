#!/bin/bash
TIME_STAMP=$(date +%Y%m%d-%H%M)
export FREE_SPACE=$(./get/free-space.sh)
export CPU_TYPE=$(uname -p)
export TEST_HOST=$(hostname -I)
export OS_NAME=$(./get/os.sh)

ALLURECTL_VER=$(allurectl --version)
export ALLURECTL_VERSION=${ALLURECTL_VER/version/}

export ALLURE_ENDPOINT=$(<./set/endpoint.txt)
export ALLURE_TOKEN=$(< ./set/token.txt)
export ALLURE_PROJECT_ID=$(< ./set/project.txt)


# common configuration
export ALLURE_RESULTS=./allure-results


#Launch specific
export ALLURE_LAUNCH_NAME="${TIME_STAMP} pytest from ${TEST_HOST}"
export COMMAND_USED=watch
export ALLURE_LAUNCH_TAGS="pytest, allurectl, ${COMMAND_USED}"


#Launch specific
export COMMAND_USED=upload
export ALLURE_LAUNCH_TAGS="pytest, allurectl, ${COMMAND_USED}"
