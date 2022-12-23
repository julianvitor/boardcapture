#!/bin/sh
# launcher.sh
echo 'wating 2 seconds for network and time synchronization'
sleep 2
cd boardcapture
cd /home/pi/boardcapture
git config pull.rebase true
git pull origin main
sudo raspi-config nonint do_camera 1 #raspi config enable camera
yes | sudo apt install unattended-upgrades #security updates
yes | sudo timedatectl set-ntp true         #time synchronization
yes | sudo systemctl restart systemd-timesyncd
yes | sudo apt install pip
yes | sudo pip install --upgrade pip setuptools wheel
yes | sudo pip install -r requirements.txt
yes | sudo pip install -r /home/pi/boardcapture/requirements.txt
python3 /home/pi/boardcapture/start.py
python3 start.py
