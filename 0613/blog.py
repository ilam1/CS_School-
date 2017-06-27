#!/usr/bin/python
print 'content-type: text/html\n'

import Cookie,os

import cgitb,hashlib,cgi
cgitb.enable()

form=cgi.FieldStorage()

f = open('data/users.txt', 'r')
text = f.read().split('\n')
f.close()

body = ""

post="""<form method = 'GET' action = 'blog.py'>
                Update:
                <br>
                <textarea rows="3" name="post" cols="25">
Tell us about your day!
                </textarea>
                <br>
                <input type="submit" name="done" value="Post!">
"""

comment1="""<form method = 'GET' action = 'blog.py'>
                <br>
                <textarea rows="3" name="comment"""
comment2="""" cols="25"></textarea>
                <input type="submit" name="go"""
comment3="""" value="Post!">"""


boxo='''<p class="double">'''
boxc="</p>"


def lt(text):
    return text.strip().split('\n\n')

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

def blog(faction,text,comments,user):
    title=faction[0].upper()+faction[1:]
    body = '''<h1 align="center">'''+title+'''</h1>'''
    body += post
    if not(text==''):
        for x in lt(text):
            new=x.strip('\n')
            nu=new[0]
            body += "<br><br>"+boxo+new+'<br><b>Comments:</b>'
            for y in lt(comments):
                y=y.strip('\n')
                if not (y==""):
                    if y[0] == nu:
                       body+='<br><table border="1" width="1250"><tr><td>'+y[1:]+'</td></tr></table>'
            body+=comment1+nu+comment2+nu+comment3+boxc
    return body

def get_comment(faction):
        fa=faction[:2]
        f = open('data/'+fa+'.txt', 'r')
        text=f.read()
        f.close()
        return text

def get_text(faction):
        f = open('data/'+faction+'.txt', 'r')
        text = f.read()
        f.close()
        return text
def findnum(faction,text):
         if not(text==''):
            num=int(lt(text)[-1][0])
            return num

def update(faction,user,num):
    if 'done' in form:
        status = form.getvalue('post')
        status = status.replace('<', '&lt')
        status = status.replace('>', '&gt')
        if not(status is None):
        	if text=='':
           		f = open('data/'+faction+'.txt', 'a')
           		f.write('0. <b>'+'<a href="profile.py?name='+user+'">'+user+"</a>"+':</b><br>'+status+"\n\n")
           		f.close()
        	else:
           		f = open('data/'+faction+'.txt', 'a')
           		f.write(str(num+1)+'. <b>'+'<a href="profile.py?name='+user+'">'+user+"</a>"+':</b><br>'+status+"\n\n")
           		f.close()

def comms(user, faction,num):
    i=0
    fac=faction[:2]
    f = open('data/'+fac+'.txt', 'a')
    while i <= num:
        if 'go'+str(i) in form:
           commt=form.getvalue('comment'+str(i))
           commt=commt.replace('<', '&lt')
           commt=commt.replace('>', '&gt')
           if not(commt is None):
             f.write(str(i)+'<b>'+'''<a href="profile.py?name='''+user+'">'+user+"</a>"+':</b><br>'+commt+"\n\n")
        i+=1
    f.close()

if 'HTTP_COOKIE' in os.environ:
    cookie_string=os.environ.get('HTTP_COOKIE')
    c = Cookie.SimpleCookie()
    c.load(cookie_string)
    if 'username' in c and 'ID' in c:
        username = c['username'].value
        ID = c['ID'].value
        IP = os.environ['REMOTE_ADDR']
        faction=getfac(username).lower()
        text=get_text(faction).strip()
        comments=get_comment(faction).strip()
        num=findnum(faction,text)
        comms(username,faction,num)
        update(faction,username,num)
        text=get_text(faction).strip()
        comments=get_comment(faction).strip()
        body = blog(faction,text,comments,username)
        body += '<br><br>Back to the <a href="stuymap.py?username='+username+'">mainpage!</a>'
    else:
        body+= "Your information expired<br>\n"
        body+= 'Go Login <a href="login.py">here</a><br>'
else:
    body+= 'You seem new<br>\n'
    body+='Go Login <a href="login.py">here</a><br>'
    body+='Or create an account <a href="createaccount.py">here</a>'

head = '''<head>
<title> Blog</title>
 <style>
 body {
   background-image: url("pictures/blog1.jpg");
   background-repeat: no-repeat;
   background-attachment: fixed;
   background-position: center;
   background-size:cover;
 }
 p.double {border-style: double;
 border-width: 5px;}
 p.dotted {border-style: dotted;}

 </style>
 </head>
 <body>'''
head2 = '''<html>
<style>
p.double {border-style: double;
border-width: 5px;}
p.dotted {border-style: dotted;}
 body {
   background-color: #000000
   background-image: url("pictures/blog.jpg");
   background-repeat: no-repeat;
   background-attachment: fixed;
   background-position: center;
}
</style>
<head><title>Blog</title>
</head>

<body>
Back to the <a href="stuymap.py?username='+username+'">mainpage!</a>'''
foot = '''</body>
</html>'''

print head
print body
print foot
