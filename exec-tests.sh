ITERATIONS="1,2,3"
for ineration in ${ITERATIONS}
    do
        pytest ./tests --alluredir=allure-results
    done