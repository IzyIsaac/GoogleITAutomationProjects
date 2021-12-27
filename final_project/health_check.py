#!/usr/bin/env python3

import sys
import os
from enum import Enum 
import psutil
import socket
import emails

class Alert(Enum):
    CPU = 'Error - CPU usage is over 80%'
    DISK = 'Error - Available disk space is less than 20%'
    MEMORY = 'Error - Available memory is less than 500MB'
    HOST = 'Error - localhost cannot be resolved to 127.0.0.1'



def main(argv):
    sender = 'automation@example.com'
    recipient = 'student-00-405db269f197@example.com'
    body = 'Please check your system and resolve the issue as soon as possible'
    cpu_percent = psutil.cpu_percent()
    memory_available = psutil.virtual_memory().available
    disk_usage = psutil.disk_usage('/').percent
    localhost = socket.gethostbyname('localhost')
    if cpu_percent > 80:
        emails.send(emails.generate(sender, recipient, Alert.CPU, body))
    if memory_available < 524288000:
        emails.send(emails.generate(sender, recipient, Alert.MEMORY, body))
    if disk_usage > 80:
        emails.send(emails.generate(sender, recipient, Alert.DISK, body))
    if localhost != '127.0.0.1':
        emails.send(emails.generate(sender, recipient, Alert.HOST, body))

if __name__ == "__main__":
    main(sys.argv)