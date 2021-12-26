#! /usr/bin/env python3
import os
import requests
import json

# Didn't download this data from the lab unfortunately...
feedbackdir = '/data/feedback'

for filename in os.listdir(feedbackdir):
    with open(os.path.join(feedbackdir, filename)) as feedback:
        feedbackdict = {}
        # Read title
        feedbackdict['title'] = feedback.readline().strip()
        # Read name
        feedbackdict['name'] = feedback.readline().strip()
        # Read date
        feedbackdict['date'] = feedback.readline().strip()
        # Read feedback
        feedbackdict['feedback'] = feedback.readline().strip()

        res = requests.post('http://34.72.1.161/feedback/', data = feedbackdict)
        print(res.status_code)
        print(res.reason)
