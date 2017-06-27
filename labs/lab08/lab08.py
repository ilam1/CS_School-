#!/usr/bin/python
print "content-type: text/html\n"

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
##        elif "' " == string[1:3] and "s" != string[0]:
##            string=string[1:]
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
#print lowerletters("a b a c a b fish happy meal fish")
#print lowerletters("""a b a c a b
#     fish    
#happy     meal
#         fish""")
#print lowerletters("""a 
#b a C a b Fish haPpy mEaL 
#fiSH""")
#print lowerletters("""a 
#b a! C a b!!!! "Fish" happy meal. 
#fish?""")
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
    words = []
    tally = []
    x=0
    text = lowerletters(text)
    text = text.split()
    while x < len(text):
        y=text[x].strip('''\.,'-!@#$%^&*()=+|?>_<''')
        if len(y) != 0:
            if y in words:
                tally[words.index(y)] += 1
            else:
                words.append(y)
                tally.append(1)
        x += 1
        #text=text[len(y) + 1:]
        #print words,tally
    return words,tally


#print TallyWords("a b a c a b fish happy meal fish")
#print TallyWords("""a b a c a b
#     fish    
#happy     meal
#         fish""")
#print TallyWords("""a 
#b a C a b Fish haPpy mEaL 
#fiSH""")
#print TallyWords("""a 
#b a! C a b!!!! "Fish" happy meal. 
#fish?""")
#print TallyWords("The great hero bob was the best hero the the.")

def printlist(a,b):
  x=""
  i=0
  while len(a) > i:
    #print str(a[i]) + ":" + str(b[i]) + "\n"
    x += str(a[i]) + ":" + str(b[i]) + "\n"
    i += 1
  return x
#print printlist([1,2,3,4], ["a","b","c","d"])
#print printlist(TallyWords("a b a c a b fish happy meal fish"))
#a=TallyWords("a b a c a b fish happy meal fish")
#print printlist(a[0], a[1])
#b=TallyWords("The great hero bob was the best hero the the.")
#print printlist(b[0], b[1])
#print printlist(a)


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
w,t=TallyWords(text)
#print printlist(w,t)

def once(a,b):
    i=0
    x=0
    while len(a) > i:
      if b[i] == 1:
        x += 1
      i += 1
    return x
#once(w,t)

def firsthundred(a,b):
    i=0
    x= 0
    y="<br>"
    while x < 100:
      if b[i] == 1:
        y += a[i] + "<br>"
        x += 1
      i += 1
    return y

def mostcommon(a,b):
    x="<table border ='1' width='15%'> <tr><th> Words </th> <th> Tally </th> </tr>"
    y=0
    c=[]
    c.extend(a)
    d=[]
    d.extend(b)
    while y < 10:
      x += "<tr><td>" + str(c[d.index(max(d))]) + "</td><td>" + str(max(d)) + "</td></tr>"
      d.insert(d.index(max(d)),0)
      d.remove(max(d))
      y += 1
    return x + "</table>"
#print mostcommon(w,t)

def totalwords(a,b):
    i = 0
    x=0
    while i < len(b):
       x += b[i]
       i += 1
    return x

def printtable(a,b):
    x='''<!DOCTYPE html>\n<html>\n <head><title>Tally of ''' + s+ ''' </title></head>\n <body>\n <h1> Word count of ''' + s + ''' </h1>'''
    x += "Number of words total: " + str(totalwords(w,t)) + '<br><br>'
    x += "Number of distinct words: " + str(len(a)) + '<br><br>' 
    x += "Words that occur once: " + str(once(w,t)) + "<br><br>"
    x += "  <table width ='75%'> <tr> <th> First 100 words that appear once: </th>"
    x += "<th> Top 10 most common words: </th> <th> Tally of All Words </th> </tr>"
    x += "<tr> <td valign='top' align='center'>" + str(firsthundred(w,t)) + "</td> <td valign = 'top' align='center'> <br>" + mostcommon(w,t) +"</td> <td> <br>"
    #x += "First 100 words that appear once: " + str(firsthundred(w,t)) 
    #x +=  mostcommon(w,t)
    x += '''<table border="1" width="15%" align='center'><tr> \n <th> Words </th> <th> Tally </th> </tr>'''
    i=0
    while len(a) > i:
        x += "<tr> \n <td> " + str(a[i]) + "</td> <td>" + str(b[i]) + "</td> </tr>"
        i += 1
    x += " </td> </tr></table> \n </table> \n </body> \n</html>"
    return x

print printtable(w,t)

#print "<!DOCTYPE html>\n<html>\n <head><title>" '''</title></head>\n <body>\n <table border="1">'''
#print " <tr> \n <th> Words </th> <th> Tally </th> </tr>"
#print " <tr> \n <td>" + printlist(w,t) + "</tr>"
#print " </table> \n </body> \n</html>"


