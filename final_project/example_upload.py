#!/usr/bin/env python3
import requests

# This example shows how a file can be uploaded using
# The Python Requests module

url = "http://34.123.169.96/upload/"
with open('/usr/share/apache2/icons/icon.sheet.png', 'rb') as opened:
    r = requests.post(url, files={'file': opened})
