#!/usr/bin/python
import cgitb,hashlib,cgi,random
cgitb.enable()

form=cgi.FieldStorage()

abnegation=[["You're walking down a street and a homeless man asks you if you have change. You...",["Say no and keep walking","Slap him. Why should you give him money?","Say yes and give him moneyc","Say yes, but do nothing"]],["Your mom is making dinner when the doorbell rings. You...",["Yell, Mom! The doorbell rang!","You get the doorc","You open the door and scream go away! We're busy!","Wait until your mom yells, can you get it! then you do it."]],["Your mom gives you ten dollars to spend wherever you want. With the money you..",["Put into savings","Beg for more","Go buy something as soon as you get it","Refuse the money","Buy clothes, food, etc., for the homelessc"]]]
amity=[["When traveling on a budget, you choose to...",["Conserve your money","Trust in the kindness of othersc"]],["When the weekend comes around, your priority is to...",["Be social and make time for friends and familyc","Sleep"]],["When a crowd forms around a famous site, you...",["Join the crowd to share in their excitementc","Wait for it to disperse"]]]
candor=[["As a traveler, you're more trusting of...",["People who seem straightforward and directc","People who are open and welcoming"]],["When friends seem annoyed by your carefree way of life, you...",["Let it go and keep your distance","Share your perspective and tell them to deal with itc"]],["What do you think makes friendships last?",["Being honest and expressivec","Being accepting and not judgemental"]]]
dauntless=[["You want to buy an item from a street vendor who gets pushy. You choose to...",["Forgo the purchase to avoid unpleasant haggling","Negociating hard to strike a good dealc"]],["If a favorite place was at risk of being torn down, you would...",["Support a community movement to preserve itc","Accept that it will soon be gone and move on"]],["The time comes for you to move on. You choose to...",["Stay in familiar territory","Travel to new placesc"]]]
erudite=[["A coin is weighted so that the probability of heads is 2/3. What is the probability of getting exactly two heads in five tosses of the coin?",["40/243c","43/243","55/298","12/679"]],["The sum of the first five terms of an arithmetic series is 70, while the sum of the first ten terms of the same series is 210. What is the first term?", ["5","2/3","42/5c","10/17"]],["For the function f(x)=2sinx-1, find the amplitude, vertical displacement, range, frequency, and period. Please answer the questions in order with commas separating each.",["8,-3,(-5,2),4,2pi","2,-1,(-3,1),1,2pic","6,-2,(-5,4),7,1/2pi","10,-9,(-3,2),8,1/4pi"]]]
#Question pool: Abnegation: 0 Amity: 0 Candor: 0 Dauntless: 0 Erudite: 3

def test2():
    ans = "<h1> Check your compatibility with other factions! </h1>"
    ans += "<h2> How do you want to make your test? </h2>"
    ans += 'Back to the <a href="stuymap.py?username=' + str(form.getvalue('username')) + '">mainpage!</a><br><br>'
    ans += '<form method="GET" action="test2.py">'
    ans += '<input type="hidden" name="username" value="' + form.getvalue('username') + '">'
    ans += 'Total questions: <input type="text" name="number" size="10" value="5">'
    ans += '<br><br>Abnegation<input type="checkbox" name="abnegation" value="true">'
    ans += '<br>Amity<input type="checkbox" name="amity" value="true">'
    ans += '<br>Candor<input type="checkbox" name="candor" value="true">'
    ans += '<br>Dauntless<input type="checkbox" name="dauntless" value="true">'
    ans += '<br>Erudite<input type="checkbox" name="erudite" value="true">'
    ans += '<br><br><input type="submit" name="submit1" value="Submit!">'
    return ans

print 'content-type: text/html\n'
head =  '''<head>
<title>Compatibility Test</title>
 <style>
 body {
   background-image: url("pictures/test04.jpg");
   background-repeat: no-repeat;
   background-attachment: fixed;
   background-position: center;
   background-size:cover;
 }
 </style>
 </head>'''
print head
print test2()

#test=[]
#answers=[]
def quiz():
#if "submit1" in form:
#    global test
    test=[]
    answers=[]

    if "abnegation" in form:
        for each in abnegation:
            test.append(each[0])
            answers.append(each[1])
    if "amity" in form:
        for each in amity:
            test.append(each[0])
            answers.append(each[1])
    if "candor" in form:
        for each in candor:
            test.append(each[0])
            answers.append(each[1])
    if "dauntless" in form:
        for each in dauntless:
            test.append(each[0])
            answers.append(each[1])
    if "erudite" in form:
        for each in erudite:
            test.append(each[0])
            answers.append(each[1])
#    print test
#    print answers
    return test, answers

#answers=test()[1]
def correctness(t):
    if t[-1]=='c':
        return 'correct'
    else:
        return 'bad'

def sub1():
    if "submit1" in form:
        test,answers = quiz()
        dontDelete1, dontDelete2 = test, answers
        tnumber=form.getvalue("number")
        if not (tnumber is None):
            tnumber = int(form.getvalue("number"))
            if tnumber > len(test):
                print "<br><br>Your number has exceeded the question bank<br>On the bright side, that's less work for you :)"
            if tnumber <= 0:
                test = []
            length=len(test)
            while tnumber < length:
                index = random.randint(1,length)-1
                del test[index]
                del answers[index]
                length -= 1
            if len(test) > 0:
                print '<br><br><form method="GET" action="test2.py>"'
                y = 0
                for each in test:
                        print '<br><br>' + str(each)+'<br>'
                        x=0
                        for every in answers[y]:
                            if x==0:
                                print every.strip('c')+'''<input type="radio" name="ques''' + str(y) + '" value="'+correctness(every)+'" checked><br>'
                            else:
                                print every.strip('c')+'''<input type="radio" name="ques''' + str(y) + '" value="'+correctness(every)+'"><br>'
                            x+=1
                        y += 1
            print '<input type = "hidden" name="num" value="' + str(len(dontDelete1)) + '">'
            print '<br><input type = "submit" name="submit2" value="Submit!"></form>'
#    print "submit2" in form
#    print form
#print test

def sub2():
    if "submit2" in form:
        print "<br><br> Results: <br>"
        points = 0
    #    print test
        num= int(form.getvalue('num'))
        x=0
        while x < num:
            print "<br>" + str(x + 1) + ". "
            ans=form.getvalue("ques" + str(x))
            if ans=="correct":
                points += 1
                print "Correct - Well Done ^.^"
            else:
                print "Better luck next time"
            x+=1

sub1()
sub2()
