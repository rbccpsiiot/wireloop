cd ..
read -p "Are you very sure? N/y " ans

if [ "$ans" = "y" ]
then
rm -r users/*
ls
fi
