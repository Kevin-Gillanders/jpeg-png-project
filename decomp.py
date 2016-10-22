import numpy as np
import png
from random import randint

#This program can alter the actual colours of a png
#I scamble the colours in the middle of the image in this script

file = "Capture.png"
outFile = "decomp.png"
with open(file, "rb") as f:
    data = f.read()

meta = png.Reader(file).read()
meta = meta[-1]
print(meta)
col = png.Reader(file).asDirect()
colcount = 0
store = []
rowCount = 0
print('in')
for rgb in list(col[2]):
    #print(rgb , "\n\n")
    colcount = 0
    for pix in rgb:   
            if(pix >= 245):
                pix -= randint(10, 100)
            elif(pix <= 10):
                pix += randint(10, 100)
            else:
                pix -= 6000
            store.append(pix)
    rowCount += 1
print('out')
with open(outFile, 'wb')as f:
    image_2d = np.array(store).astype(np.uint8)
    if(meta['alpha'] == True):
        image_2d = np.reshape(image_2d, (col[1], col[0]*4))
    else:
        image_2d = np.reshape(image_2d, (col[1], col[0]*3))
    print(image_2d)
    w = png.Writer(width = col[0], height = col[1],bitdepth = meta['bitdepth'], alpha = meta['alpha'],
                   planes = meta['planes'], size = meta['size'], interlace = meta['interlace'])
    w.write(f,image_2d)

