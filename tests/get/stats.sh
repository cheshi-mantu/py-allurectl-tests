#!/bin/bash
allurectl launch list --project-id ${ALLURE_PROJECT_ID} --output json --size 1 --no-header
export ALLURE_LAUNCH_ID=$(allurectl launch list --project-id ${ALLURE_PROJECT_ID} --output json --size 1 | jq -r .[0].id)
echo "${ALLURE_LAUNCH_ID}"