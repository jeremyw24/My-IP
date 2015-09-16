import sys
from netifaces import interfaces, ifaddresses, AF_INET
import netifaces
import logging
import time
import subprocess
import sched

logging.basicConfig(level=logging.INFO, 
                    filename='myip_log.txt', # log to this file
                    format='%(asctime)s %(message)s') # include timestamp

s = sched.scheduler(time.time, time.sleep)

def log_ip_address(sc):
  print ("Logging IP Now...")
  for ifaceName in interfaces():
      addresses = [i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr':'No IP addr'}] )]
      #print '%s: %s' % (ifaceName, ', '.join(addresses))
      logging.info('%s: %s' % (ifaceName, ', '.join(addresses)))
      sc.enter(60,1,log_ip_address,(sc,))

s.enter(1,60,log_ip_address,(s,))
s.run()



#while True:
  #log_ip_address()
