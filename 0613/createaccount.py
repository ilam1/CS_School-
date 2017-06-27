#!/usr/bin/python
print 'content-type: text/html'
print ''

import cgitb,cgi,hashlib
cgitb.enable()

form = cgi.FieldStorage()

head = '''<html>
<head>
    <title>Create an Account</title>
	<style>
	    body {
		background-image: url("pictures/createacc.jpg");
		background-repeat: no-repeat;
		background-attachment: fixed;
		background-position: center right;
	    }
	</style>

</head>
<body>
   '''
body = ""
foot = '''
</body>
</html>
'''


if len(form)==0:
    body = '''<br><br><br><br><br><br><br>
    <h1 style="font-size:450%;"><center>Create account:</center></h1>
    <form action="createaccount.py">

    <p style="font-size:300%; text-align:center;">Username: <input style="font-size:80%;" type="text" name="username"><br>
    Password: <input style="font-size:80%;" type="password" name="password"><br>
    <br>
    <input style="font-size:80%;" type="submit" value=" Create Account "></p>
    '''
else:
    if 'username' in form and 'password' in form:
        users = open('data/users.txt','r').read().split('\n')
        users = [each.split(',') for each in users]
        users.remove( [""])
        username = form.getvalue('username')
        password = form.getvalue('password')
        #nice python features that I do not teach...
        if not username in [a[0] for a in users] and len(username)>2:
            f = open('data/users.txt','a')
            f.write(username+","+hashlib.sha256(password).hexdigest()+','+'Factionless\n')
            f.close()
            body += 'Successfully added. <a href="login.py"> Click here to log in</a>.<br>'
	elif len(username)<3:
	    body+= 'Username is too short!'
        else:
            body += 'Username already taken!'
    else:
        body += "Please use the form!"

print head
print body
print foot
