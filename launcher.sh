#!/bin/sh
# launcher.sh
# navigate to home, file directory, execute python script and return home
# ensure this script is executable on linux by running:
# sudo chmod 755 launcher.sh

cd /
cd home/pi/swinburne
sudo python myip.py
cd /