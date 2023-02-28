#!/opt/homebrew/bin/bash
while true
do
    pytest ${PWD}/tests/ch1 --alluredir=${PWD}/allure-results/
done