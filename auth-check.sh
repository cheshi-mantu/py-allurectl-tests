export ALLURE_ENDPOINT=$(<./tests/set/endpoint.txt)
export ALLURE_TOKEN=$(< ./tests/set/token.txt)
export ALLURE_PROJECT_ID=$(< ./tests/set/project.txt)

allurectl auth login