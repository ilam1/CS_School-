#!/usr/bin/python
print 'content-type: text/html\n'

import cgitb
cgitb.enable()

f = open("data/loggedin.txt", 'w')
f.close()
