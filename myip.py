import sys
from netifaces import interfaces, ifaddresses, AF_INET
import netifaces
import logging
import time
import subprocess
import sched

# Configure logging & output file for log
logging.basicConfig(level=logging.INFO, 
                    filename='myip_log.txt', # log to this file
                    format='%(asctime)s %(message)s') # include timestamp

# Configure scheduler to run function below
s = sched.scheduler(time.time, time.sleep)

# IP Address Logging Function (function required to ensure it can be run in a schedule)
def log_ip_address(sc):
  print ("Logging IP Now...")
  for ifaceName in interfaces():
      addresses = [i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr':'No IP addr'}] )]
      logging.info('%s: %s' % (ifaceName, ', '.join(addresses)))
      sc.enter(1,60,log_ip_address,(sc,))
      time.sleep(40)

# Need to add escape clause. 
# Need to add log message when IP Address is lost.
# Print IP Lost to terminal while program is running + log file. 

s.enter(1,60,log_ip_address,(s,))
s.run()
