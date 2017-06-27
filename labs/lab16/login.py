#!/usr/bin/python
print 'content-type: text/html\n'
print ''
import cgitb
cgitb.enable()

import cgi
form = cgi.FieldStorage()
##
##with open('data/loggedin.txt', 'w') as file_:
##    raise SystemExit(0)

import hashlib
import random
import os

ip = os.environ["REMOTE_ADDR"]

f= open("data/users.txt", "r")
userText = f.read()
userText = userText.split("\n")
f.close()

g=open("data/loggedin.txt","r")
log = g.read()
g.close()


print """<html>
 <head>
  <title>Lab 16 Login</title>
 </head>
<body>
 <h1> Login! </h1>
 <form method="GET" action="login.py">
  Username: <input type="text" name="username"> <br>
  Password: <input type="password" name="password"> <br><br>
  <input type="submit" name="submit" value="Login">
"""

#login = form.getvalue("username")+","+ hashlib.sha256(form.getvalue("password")).hexdigest()
#print form
if "submit" in form:
    if "username" in form and "password" not in form:
        print "<br><br> Password?"
    if "username" not in form and "password" in form:
        print "<br><br> Username?"
    if "username" not in form and "password" not in form and form!= []:
        print "<br><br> ..."

def getLine(x,string):
    return string[string.index(x):string.index("\n", string.index(x)) + 1]

#randomnum=random.randint(1000000000,9999999999)
if "username" in form and "password" in form:
    randomnum=random.randint(1000000000,9999999999)
    if form.getvalue("username")+","+ hashlib.sha256(form.getvalue("password")).hexdigest() in userText:
        if form.getvalue("username") + "," in log:
#            print "triggered"
            newString = form.getvalue("username") + ',' + str(randomnum) + "," + str(ip) + "\n"
            newdata = log.replace(getLine(form.getvalue("username") + ",", log), newString, 1) 
            f = open("data/loggedin.txt", "w")
            f.write(newdata)
            f.close()
        else:
            h = open("data/loggedin.txt","a")
            h.write(form.getvalue("username") + "," + str(randomnum) + "," + str(ip)+"\n")
            h.close()
        print "<br><br>"
        print '<a href="mainpage.py?user=' + form.getvalue('username') + '&id=' + str(randomnum) + '">Success!</a>'
    else:
        print "<br><br>Login Failed!"
