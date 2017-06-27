#!/usr/bin/python
print "content-type: text/html\n"

import cgitb,hashlib,cgi
cgitb.enable()
import Cookie,os

form=cgi.FieldStorage()

head = '''<!DOCTYPE html>
<html>
 <head>
  <title>Profile</title>
 <style>
  body {
    background-image: url("pictures/snow.png");
    background-repeat: no-repeat;
    background-attachment: fixed;
    background-position: center;
    background-size:cover;
  }
p.test {
    word-wrap: break-word;
    }
 </style>

 </style>
 </head>
<body>
'''

body = '<h1 align="center"> Profile </h1>'
foot = '''</body>
</html>
'''
def authenticate(u,ID,IP):
    loggedIn = open('data/loggedin.txt','r').read().split('\n')
    loggedIn = [each.split(',') for each in loggedIn]
    loggedIn.remove([''])
    for a in loggedIn:
        if a[0] == u:
            return a[1]==str(ID) and a[2]==IP
    return False

def getfac(u):
    users = open('data/users.txt','r').read().split('\n')
    users = [each.split(',') for each in users]
    users.remove([''])
    for a in users:
        if a[0] == u:
            return a[2].strip()

def prof(u,fac):
    ans="<h2>User: "+u+"</h2>"
    ans+="<h2>Faction: <i>"+fac+"</i><h2>"
    return ans

def form0(u):
    ans='<form method = "GET" action = "profile.py?username='+u+'">'
    ans+='''<h2>Update Description: </h2><textarea rows="5" name="d" cols="50"></textarea>'''
    ans += '<input type="hidden" name="username" value="'+u+'">'
    ans+='''<br><input type="submit" name="sub" value="Save Changes">'''
    return ans

def breakup(text):
    L=text.strip().split('\n')
    i=0
    for every in L:
        L[i]=every.split('@')
        i+=1
    return L

def together(L):
    i=0
    for every in L:
        L[i]='@'.join(every)
        i+=1
    return '\n'.join(L)

def update(u):
    d=form.getvalue('d')
    d=d.replace('<', '&lt')
    d=d.replace('>', '&gt')
    f = open('data/description.txt', 'r')
    text=f.read()
    f.close()
    if not(text==""):
        text=breakup(text)
        user=[]
        for thing in text:
            user.append(thing[0])
        if u in user:
            text.pop(user.index(u))
        text.append([u,d])
    else:
        text=[[u,d]]
    f = open('data/description.txt', 'w')
    f.write(together(text))
    f.close()

def show(u):
    a=''
    b='<h2>Description:</h2><p class="test">'
    f = open('data/description.txt', 'r')
    text=f.read()
    f.close()
    text=breakup(text)
    for every in text:
        if every[0]==u:
            a += every[1]
    if a =='':
        a+="Currently Empty"
    b+=a+'</p>'
    return b

if 'HTTP_COOKIE' in os.environ:
    cookie_string=os.environ.get('HTTP_COOKIE')
    c = Cookie.SimpleCookie()
    c.load(cookie_string)
    if 'username' in c and 'ID' in c:
        username = c['username'].value
        ID = c['ID'].value
        IP = os.environ['REMOTE_ADDR']
        name=form.getvalue('name')
        body += 'Back to the <a href="stuymap.py?username='+username+'">mainpage!</a>'
        if 'name' in form:
            faction=getfac(name)
            body+=prof(name,faction)
            if name == username:
                if 'd' in form: 
                    update(username)
            body+=show(username)
            if name == username:
                body+=form0(username)
        else:
            faction=getfac(username)
            body+=prof(username,faction)
            if 'd' in form: 
                update(username)
            body+='<p class="test">'+show(username)+'</p>'+form0(username)
    else:
        body+= "Your information expired<br>\n"
        body+= 'Go Login <a href="login.py">here</a><br>'
else:
    body+= 'You seem new<br>\n'
    body+='Go Login <a href="login.py">here</a><br>'
    body+='Or create an account <a href="createaccount.py">here</a>'

print head
print body
print foot
