#!/usr/bin/python
print 'content-type: text/html\n'
print ''
import cgitb
cgitb.enable()
import cgi
form = cgi.FieldStorage()

import hashlib
import random
import os
ip = os.environ["REMOTE_ADDR"]

f= open("data/users.txt", "r")
text = f.read()
ans = text.split("\n")
f.close()

g=open("data/loggedin.txt","r")
log = g.read()
g.close()


print """<html>
 <head>
  <title>Lab 15 Login</title>
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
if "username" in form and "password" not in form:
    print "<br><br> Password?"
if "username" not in form and "password" in form:
    print "<br><br> Username?"
if "username" not in form and "password" not in form and form!= []:
    print "<br><br> ..."

def line(x,str):
    str=str[str.index(x):]
    if "\n" in str:
        return str[:str.index(x)]
    else:
        return str


#randomnum=random.randint(1000000000,9999999999)
if "username" in form and "password" in form:
    randomnum=random.randint(1000000000,9999999999)
    if form.getvalue("username")+","+ hashlib.sha256(form.getvalue("password")).hexdigest() in ans:
        if form.getvalue("username") + "," in log:
#            print "triggered"
            newdata = log.replace(line((form.getvalue("username") + ","),log),form.getvalue("username") + "," + str(randomnum) + "," + str(ip)+"\n") #ERROR
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


