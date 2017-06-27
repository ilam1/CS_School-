#!/usr/bin/python
print "content-type: text/html\n"

import cgitb
cgitb.enable()

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

f = open('dante.txt', 'r')
Dante = f.read()
f.close()
Dante = Dante.lower()
Dante = " ".join(Dante.split('--'))
Dante = Dante.split()
x=TallyWords(Dante)

g=open('macbeth.txt', 'r')
Macbeth = g.read()
g.close()
Macbeth = Macbeth.lower()
Macbeth = " ".join(Macbeth.split('--'))
Macbeth = Macbeth.split()
y=TallyWords(Macbeth)

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
#print uniquewords(x)

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
#print invert(x)

#def mostcommon(x):
#    max(x.values())
#print x[str(max(x.values() ))]

def genVals(d):
    d2=sorted(d)
    L=[]
    for i in range(len(d)):
        L.append(d[d2[i]])
    return L

def Compare(v1,v2):
    x=''
    if v1>v2:
        x='Dante'
    else:
        x='Hamlet'
    return x

def Content(L1,L2):
    HorD=[]
    Vals=[]
    for i in range(len(L1)):
        HorD.append(Compare(L1[i],L2[i]))
        Vals.append(abs(L1[i]-L2[i]))
    return HorD,Vals

dpercent={}
mpercent={}
#def printtable(x,y):
#    ans ='<!DOCTYPE html>\n<html>\n <head><title>Tally </title></head>\n <body>\n' #<h1> Word count of ' + s + ' </h1>'
#    ans += '<table width="50%"> <tr> <th> Dante </th> <th> Macbeth </th> <th> Highest %</th></tr> \n'
#    ans += '''<tr> <td><table border="1"><tr> \n <th> Words </th> <th> Tally </th> <th> % </th> </tr>'''
#    for each in sorted(x):
#        xpercent= round(100 * float(x[each]) / sum(x.values()), 3)
#        ans += "<tr> \n <td> " + str(each) + "</td> <td>" + str(x[each]) + "</td> <td>" + str( round(100 * float(x[each]) / sum(x.values()), 3)) + "</td> </tr>"
#       dpercent[each]=xpercent
#    ans += " </table> </td>  \n"
#    ans += '''<td> <table border = "1"> <tr> \n <th> Words </th> <th> Tally </th> <th> % </th> </tr>'''
#    for each in sorted(y):
#        ypercent=  round(100 * float(y[each]) / sum(y.values()), 3)
#        ans += "<tr> \n <td> " + str(each) + "</td> <td>" + str(y[each]) + "</td> <td>" + str( round(100 * float(y[each]) / sum(y.values()), 3)) + "</td> </tr>"
#        mpercent[each]=ypercent
#    ans += " </table> </td> \n"
#    return ans
#print printtable(x, y)

dantevals=genVals(dpercent)
macvals=genVals(mpercent)
HorD,Vals=Content(dantevals,macvals)


'''def ListtoDict(L1,L2):
    d3={}
    for i in range(len(L1)):
        d3[L1[i]]=L2[i]
    return d3
print ListtoDict(L3,L4)'''



'''dantekeys=sorted(dpercent.keys())[:50]
mackeys=sorted(mpercent.keys())[:50]'''

dpercent={}
mpercent={}
def printtable(x,y):
    xcopy=x.copy()
    ycopy=y.copy()
    zcopy = invert(xcopy)
    acopy = invert(ycopy)
    temp = xcopy.values()
    temp2= ycopy.values()
    ans ='<!DOCTYPE html>\n<html>\n <head><title>Tally </title></head>\n <body>\n <h1> Word count </h1>'
    ans += "<h3> Number of unique words </h3> <ul> <li> Dante: " + str(uniquewords(x)) + "</li> <li> Macbeth: " + str(uniquewords(y)) + "</li></ul> \n"
    ans += '<table width="60%"> <tr> <th> 20 most common words in Dante </th><th> 20 most common words in Macbeth </th> <th> Dante </th> <th> Macbeth </th> <th> Percent Comparison </th> </tr>'
    ans += '''\n<tr><td valign='top'><table border = "1"> <tr> <th> Words </th> <th> Tally </th> </tr>'''
#    print temp.pop(temp.index(max(temp)))
#20 most common words in Dante
    for each in range(20):
        a = temp.pop(temp.index(max(temp)))
        if len(zcopy[a]) == 1:
            ans += "<tr> <td>" + str(zcopy[a][0]) + "</td> <td>" + str(a) + "</td> </tr>"
        #ans += "<tr> <td>" + str(zcopy[max(xcopy.values())]) + "</td> <td>" + str(max(xcopy.values())) + "</td> </tr>"
            zcopy[a] = 0
        else:
            ans += "<tr> <td>" + str(zcopy[a][0]) + "</td> <td>" + str(a) + "</td> </tr>"
            del zcopy[a][0]# = 0
        #zcopy[max(xcopy.values())] = 0
    ans += '''</table> </td>'''
    ans += '''<td valign='top'><table border = "1"> <tr> <th> Words </th> <th> Tally </th> </tr>'''
#    print temp.pop(temp.index(max(temp)))
#20 most common words in Macbeth
    for each in range(20):
        a = temp2.pop(temp2.index(max(temp2)))
        if len(acopy[a]) == 1:
            ans += "<tr> <td>" + str(acopy[a][0]) + "</td> <td>" + str(a) + "</td> </tr>"
        #ans += "<tr> <td>" + str(zcopy[max(xcopy.values())]) + "</td> <td>" + str(max(xcopy.values())) + "</td> </tr>"
            acopy[a] = 0
        else:
            ans += "<tr> <td>" + str(acopy[a][0]) + "</td> <td>" + str(a) + "</td> </tr>"
            del acopy[a][0]# = 0
        #zcopy[max(xcopy.values())] = 0
    ans += '''</table> </td>'''
#Dante tally word count
    ans += '''<td><table border="1""><tr> \n <th> Words </th> <th> Tally </th> <th> % </th> </tr>'''
    for each in sorted(x):
        xpercent= round(100 * float(x[each]) / sum(x.values()), 3)
        ans += "<tr> \n <td> " + str(each) + "</td> <td>" + str(x[each]) + "</td> <td>" + str( round(100 * float(x[each]) / sum(x.values()), 3)) + "</td> </tr>"
        dpercent[each]=xpercent
    ans += " </td> </table> \n"

#    ans += '''<td><table border="1"><tr> \n <th> Words </th> <th> Tally </th> <th> % </th> </tr>'''
#    for each in sorted(x):
#        ans += "<tr> \n <td> " + str(each) + "</td> <td>" + str(x[each]) + "</td> <td>" + str( round(100 * float(x[each]) / sum(x.values()), 3)) + "</td> </tr>"
#    ans += " </td> </table> \n"
#Macbeth tally word count
    ans += '''<td> <table border = "1"> <tr> \n <th> Words </th> <th> Tally </th> <th> % </th> </tr>'''
    for each in sorted(y):
        ypercent=  round(100 * float(y[each]) / sum(y.values()), 3)
        ans += "<tr> \n <td> " + str(each) + "</td> <td>" + str(y[each]) + "</td> <td>" + str( round(100 * float(y[each]) / sum(y.values()), 3)) + "</td> </tr>"
        mpercent[each]=ypercent
        ans += "<tr> \n <td> " + str(each) + "</td> <td>" + str(y[each]) + "</td> <td>" + str( round(100 * float(y[each]) / sum(y.values()), 3)) + "</td> </tr>"
    ans += "</table> \n </body> \n</html>"
    return ans
print printtable(x, y)
def printpercent(L3,L4):
    ans='<td><table border="1"><tr><th>Book</th><th>Difference</th></tr>'
    for each in range(len(L3)):
        ans+='<tr> \n <td>' +str(L3[each])+'</td><td>'+str(L4[each])+'</td> </tr>'
    ans+='</table></td>\n'
    ans+= "</table> \n </body> \n</html>"
    return ans

#print reList(HorD,Vals)
print printpercent(HorD,Vals)
