#!/usr/bin/env python3

import time
import urllib.request

fp = urllib.request.urlopen("http://localhost:1234/")

while i < 20:
    encodeContent = fp.read()
    decodedContent = encodeContent.decode("utf8")

    print(decodedContent)
    with open('data.txt', 'r') as f:
        f.writelines(decodedContent)
    time.sleep(15)


fp.close()