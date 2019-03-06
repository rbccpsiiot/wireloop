export ISA_USER_ID=$1
export ISA_NO_PLOT=1

jupyter nbconvert --execute filter50Hz.ipynb
