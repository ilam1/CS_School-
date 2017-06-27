#!/usr/bin/python
print "content-type: text/html\n"

#import cgitb
#cgitb.enable()

def optionVals():
    ans=''
    for i in range(26):
        ans+='\t\t\t\t<option value="'+str(chr(i+ord('a')))+'">'+str(chr(i+ord('a')))+'</option>\n'
    return ans

print "Product of : Melina Tsai and Irene Lam"

print '''<!DOCTYPE html>
<html>
\t<head><title>Tally</title></head>'''
print '\t<body>'
print '<h3>Books to compare:</h3>'
print '\t\t<form method="GET" action="lab14.py">'
print '\t\t\t<br>'
print '\t\t\tBook 1: <select name="book1" size="1">'
print '\t\t\t\t<option value="hamlet">Hamlet</option>'
print '\t\t\t\t<option value="othello">Othello</option>'
print "\t\t\t\t<option value='dante'>Dante's Inferno</option>"
print '\t\t\t\t<option value="macbeth">Macbeth</option>'
print '\t\t\t</select>'
print '\t\t\t<br>'
print '\t\t\tBook 2: <select name="book2" size="1">'
print '\t\t\t\t<option value="hamlet">Hamlet</option>'
print '\t\t\t\t<option value="othello">Othello</option>'
print "\t\t\t\t<option value='dante'>Dante's Inferno</option>"
print '\t\t\t\t<option value="macbeth">Macbeth</option>'
print '\t\t\t</select> <br> <br>'
print '\t\t\tWords that start with the letter <select name="letters" size="1">'
print optionVals()
print '\t\t\t</select><br>'
print '<input type="submit" name="submitted">'

import cgi
form=cgi.FieldStorage()

book1 = 'dante'
book2 = 'macbeth'
letters= 'a'
#print form
#print 'book1' in form

if 'book1' in form:
    book1=str(form.getvalue('book1'))
if 'book2' in form:
    book2=str(form.getvalue('book2'))
if 'letters' in form:
    letters=str(form.getvalue('letters'))
def TallyWords(text): #dictionary version of tallying words after stripping punctuation
    ans = {}
    for each in range(len(text)):
        y = text[each].strip("""\.',-!@":;$%^&*[]()=+?><_""")
        if len(y) != 0:
            if y in ans:
                ans[y] += 1
            else:
                ans[y] = 1
    return ans
#def bookForm():
#    print '<form method="GET">'
#def bookCompare(txt1,txt2):

f = open(book1+'.txt', 'r')
Dante = f.read()
f.close()
Dante = Dante.lower()
sent1 = Dante.count(".")
Dante = " ".join(Dante.split('--'))
Dante = Dante.split()
x=TallyWords(Dante)
g=open(book2+'.txt', 'r')
Macbeth = g.read()
g.close()
Macbeth = Macbeth.lower()
sent2 = Macbeth.count(".")
Macbeth = " ".join(Macbeth.split('--'))
Macbeth = Macbeth.split()
y=TallyWords(Macbeth)

def startsWith(d,letters):
    L=d.keys()
    count=0
    for i in range(len(L)):
        if L[i][0]==str(letters):
            count+=1
    return count


q=startsWith(x,letters)
r=startsWith(y,letters)


def fillMissing(A,B): #1
    for each in A:
        if each not in B:
            B[each] = 0
fillMissing(x,y)
fillMissing(y,x)

def uniquewords(dicti):
    ans = 0
    for each in dicti:
        if dicti[each] == 1:
            ans += 1
    return ans

def invert(x):
    ans = {}
    for item in x.items():
#        print item[1]
        if item[1] not in ans:
            temp = []
            temp.append(item[0])
            ans[item[1]] = temp
#            print ans[item[1]]
        else:
            ans[item[1]].append(item[0])
#        ans[item[1]] = item[0]
    return ans

def genVals(d):
    d2=sorted(d)
    L=[]
    for i in range(len(d)):
        L.append(d[d2[i]])
    return L

def Compare(v1,v2):
    x=''
    if v1>v2:
        x=book1
    else:
        x=book2
    return x

dpercent = {}
mpercent = {}

def Content(L1,L2):
    HorD=[]
    Vals=[]
    for i in range(len(L1)):
        HorD.append(Compare(L1[i],L2[i]))
        Vals.append(abs(L1[i]-L2[i]))
    return HorD,Vals

#dantevals=genVals(dpercent)
#macvals=genVals(mpercent)
#HorD,Vals=Content(dantevals,macvals)


#def printpercent(L3,L4):
#    ans='<td><table border="1"><tr><th>Book</th><th>Difference</th></tr>'
#    for each in range(len(L3)):
#        ans+='<tr> \n <td>' +str(L3[each])+'</td><td>'+str(L4[each])+'</td> </tr>'
#    ans+='</table></td>\n'
##    ans+= "</table> \n </body> \n</html>"
#    return ans

#print reList(HorD,Vals)
#print printpercent(HorD,Vals)


#dpercent={}
#mpercent={}
def printtable(x,y):
    zcopy = invert(x)
    acopy = invert(y)
    temp = x.values()
    temp2= y.values()
#    ans ='<!DOCTYPE html>\n<html>\n <head><title>Tally </title></head>\n <body>\n <h1> Word count </h1>'
    ans = "<h3> Number of unique words </h3> <ul> <li>" + book1.capitalize() + " : " + str(uniquewords(x)) + "</li> <li>" + book2.capitalize() + " : " + str(uniquewords(y))+ "</li></ul>"
    ans+= "<h3> (Melina)Number of words that start with '"+str(letters)+"' : </h3>"
    ans+= "<ul><li> "+book1.capitalize()+' : '+str(q)+"</li>"
    ans+= "<li>"+book2.capitalize()+' : '+str(r)+"</li></ul>"
    ans += "<h3> (Irene pt.1) Total sentences </h3> <ul> <li>" + book1.capitalize() + " : " + str(sent1) + "</li><li>" + book2.capitalize() + " : " + str(sent2) + "</li></ul>"
    ans += "<h3> (Irene pt.2) Average words per sentence </h3> <ul> <li>" + book1.capitalize() + " : " + str(float(sum(x.values())/sent1)) + "</li><li>" + book2.capitalize() + " : " + str(float(sum(y.values())/sent2)) + "</li></ul>"
    ans += '<table width=1000px> <tr> <th> 20 most common words in ' + book1.capitalize() + ' </th><th> 20 most common words in ' + book2.capitalize() + ' </th> <th> ' + book1.capitalize() + ' </th> <th>' + book2.capitalize() + '</th><th> Highest %</th></tr> \n'
    ans +="<tr><td valign='top'><table border='1'>"
    for each in range(20):
        a = temp.pop(temp.index(max(temp)))
        if len(zcopy[a]) == 1:
            ans += "<tr> <td>" + str(zcopy[a][0]) + "</td> <td>" + str(a) + "</td> </tr>"
        #ans += "<tr> <td>" + str(zcopy[max(xcopy.values())]) + "</td> <td>" + str(max(xcopy.values())) + "</td> </tr>"
            zcopy[a] = 0
        else:
            ans += "<tr> <td>" + str(zcopy[a][0]) + "</td> <td>" + str(a) + "</td> </tr>"
            del zcopy[a][0]# = 0
    ans += '''</table></td> \n <td valign='top'> <table border='1'>'''
    for each in range(20):
        a = temp2.pop(temp2.index(max(temp2)))
        if len(acopy[a]) == 1:
            ans += "<tr> <td>" + str(acopy[a][0]) + "</td> <td>" + str(a) + "</td> </tr>"
            acopy[a] = 0
        else:
            ans += "<tr> <td>" + str(acopy[a][0]) + "</td> <td>" + str(a) + "</td> </tr>"
            del acopy[a][0]
    ans += "</table> </td> \n"
    ans += ''' <td valign='top'><table border = '1'> <tr> <th> Words </th> <th> Tally </th> <th> % </th> </tr>'''
    for each in sorted(x):
        xpercent= round(100 * float(x[each]) / sum(x.values()), 3)
        ans += "<tr> <td> " + str(each) + "</td> <td>" + str(x[each]) + "</td> <td>" + str( round(100 * float(x[each]) / sum(x.values()), 3)) + "</td> </tr>"
        dpercent[each]=xpercent
    ans += "</table></td> \n"
    ans += '''<td valign = 'top'> <table border = '1'> <tr> <th> Words </th> <th> Tally </th> <th> % </th> </tr> \n'''
    for each in sorted(y):
        ypercent=  round(100 * float(y[each]) / sum(y.values()), 3)
        ans += "<tr> <td> " + str(each) + "</td> <td>" + str(y[each]) + "</td> <td>" + str( round(100 * float(y[each]) / sum(y.values()), 3)) + "</td> </tr>"
        mpercent[each]=ypercent
    ans += " </table> </td> \n"
#    ans += printpercent(HorD, Vals)
#    ans += '''</tr> </table> </body> </html>'''
    return ans
print printtable(x, y)

dantevals=genVals(dpercent)
macvals=genVals(mpercent)
HorD,Vals=Content(dantevals,macvals)


'''def ListtoDict(L1,L2):
    d3={}
    for i in range(len(L1)):
        d3[L1[i]]=L2[i]
    return d3
print ListtoDict(L3,L4)'''

def printpercent(L3,L4):
    ans='<td valign="top"><table border="1"><tr><th>Book</th><th>Difference</th></tr>'
    for each in range(len(L3)):
        ans+='<tr> \n <td>' +str(L3[each])+'</td><td>'+str(L4[each])+'</td> </tr>'
    ans+='</table></td>\n'
    ans+= "</tr></table> \n </body> \n</html>"
    return ans

#print reList(HorD,Vals)
print printpercent(HorD,Vals)

'''dantekeys=sorted(dpercent.keys())[:50]
mackeys=sorted(mpercent.keys())[:50]'''


