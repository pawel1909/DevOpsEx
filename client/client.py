#!/usr/bin/env python3

import urllib.request

fp = urllib.request.urlopen("http://localhost:1234/")

encodeContent = fp.read()
decodedContent = encodeContent.decode("utf8")

print(decodedContent)



fp.close()