#!/usr/bin/python
print "content-type: text/html\n"

import cgitb
cgitb.enable()
import cgi
form = cgi.FieldStorage()

import os
ip = os.environ["REMOTE_ADDR"]

f = open("data/loggedin.txt","r")
log = f.read().split("\n")
log.remove('')
f.close()
#print log

#print form.getvalue("user")
#print form.getvalue("id")
#print str(username) + "," + ID + "," + str(ip) in log
def userinlog(username, ID): 
    if str(username) + "," + ID + "," + str(ip) in log:
        return "You are successfully logged in!"
    else:
        return "<a href='login.py'>Go log in </a>"

print userinlog(form.getvalue("user"), form.getvalue("id"))

