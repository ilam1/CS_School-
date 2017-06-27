#!/usr/bin/python
print 'content-type: text/html'
print ''
import cgitb
cgitb.enable()
import cgi
form = cgi.FieldStorage()

import hashlib

f = open("data/users.txt", "r")
text = f.read()
f.close()

print """<html>
 <head>
  <title>Lab 15 Create Account</title>
 </head>
<body>
 <h1> Create an account! </h1>
 <form method="GET" action="createaccount.py">
  Username: <input type="text" name="username"> <br>
  Password: <input type="password" name="password"> <br><br>
  <input type="submit" name="submit" value="create account">
"""
#print "username" in form
#print "password" in form  
if "username" in form and "password" in form and form.getvalue("username") in text:
    print "<br><br>Please choose a more unique username"
if "username" not in form and "password" not in form:
    print "<br><br>Something is better than nothing..."
if "username" in form and "password" not in form:
    print "<br><br>Password?"
if "username" not in form and "password" in form:
    print "<br><br>Username?"

if "username" in form and "password" in form and form.getvalue("username") not in text:
    error = False
    for each in form.getvalue("username")+form.getvalue("password"):
        if each in '''!@#$%^&*()_+`-={}|[]\:"<>'?,./;''':
            if error == False:
                print "<br><br> :P No special characters!! >,<"
            error = True
    if error == False:
        f = open("data/users.txt", 'a')
        f.write(form.getvalue("username"))
        f.write(",")
        f.write(hashlib.sha256(form.getvalue("password")).hexdigest())
        f.write("\n")
        f.close()
