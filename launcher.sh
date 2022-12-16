#!/bin/sh
# launcher.sh
echo 'wating for network'
sleep 5
sudo git config pull.rebase true
sudo git pull origin main
sudo raspi-config nonint do_camera 1 #raspi config enable camera
sudo yes | sudo apt-get update 
sudo yes | sudo apt-get install unattended-upgrades #security updates
sudo yes | sudo pip install -r requirements.txt
sudo git config pull.rebase true
sudo git pull origin main
sudo python3 start.py
