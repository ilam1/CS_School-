#!/usr/bin/python
print 'content-type: text/html\n'

import cgitb
cgitb.enable()

f = open("data/users.txt", 'w')
f.close()
