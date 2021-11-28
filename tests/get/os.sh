#!/bin/bash
#getting os name
os_name=$(lsb_release -a | grep "Description")
os_name=(${os_name//' '/ })
echo "${os_name[1]} ${os_name[2]}"