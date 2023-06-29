ITERATIONS="1,2,3"
for ineration in ${ITERATIONS}
    do
        pytest ${PWD}/tests/ch1 --alluredir=${PWD}/allure-results/
    done