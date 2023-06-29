ITERATIONS="1,2,3"
for ineration in ${ITERATIONS}
    do
        pytest ./tests/ch1 --alluredir=allure-results
    done