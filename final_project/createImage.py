#!/usr/bin/env python3

from PIL import Image
import os
import imghdr
directory = 'supplier-data/images'
for infile in os.listdir(directory):
    name, ext = os.path.splitext(infile)
    if imghdr.what(os.path.join(directory, infile)) == 'tiff':
        with Image.open(os.path.join(directory, infile)) as image:
            resized = image.resize((600,400))
            resized.convert('RGB').save(os.path.join(directory, name + '.jpeg'))




