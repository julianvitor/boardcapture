# comandos para o crontab (crontab -e)

@reboot sudo sh /home/pi/boardcapture/launcher.sh >/home/pi/boardcapture/logs/cronlog 2>&1
0 5 * * * sudo reboot



# comandos sistema
sudo timedatectl set-ntp true
sudo systemctl restart systemd-timesyncd

# parametros do sistema

ssh = pi
senha = **12345678**

wifi = pi
senha = **12345678**

usuario = pi
senha = **12345678**

# raspi config (sudo raspi-config)

teclado
autostart
enable camera
update

# instalar o boardcap
sudo apt install git
git clone https://github.com/julianvitor/boardcapture.git
cd boardcapture & sh launcher.sh

# reinicie