#!/usr/bin/python
print "content-type: text/html\n"

import cgitb,hashlib,cgi
cgitb.enable()
import Cookie,os

form=cgi.FieldStorage()
username = form.getvalue("username")

f = open("data/loggedin.txt","r")
text=f.read().split("\n")
f.close()

ans = ""
for each in text:
    if username != each.split(",")[0]:
        ans += each
g = open("data/loggedin.txt","w")
g.write(ans)
g.close()

print "You have successfully logged out."
print '''<meta http-equiv="refresh" content="1; url=stuymap.py">'''
