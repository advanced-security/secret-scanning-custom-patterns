#!/usr/bin/env python3

from base64 import urlsafe_b64encode as b64encode
import re

for c in range(0, 255):
    for d in range(0, 255):
        for l in range(0, 2):
            token = (
                b64encode(('{"' + chr(c) + chr(d) + ('.' * (l + 2)) + chr(c) + chr(d) + '}').encode('utf-8')).decode('utf-8') + '.' +
                b64encode(('{"' + chr(c) + chr(d) + ('.' * (l + 2)) + chr(c) + chr(d) + '}').encode('utf-8')).decode('utf-8') + '.' +
                b64encode(('{"' + chr(c) + chr(d) + ('.' * (l + 2)) + chr(c) + chr(d) + '}').encode('utf-8')).decode('utf-8')
            )

            print(token)
            if '=' in token:
                print(re.sub('=', '', token))

