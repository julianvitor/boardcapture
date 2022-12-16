#!/bin/sh
# launcher.sh

sudo apt update
sudo timedatectl set-ntp true
sudo apt install git
git clone https://github.com/julianvitor/boardcapture.git
cd boardcapture
git pull origin main
python3 start.py
