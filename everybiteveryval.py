# -*- coding: utf8 -*-
from random import randint
import binascii as ba
import re
#Flips all bits in a jpeg/png

def writeByte(x, f):
    f.write((int(x)).to_bytes(1,byteorder = 'big'))
    #f.write(bytes([int(x)])) #both of these will work

def allBytes(count):
    while count < len(data):
        innerCount = 0
        while(innerCount < 256):
            index = 0#Must have this directory structure pics\test\Byte()()   
            with open ("pics\\test" + str(count)+ "\\" + "Byte(" + str(hex(count))+ ") (" + str(innerCount) + ")"+ str(ext), "wb") as f:
                for x in data:
                    if(index == count ):
                        x = innerCount
                    index += 1
                    writeByte(x, f)
                    innerCount += 1
        count += 1
        print('Count : ' , str(count))

##file = input("what is the file called? ")
##ext = input("what file extension has it? ")
file = "test"
ext = ".jpg"
with open(file+ext, "rb") as f:
    data = f.read()
count = 0
innerCount = 0
index = 0
print(len(data))
allBytes(count)
    

print("out")

