import re
import io
import sys
import time
from functools import partial
from contextlib import contextmanager




def text_match(text):
    pattern = "authentication failure"
    if re.search(pattern, text):
        #put into an array or list
        list.append(re.match(pattern))
    else:
        return 'no match in this 1024 block' 
def ip_match(text):
    pattern = ""

with open(sys.argv[1], 'rb') as f:
    fbuf=io.BufferedReader(f)
    for chunk in iter(partial(f.read, 100), b''):
        if fbuf == '':
            break
        print(text_match (fbuf.read(1024).decode())) 
        



regex_login = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
#regex_time = re.compile 




#find match and populate into array
#draw from array and print that statement 
#look at globalprotect fields and determine which are non-conforming and which ips are actually login logout, wtf does it say???
# output all info to a file 