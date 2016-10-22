# -*- coding: utf8 -*-
from random import randint
import binascii as ba
import re
#I wanted to experiment with jpegs and pngs
#So this it the first bit flipper I made, iterates through all bytes
#and flips it changes it to random value
def writeByte(x, f):
    #writes and converts byte to new picture
    f.write((int(x)).to_bytes(1,byteorder = 'big'))
    #f.write(bytes([int(x)])) #both of these will work

def allBytes(count):
    innerCount = 0
    index = 0 
    while( count < len(data)):#iterate compltely through all bytes in image
        with open ("all//"+ str(count) + "  " + str(hex(count))+ ".jpg", "wb") as f:
            index = 0   
            for x in data:#changes only new byte
                if(index == count ):
                    x = randint(0, 255)
                index += 1
                writeByte(x, f)
                innerCount += 1
        count += 1

##file = input("what is the file called? ")
##ext = input("what file extension has it? ")
file = "test"
ext = ".png"
with open(file+ext, "rb") as f:
    data = f.read()
count = 0
innerCount = 0
index = 0
print(len(data))
allBytes(count)
print("complete")
