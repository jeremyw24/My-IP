# My-IP
Basic python script to grab IP Address of connected ethernet adaptors and log to a file. This will report all loaded ethernet adaptors, future version to allow selection of ethernet adaptor at runtime, but currently not required.

Uses netifaces python package to read status of the ethernet adaptors.

##To Do
* Need to add escape clause eg. except KeyboardInterrupted
* Need to add a log message specific for when an IP Address is actually lost, rather than no-ip to report.
* Print to cli that IP Address has been lost to alert users that may be watching.

##For Use on Raspberry Pi
* Requires Python2.7 Dev Tools: `sudo apt-get install python2.7-dev`
* Requires pip installer: `sudo apt-get install python-pip`
* Requires netifaces library: `pip install netifaces`

###Disable Login Prompt on Raspberry Pi
* Edit inittab file: `sudo nano /etc/inittab`
* Comment out the following line: `1:2345:respawn:/sbin/getty 115200 tty1`
* Add new respawn line: `1:2345:respawn:/bin/login -f pi tty1 </dev/tty1 >/dev/tty1 2>&1`
* Save & Exit, Reboot. Pi should login to `pi@hostname ~$` prompt.

##License
See LICENSE for specific information. Script is released under GNU Public License v2.0
