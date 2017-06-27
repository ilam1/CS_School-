#!/usr/bin/python
print 'content-type: text/html\n'
print ''
import cgitb
cgitb.enable()
import cgi
form = cgi.FieldStorage()

import hashlib

f= open("data/users.txt", "r")
text = f.read()
ans = text.split("\n")
f.close()


print """<html>
 <head>
  <title>Lab 15 Login</title>
 </head>
<body>
 <h1> Login! </h1>
 <form method="GET" action="login.py">
  Username: <input type="text" name="username"> <br>
  Password: <input type="password" name="password"> <br><br>
  <input type="submit" name="submit" value="Login!">
"""

#login = form.getvalue("username")+","+ hashlib.sha256(form.getvalue("password")).hexdigest()
#print form
if "submit" in form:
    if "username" in form and "password" not in form:
        print "<br><br> Password?"
    if "username" not in form and "password" in form:
        print "<br><br> Username?"
    if "username" not in form and "password" not in form:
        print "<br><br> ..."

    if "username" in form and "password" in form:
        if form.getvalue("username")+","+ hashlib.sha256(form.getvalue("password")).hexdigest() in ans:
            print "<br><br>Success!"
        else:
            print "<br><br>Login Failed!" 

