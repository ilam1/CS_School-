#!/usr/bin/python
import cgitb,hashlib,cgi,random
cgitb.enable()

form=cgi.FieldStorage()

abnegation=[["question1","ans1"],["question2","ans2"],["question3","ans3"]]
amity=[["question1","ans1"],["question2","ans2"],["question3","ans3"]]
candor=[["question1","ans1"],["question2","ans2"],["question3","ans3"]]
dauntless=[["question1","ans1"],["question2","ans2"],["question3","ans3"]]
erudite=[["A coin is weighted so that the probability of heads is 2/3. What is the probability of getting exactly two heads in five tosses of the coin?","40/243"],["The sum of the first five terms of an arithmetic series is 70, while the sum of the first ten terms of the same series is 210. What is the first term?", "42/5"],["For the function f(x)=2sinx-1, find the amplitude, vertical displacement, range, frequency, and period.","2,-1,[-3,1],1,2pi"]] 
#Question pool: Abnegation: 0 Amity: 0 Candor: 0 Dauntless: 0 Erudite: 3

def test2():
    ans = "<h1> How do you want to make your test? </h1>"
    ans += '<form method="GET" action="test2.py">'
    ans += 'Total questions: <input type="text" name="number" size="10" value="5">'
    ans += '<br><br>Abnegation<input type="checkbox" name="abnegation" value="true">'
    ans += '<br>Amity<input type="checkbox" name="amity" value="true">'
    ans += '<br>Candor<input type="checkbox" name="candor" value="true">'
    ans += '<br>Dauntless<input type="checkbox" name="dauntless" value="true">'
    ans += '<br>Erudite<input type="checkbox" name="erudite" value="true">'
    ans += '<br><br><input type="submit" name="submit1" value="Submit!">'
    return ans

print 'content-type: text/html\n'
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

if "submit1" in form:
    test,answers = quiz()
    dontDelete1, dontDelete2 = test, answers
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
    	
#    print test
    if len(test) > 0:
        print '<br><br><form method="GET" action="test2.py"'
        y = 0
        for each in test:
            print '<br>' + str(each) + '''  <input type="text" name="ques''' + str(y) + '''" size="20">'''
            y += 1
        print '<input type = "hidden" name="test" value="' + str(dontDelete1) + '"><br>\n<input type = "hidden" name="answers" value="' + str(dontDelete2) +'"><br>'
        print '<br><input type = "submit" name="submit2" value="Submit!">'
#    print "submit2" in form
#    print form
#print test
if "submit2" in form:
    print "<br><br> Results: <br>"
    points = 0
#    print test
    test, answers = eval(form.getvalue('test')), eval(form.getvalue('answers'))
    for each in range(len(test)):
        print "<br>" + str(each + 1) + ". "
	if form.getvalue("ques" + str(each)) == answers[each]:
	    points += 1	
	    print "Correct - Well Done ^.^"
	else:
	    print "Better luck next time"
 
