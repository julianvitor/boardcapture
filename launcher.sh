#!/bin/sh
# launcher.sh
echo 'wating for network'
sleep 10
cd boardcapture
sudo git config pull.rebase true
sudo git pull origin main
sudo raspi-config nonint do_camera 1 #raspi config enable camera
yes | sudo apt update 
yes | sudo apt install unattended-upgrades #security updates
yes | sudo timedatectl set-ntp true
yes | sudo systemctl restart systemd-timesyncd
yes | sudo apt install pip
yes | sudo pip install --upgrade pip setuptools wheel
yes | sudo pip install -r requirements.txt
sudo python3 start.py
