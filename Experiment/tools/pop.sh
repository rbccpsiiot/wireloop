cd ..
lastUID=$(ls users | sort -n | tail -1)
mkdir -p roughspace


if [ -z $lastUID ]
then
echo "users is empy. Exiting..."
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
mv users/$lastUID roughspace/
fi


