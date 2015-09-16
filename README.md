# My-IP
Basic python script to grab IP Address of connected ethernet adaptors and log to a file. This will report all loaded ethernet adaptors, future version to allow selection of ethernet adaptor at runtime, but currently not required.

Uses netifaces python package to read status of the ethernet adaptors.

##To Do
* Need to add escape clause eg. except KeyboardInterrupted
* Need to add a log message specific for when an IP Address is actually lost, rather than no-ip to report.
* Print to cli that IP Address has been lost to alert users that may be watching.
