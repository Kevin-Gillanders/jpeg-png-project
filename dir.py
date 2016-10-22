import os
import errno
#Make a folder called all and fills it with
#1-N folders called test where N is the amount of bytes
#in a jpeg called test
count = 0
with open("test.jpg", "rb") as f:
    data = f.read()
try:
    while(count < len(data)):
        os.mkdir(".\\all\\test" + str(count))
        count += 1
except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise
