export ISA_USER_ID=$1
export ISA_NO_PLOT=1

#python3 -m jupyter nbconvert --execute filter50Hz.ipynb
python3 -m nbconvert --execute filter50Hz.ipynb
