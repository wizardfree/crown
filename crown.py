#!/usr/bin/env python3

from PIL import Image
import argparse
import os
from pathlib import Path

parser = argparse.ArgumentParser(description='Description of your program')
parser.add_argument('-i','--image', help='The file to have the watermark applied to', required=True)
parser.add_argument('-o','--output', help='Where to place the new file', required=True)
args = vars(parser.parse_args())

workingFile = Path(args['image'])
outputDir = Path(args['output'])
filename = os.path.split(Path(args['image']))[1]
filename = os.path.splitext(filename)[0] +'_watermark.png'

if not os.path.isdir(outputDir):
    print(str(outputDir) + ": Must be a valid dir!")
    exit(1)

if workingFile.is_file():
    img = Image.open(workingFile).convert('RGBA')
    width, height = img.size
    watermark = Image.open('thewholegang.png').convert('RGBA')
    alpha = Image.new("L", watermark.size, 50)
    size = ((width / 8), (height / 8))
    watermark.thumbnail(size, Image.ANTIALIAS)
    thumbwidth, thumbheight = watermark.size
    position = (thumbwidth, (height - (thumbheight * 2)))

    img.paste(watermark, position, watermark)
    img.save(str(outputDir) + '/' + filename, quality=95)
    print("Saving watermarked file to: {}".format(str(outputDir)))
else:
    print('Not a valid file.')
    
