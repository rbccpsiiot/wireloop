#!/bin/bash

uid=$1

if [ -z $uid ]
then
echo "Provide UID"
exit
fi



pushd users/$1/
mv gsr_readings.csv.filtered xxx.filtered
popd
python3 plotEXP.py $uid
pushd users/$1/
mv xxx.filtered gsr_readings.csv.filtered
popd

