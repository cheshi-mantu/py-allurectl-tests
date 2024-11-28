export ALLURE_TOKEN=$(cat ../secrets/xyz-token.txt)
export ALLURE_ENDPOINT=$(cat ../secrets/xyz-endpoint.txt)
export ALLURE_PROJECT_ID=1
export ALLURE_LAUNCH_NAME="checking various attachments"
export ALLURE_RESULTS=allure-results

./allurectl watch -- pytest ./tests --alluredir=${ALLURE_RESULTS}