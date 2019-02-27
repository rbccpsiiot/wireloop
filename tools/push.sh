cd ..
lastUID=$(ls roughspace | sort -n | tail -1)
mkdir -p users

if [ -z $lastUID ]
then
echo "roughspace is empty. Exiting..."
exit
fi

echo "-----------------------"
echo "Last UID -> $lastUID"
username=$(cat users/$lastUID/$lastUID)
echo "Content -> $username"
echo "-----------------------"

read -p "Sure? N/y " ans

if [ "$ans" = "y" ]
then
mv roughspace/$lastUID users/
fi


