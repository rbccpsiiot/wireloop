
#!/bin/bash
. activate.sh

if [ -z $BASH ]
then
echo "Please run using -> bash $0 and not sh $0"
exit
fi

if [ -z $1 ]
then
echo "Enter username... Usage -> bash $0 username "
exit
fi


uname=$1

uid=$(ls users | sort -n | tail -1)
uid=$(echo "$uid+1" | bc)

if [ -z $uid ]
then
uid=1
fi

pushd dactools
sh acquire.sh
popd


echo "----------------"
echo "Username: $uname"
echo "UserID: $uid"
echo "----------------"
echo ""
read -p "Proceed? N/y?  " ans
echo $ans

if [ "$ans" = "y" ]
then
mkdir -p users/$uid
echo "$uname: $uid" > users/$uid/$uid

echo "-------------------------------------"
echo "Created new user $uname in folder $uid"
echo "-------------------------------------"
echo ""

screen -S listen -X kill


echo "Copying dactools to user folder..."
cp dactools/*.py users/$uid/
cd users/$uid/

screen -d -S listen -m bash -c "python3 listen.py"

echo "Running video --->"

vlc --fullscreen --play-and-exit ~/Downloads/GSRExptvideo.mp4 >> /dev/null 2>&1

echo "Video done."
echo ""

echo "Starting GAME in..."

for i in {1..10}
do
printf $(echo "10-$i" | bc)
sleep 1
printf " "
done
echo ""
echo ""
echo ""


#call the event Monitoring Python Script
python3 wireloopEvents.py


python3 score.py 2>&1 | tee -a $uid

if [ -z $NOCOUNTDOWN ]
then
	for i in {1..90}
	do
	printf $(echo "90-$i" | bc)
	sleep 1
	printf " "
	done
fi


screen -S listen -X kill
screen -S ESDACQ -X kill


echo ""
echo "Saving data into CSVs"

python3 makecsv.py
rm data.dat

echo "Removing dactool files from user folder...."
rm *.py

echo ""
echo "Filtering 50Hz..."
#echo `pwd`

cd ../../remove50hz
#echo `pwd`
#python3 -W ignore filter50Hz.py $uid
sh pyrun.sh $uid
echo ""

cd ..
python3 plotEXP.py $uid
fi

echo "--------"
echo "Exiting"
echo "--------"
