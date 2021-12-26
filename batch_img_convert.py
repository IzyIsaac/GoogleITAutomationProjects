#!/usr/bin/env python3
import os
import sys
import imghdr
from PIL import Image

indir = sys.argv[1]
outdir = '/opt/icons'
for infile in os.listdir(indir):
    name, ext = os.path.splitext(infile)
    if imghdr.what(os.path.join(indir,infile)) == 'tiff':
        with Image.open(os.path.join(indir,infile)) as image:
            flipped = image.transpose(Image.ROTATE_90)
            resized = flipped.resize((128,128))
            resized.convert('RGB').save(os.path.join(outdir, name + '.jpeg'))
