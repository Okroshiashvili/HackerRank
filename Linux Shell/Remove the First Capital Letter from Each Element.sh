#! /bin/bash

read array 

echo ${array[@]/[A-Z]/.}
