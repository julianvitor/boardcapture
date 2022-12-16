#!/bin/sh
# launcher.sh
echo 'wating for network'
sleep 10
sudo raspi-config nonint do_camera 0
sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get install git
sudo apt-get install pip
sudo pip install -r requirements.txt
git clone https://github.com/julianvitor/boardcapture.git
cd boardcapture
git config pull.rebase true
git pull origin main
python3 start.py
