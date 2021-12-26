import os
import requests
import imghdr

url = 'http://34.123.169.96/upload/'
image_dir = 'supplier-data/images'

for filename in os.listdir(image_dir):
    if imghdr.what(os.path.join(image_dir, filename)) == 'tiff': continue
    with open(os.path.join(image_dir, filename)) as opened:
        r = requests.post(url, files={'file': opened})