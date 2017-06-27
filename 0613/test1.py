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
   background-image: url("pictures/test03.jpg");
   background-repeat: no-repeat;
   background-attachment: fixed;
   background-position: center;
   background-size:cover;
 </style>
 </head>
<body>
'''

body = "<h1> Aptitude test </h1>"
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
        if form.getvalue("question4") == "4a":
                candor += 1
        elif form.getvalue("question4") == "4b":
                dauntless += 1
        elif form.getvalue("question4") == "4c":
                erudite += 1
        elif form.getvalue("question4") == "4d":
                amity += 1
        else:
                abnegation += 1
        if form.getvalue("question5") == "5a":
                erudite += 1
        elif form.getvalue("question5") == "5b":
                dauntless += 1
        elif form.getvalue("question5") == "5c":
                candor += 1
        elif form.getvalue("question5") == "5d":
                amity += 1
        else:
                abnegation += 1
        if form.getvalue("question6") == "6a":
                abnegation += 1
        elif form.getvalue("question6") == "6b":
                erudite += 1
        elif form.getvalue("question6") == "6c":
                dauntless += 1
        elif form.getvalue("question6") == "6d":
                amity += 1
        else:
                candor += 1
        if form.getvalue("question7") == "7a":
                abnegation += 1
        elif form.getvalue("question7") == "7b":
                amity += 1
        elif form.getvalue("question7") == "7c":
                erudite += 1
        elif form.getvalue("question7") == "7d":
                dauntless += 1
        else:
                candor += 1
        if form.getvalue("question8") == "8a":
                amity += 1
        elif form.getvalue("question8") == "8b":
                dauntless += 1
        elif form.getvalue("question8") == "8c":
                candor += 1
        elif form.getvalue("question8") == "8d":
                erudite += 1
        else:
                abnegation += 1
        if form.getvalue("question9") == "9a":
                abnegation += 1
        elif form.getvalue("question9") == "9b":
                candor += 1
        elif form.getvalue("question9") == "9c":
                amity += 1
        elif form.getvalue("question9") == "9d":
                dauntless += 1
        else:
                erudite += 1
        if form.getvalue("question10") == "10a":
                erudite += 1
        elif form.getvalue("question10") == "10b":
                abnegation += 1
        elif form.getvalue("question10") == "10c":
                dauntless += 1
        elif form.getvalue("question10") == "10d":
                amity += 1
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
            if users[i][0] == username:#changed from users[i][0]:
                users[i][2]=faction
            i+=1
        i=0
        while i < len(users):
            users[i]=','.join(users[i])
            i+=1
        return "\n".join(users)+"\n"

Diver = False
def realfacresult(faction, username): #takes factionresult(points()) as its parameter <list
#	Diver = False
        b=""
        if len(faction) == 1:
		text=replacetext(username,faction)
#orig                text=replacetext(username,factionresult(points()))
                g = open("data/users.txt","w")
                g.write(text)
                g.close()
		b += "<br>You got "+ faction[0] +"!" #added
		b += '<br><p><a href="stuymap.py?username='+username+'">Go Check Out Your New Features Here! </a> </p>'
        if len(faction) > 1: ###UNFINISHED
                b += "<br>You're divergent. You must select a faction to fit in: <br><select name='divergent' size='1'>"
		Diver = True
                for each in faction:
                        b += "  <option>" + str(each) + "</option>" #from  str(faction.pop(0))
		b+='</select><input type="submit" name="sub" value="Choose">'
#orig                b += "</select>"
#orig                if "divergent" in form:
#orig                        text=replacetext(username,form.getvalue("divergent"))
#orig                        g = open("data/users.txt","w")
#orig                        g.write(text)
#orig                        g.close()
        return b


#def authenticate(u,ID,IP):
#    loggedIn = open('data/loggedin.txt','r').read().split('\n')
#    loggedIn = [each.split(',') for each in loggedIn]
#    loggedIn.remove([''])
#    for a in loggedIn:
#        if a[0] == u:
#            return a[1]==str(ID) and a[2]==IP
#    return False

test1 = [["1. I agree most strongly with the following proverb:", "Ignorance is bliss", "Knowledge is power", "A house divided against itself cannot stand", "A taste of your own medicine" , "All that glitters is not gold"],["2. Choose one of the following:", "YOLO","TBH","BTW","LOL","WBU"],["3. If I am going to be stranded on a deserted island, I would bring:" ,"food", "weapon", "computer","first-aid kit","friend"],["4. The thing that aggravates me above all else is","Human nature","Cowardice","Stupidity","Anger","Greed"],["5. If I could have any power, I would desire","Clairvoyance","Telekinesis","Mind-reading","Negation of powers","Nothing, being human is satisfying in itself"],["6. I relate most strongly with","Earth","Water","Fire","Wind","Metal"],["7. The scent that appeals to me most is that of","A freshly baked meal","A crackling fire","Old books","The beach","Home"],["8. The mythological creature of my dreams is", "Unicorn","Dragon","Centaur","Sphinx","Elf"],["9. The most captivating celestial body is the","Sun","Moon","Star","Planet","Space"],["10. The number calling for me right now is", "1","2","3","4","5"]]
def test():
        y = 0
        ans = "<form method = 'GET' action = 'test1.py'>" 
        for each in test1:
            y += 1
            ans += each[0] + "<br>" + each[1] + "<input type='radio' name='question"  + str(y) + "' value='" + str(y) + "a' checked >"
            ans += "<br>" + each[2] + "<input type='radio' name='question" + str(y) + "' value='" + str(y) + "b' >"
            ans += "<br>" + each[3] + "<input type='radio' name='question" + str(y) + "' value='" + str(y) + "c' >"
            ans += "<br>" + each[4] + "<input type='radio' name='question" + str(y) + "' value='" + str(y) + "d' >"
            ans += "<br>" + each[5] + "<input type='radio' name='question" + str(y) + "' value='" + str(y) + "e' >"
            ans += "<br> <br>"
#            ans += each[0] + "<br>" + "<input type='radio' name='question"  + str(y) + "' value='" + str(y) + "a' checked >" + each[1]
#            ans += "<br>" + "<input type='radio' name='question" + str(y) + "' value='" + str(y) + "b' >" + each[2]
#            ans += "<br>" + "<input type='radio' name='question" + str(y) + "' value='" + str(y) + "c' >" + each[3]
#            ans += "<br>" + "<input type='radio' name='question" + str(y) + "' value='" + str(y) + "d' >" + each[4]
#            ans += "<br>" + "<input type='radio' name='question" + str(y) + "' value='" + str(y) + "e' >" + each[5]
#            ans += "<br> <br>"
        ans +=  '''<input type="submit" name="submit" value="I'm done!">'''
        return ans

#global Diver
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
#        if authenticate(form.getvalue("username"),ID,IP):
        body += test()
        if "submit" in form and Diver != True:
            body+=realfacresult(factionresult(points()),username)
	if "sub" in form:
	    if "divergent" in form:
		body+=realfacresult([form.getvalue("divergent")],username)
#            body+= '<br><p><a href="stuymap.py?username='+username+'">Go Check Out Your New Features Here!</a></p>'
#	    body+=str(Diver)
#        else:
#       	    body+="Failed to Authenticate cookie<br>\n"
#            body+='Go Login <a href="login.py">here</a><br>'
#	    body+= form.getvalue("username") + "ID: " + str(ID) + " IP: "+ str(IP)	    
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
