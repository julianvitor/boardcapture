#!/bin/sh
# launcher.sh
echo 'wating for network'
sleep 5
cd boardcapture
git config pull.rebase true
git pull origin main
sudo raspi-config nonint do_camera 1
sudo apt-get update 
sudo yes | apt-get install unattended-upgrades
sudo yes | pip install -r requirements.txt
git config pull.rebase true
git pull origin main
python3 start.py
