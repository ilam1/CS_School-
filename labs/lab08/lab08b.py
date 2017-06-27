#!/usr/bin/python
print "content-type: text/html\n"

import cgitb
cgitb.enable()

import random
def lowerletters(string):
    x=""
    while len(string) > 0:
        if string[0] == " ":
            x += " "
        if 48 <= ord(string[0]) <= 57:
            x += string[0]
        if 'a' <= string[0] <= 'z':
            x += string[0]
        elif 'A' <= string[0] <= 'Z':
            x += chr(ord(string[0]) + 32)
        elif "." == string[0]:
            x += string[0]
        elif "," == string[0]:
            x += string[0]
        elif "'" == string[0]:
            x += string[0]
        elif "\n" == string[0]:
            x += " "
        elif "--" == string[0:2]:
            x += " "
        elif "-" == string[0]:
            x += string[0]
        string=string[1:]
    return x

def findword(string):
    x=""
    while len(string) > 0:
        if string[0] == " ":
            return x
        else:
            x += string[0]
        string = string[1:]
    return x
#print findword("a b a c a b fish happy meal fish")

def TallyWords(text):
    ans = {}
#    text = text.lower()
#    text = text.split()
#    print text
    for each in range(len(text)):
        y = text[each].strip("""\.',-!@":;$%^&*[]()=+?><_""")
#        print y
        if len(y) != 0:
            if y in ans:
                ans[y] += 1
            else:
                ans[y] = 1
    return ans

def printlist(a,b):
  x=""
  i=0
  while len(a) > i:
    #print str(a[i]) + ":" + str(b[i]) + "\n"
    x += str(a[i]) + ":" + str(b[i]) + "\n"
    i += 1
  return x

v=random.randint(0,1)
s=""
if v == 0:
    fileName = 'dante.txt'
    s="Dante.txt"
else:
    fileName = 'macbeth.txt'
    s="Macbeth.txt"


f = open(fileName, 'r')
text = f.read()
f.close()
text = text.lower()
text = " ".join(text.split('--'))
text = text.split()
x=TallyWords(text)
#for each in range(len(text)):
#    y = text[each].strip("""\.',-!@":;$%^&*()=+?><_""")

#for key in sorted(x.iterkeys()):
#   print "%s: %s" % (key, x[key])


#print x
#print sorted(x)
def printtable(x):
    ans ='<!DOCTYPE html>\n<html>\n <head><title>Tally of ' + s+ ' </title></head>\n <body>\n <h1> Word count of ' + s + ' </h1>'
    ans += '''<table border="1" width="15%"><tr> \n <th> Words </th> <th> Tally </th> </tr>'''
    for each in sorted(x):
#        print each + "<br>"
        ans += "<tr> \n <td> " + str(each) + "</td> <td>" + str(x[str(each)]) + "</td> </tr>"
    ans += " </td> </tr></table> \n </table> \n </body> \n</html>"
    return ans
print printtable(x)

#print "<!DOCTYPE html>\n<html>\n <head><title>" '''</title></head>\n <body>\n <table border="1">'''
#print " <tr> \n <th> Words </th> <th> Tally </th> </tr>"
#print " <tr> \n <td>" + printlist(w,t) + "</tr>"
#print " </table> \n </body> \n</html>"
