#!/usr/bin/python
print "content-type: text/html\n"

import cgi
import cgitb
cgitb.enable()
formresults = cgi.FieldStorage()

f=open("MOCK_DATA.csv", 'r')
text = f.read()
f.close()

def fixCommas(L):
    for inner in L:
        i=0
        while i < len(inner):
            res = ''
            if inner[i][0]=='"':
                while inner[i][-1] != '"' and i<len(inner):
                    res += inner[i]+","
                    inner.pop(i)
                inner[i]=(res+inner[i]).strip('"')
            i+=1
            
def makeList(s):
    ans=s.split("\n")
    ans = ans[1:]
    numStudents=0
    studentTotal=0
    for each in range(len(ans)-1):
        ans[each] = ans[each].split(',')
        each2 = ans[each]
        numStudents += 1
        totalScore=0
        if each2[-4].isdigit() and each2[-3].isdigit() and each2[-2].isdigit() and each2[-1].isdigit():
            totalScore = int(each2[-3])+int(each2[-2])+int(each2[-1])
        if totalScore > 0:
            ans[each].append(str(totalScore))
            studentTotal += totalScore           
    fixCommas(ans)
    return ans
r= makeList(text)
r=r[:len(r)-1]
#print r

def makeTableBody(L):
    ans = "<table border ='1'> <tr><th> ID </th> <th> First Name </th> <th> Last Name </th> <th> Email </th> <th> State of Residence </th> </tr>"
    for each in L:
        ans += "<tr>"
        while len(each) > 0:
            ans += "<td>" + str(each[0]) + "</td>"
            each=each[1:]
        ans += "</tr>\n"
    ans += "</table>"
    return ans

def matchcriteria(L,x,num): #matches criteria on L based on x
    ans=[]
    for each in L:
	if x.lower() in each[num].lower():
	    ans.append(each)
    return ans         
#print makeTableBody(matchcriteria(r[:50],"an", 2))

#If neither 1 nor 4 are checked
if "findbyname" not in formresults and "state" not in formresults: 
    print makeTableBody(r)

#If only 1 is checked
if "findbyname" in formresults and "state" not in formresults:
    if formresults.getvalue('radio') == 'First':
        print makeTableBody(matchcriteria(r,formresults.getvalue('searchterm'),1))
    if formresults.getvalue('radio') == 'Last':
        print makeTableBody(matchcriteria(r,formresults.getvalue('searchterm'),2))
    if formresults.getvalue('radio') == 'email':
        print makeTableBody(matchcriteria(r,formresults.getvalue('searchterm'),3))

#If only 4 is checked
if "findbyname" not in formresults and "state" in formresults:
    print makeTableBody(matchcriteria(r,formresults.getvalue('residence'),4))



#If 1 and 4 are both checked
if "findbyname" in formresults and "state" in formresults:
    if formresults.getvalue('radio') == 'First':
        print makeTableBody(matchcriteria(matchcriteria(r,formresults.getvalue('residence'),4), formresults.getvalue('searchterm'),1))
    if formresults.getvalue('radio') == 'Last':
        print makeTableBody(matchcriteria(matchcriteria(r,formresults.getvalue('residence'),4), formresults.getvalue('searchterm'),2))
    if formresults.getvalue('radio') == 'email':
        print makeTableBody(matchcriteria(matchcriteria(r,formresults.getvalue('residence'),4), formresults.getvalue('searchterm'),3))
