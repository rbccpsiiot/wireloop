#echo "ok" | socat - udp-sendto:localhost:5000
python -u say.py | socat - udp-sendto:localhost:5000
#python iiot_2.py | socat - udp-sendto:192.168.77.104:5000

