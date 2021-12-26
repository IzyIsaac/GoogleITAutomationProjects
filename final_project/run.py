#! /usr/bin/env python3

import os
import requests

url = 'http://34.123.169.96/fruits'
descriptions_dir = 'supplier-data/descriptions'
for filename in os.listdir(descriptions_dir):
    with open(os.path.join(descriptions_dir, filename)) as description:
        descriptions = {}
        # Read title
        descriptions['name'] = description.readline().strip()
        # Read name
        descriptions['weight'] = int(description.readline().split(' ')[0])
        # Read date
        descriptions['description'] = description.readline().strip()
        # Read feedback
        descriptions['image_name'] = filename.split('.')[0] + '.jpeg'

        res = requests.post(url, data = descriptions)
        print(res.status_code)
        print(res.reason)