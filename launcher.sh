#!/bin/sh
# launcher.sh
echo 'wating for network'
sleep 10
sudo su
cd boardcapture
git config pull.rebase true
git pull origin main
raspi-config nonint do_camera 1 #raspi config enable camera
yes | apt-get update 
yes | apt-get install unattended-upgrades #security updates
yes | pip install -r requirements.txt
python3 start.py
