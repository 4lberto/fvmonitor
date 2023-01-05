#!/bin/bash


echo "*** Starting loop IN THE BACKGROUND"
echo "ps -aux |grep python  --- to see if it is running"
echo "kill the process to stop it"
pipenv run python loop_insert.py & disown


