screen -S ESDACQ -X kill

#screen -d -m -S ESDACQ connectAndStart.sh
screen -d -S ESDACQ -m bash -c "cd ../bluepy; python2 iiot_2.py | socat - udp-sendto:localhost:5000"
