#!/usr/bin/python
print "content-type: text/html\n"

import cgitb,hashlib,cgi
cgitb.enable()
import Cookie,os

form=cgi.FieldStorage()

head = '''<!DOCTYPE html>
<html>
 <head>
  <title>Aptitude Test</title>
 <style>
 body {
   background-color: #D08BE5;
 </style>
 </head>
<body>
'''

body = "<h1> Aptitude Test </h1>"
foot = '''</body>
</html>
'''

def getfac(u):
    users = open('data/users.txt','r').read().split('\n')
    users = [each.split(',') for each in users]
    users.remove([''])
    for a in users:
        if a[0] == u:
            return a[2].strip()

def points():
        abnegation = 0
        amity = 0
        candor = 0
        dauntless = 0
        erudite = 0
        if form.getvalue("question1") == "1a":
                amity += 1
        elif form.getvalue("question1") == "1b":
                erudite += 1
        elif form.getvalue("question1") == "1c":
                abnegation += 1
        elif form.getvalue("question1") == "1d":
                dauntless += 1
        else:
                candor += 1
        if form.getvalue("question2") == "2a":
                dauntless += 1
        elif form.getvalue("question2") == "2b":
                candor += 1
        elif form.getvalue("question2") == "2c":
                erudite += 1
        elif form.getvalue("question2") == "2d":
                amity += 1
        else:
                abnegation += 1
        if form.getvalue("question3") == "3a":
                amity += 1
        elif form.getvalue("question3") == "3b":
                dauntless += 1
        elif form.getvalue("question3") == "3c":
                erudite += 1
        elif form.getvalue("question3") == "3d":
                abnegation += 1
        else:
                candor += 1
        return [abnegation,amity,candor,dauntless,erudite]


def factionresult(L): #takes points() as its parameter
        faction = []
        maxi = max(L[0], L[1], L[2], L[3], L[4])
        if L[0] == maxi:
                faction.append("Abnegation")
        if L[1] == maxi:
                faction.append("Amity")
        if L[2] == maxi:
                faction.append("Candor")
        if L[3] == maxi:
                faction.append("Dauntless")
        if L[4] == maxi:
                faction.append("Erudite")
        return faction

def replacetext(username,faction): #adds the faction to the end of the string that has username in it (for appending faction result to users.txt)
        faction=faction[0]
        users = open('data/users.txt','r').read().split('\n')
        users = [each.split(',') for each in users]
        users.remove([''])
        i=0
        while i < len(users):
            if users[i][0]==username:
                users[i][2]=faction
            i+=1
        i=0
        while i < len(users):
            users[i]=','.join(users[i])
            i+=1
        return "\n".join(users)+"\n"


def realfacresult(faction, username): #takes factionresult(points()) as its parameter <list
        b=""
        if len(faction) == 1:
                text=replacetext(username,faction)
                g = open("data/users.txt","w")
                g.write(text)
                g.close()
                b+="<br>You got "+ faction[0] +"!"
                b+= '<br><p>Go Check Out Your New Features <a href="mainpage.py">Here</a>!</p>'
        if len(faction) > 1: ###UNFINISHED
                b += "<br><br>You're divergent. You must select a faction to fit in: <br><select name='divergent' size='1'>"
                for each in faction:
                        b += "  <option>" + str(each) + "</option>"
                b += '''</select><input type="submit" name="sub" value="Choose">'''
        return b


def authenticate(u,ID,IP):
    loggedIn = open('data/loggedin.txt','r').read().split('\n')
    loggedIn = [each.split(',') for each in loggedIn]
    loggedIn.remove([''])
    for a in loggedIn:
        if a[0] == u:
            return a[1]==str(ID) and a[2]==IP
    return False

test1 = [["1. I agree most strongly with the following proverb:", "Ignorance is bliss", "Knowledge is power", "A house divided against itself cannot stand", "A taste of your own medicine" , "All that glitters is not gold"],["2. Choose one of the following:", "YOLO","TBH","BTW","LOL","WBU"],["3. If I am going to be stranded on a deserted island, I would bring:" ,"food", "weapon", "computer","first-aid kit","friend"]]
def test():####ERROR
        y = 0
        ans = "<form method = 'GET' action = 'test1.py'>" ##form.getvalue("username") is None
        for each in test1:
            y += 1
            ans += each[0] + "<br>" + each[1] + "<input type='radio' name='question"  + str(y) + "' value='" + str(y) + "a' checked >"
            ans += "<br>" + each[2] + "<input type='radio' name='question" + str(y) + "' value='" + str(y) + "b' >"
            ans += "<br>" + each[3] + "<input type='radio' name='question" + str(y) + "' value='" + str(y) + "c' >"
            ans += "<br>" + each[4] + "<input type='radio' name='question" + str(y) + "' value='" + str(y) + "d' >"
            ans += "<br>" + each[5] + "<input type='radio' name='question" + str(y) + "' value='" + str(y) + "e' >"
            ans += "<br> <br>"
#        ans += '''<input type="hidden" name="username" value="''' + form.getvalue('username') + '''">'''
        ans +=  '''<input type="submit" name="submit" value="I'm done!">'''
        return ans

if 'HTTP_COOKIE' in os.environ:
    cookie_string=os.environ.get('HTTP_COOKIE')
    c = Cookie.SimpleCookie()
    c.load(cookie_string)
    ##print all the data in the cookie
    #body+= "<h1>cookie data</h1>"
    #for each in c:
    #    body += each+":"+str(c[each].value)+"<br>"
    if 'username' in c and 'ID' in c:
        username = c['username'].value
        ID = c['ID'].value
        IP = os.environ['REMOTE_ADDR']

        ##print all the users logged in
        #body += "<h1>userstuff</h1>"
        #body += str(loggedIn)
        #body += "<br>"
        if authenticate(username,ID,IP):
            body += test()
            if "submit" in form:
                body+=realfacresult(factionresult(points()),username)
            if "sub" in form:
                if "divergent" in form:
                    body+=realfacresult([form.getvalue("divergent")],username)
        else:
            body+="Failed to Authenticate cookie<br>\n"
            body+= 'Go Login <a href="login.py">here</a><br>'
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
