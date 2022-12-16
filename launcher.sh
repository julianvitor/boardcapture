#!/bin/sh
# launcher.sh
echo 'wating for network'
sleep 10
sudo raspi-config nonint do_camera 1
sudo apt-get update
yes
sudo apt-get install unattended-upgrades
yes
sudo apt-get install git
yes
sudo apt-get install pip
yes
sudo pip install -r requirements.txt
cd boardcapture
git config pull.rebase true
git pull origin main
python3 start.py
