#!/usr/bin/python
print "content-type: text/html\n"


def fixCommas(L):
    for inner in L:
        i=0
        while i < len(inner):
            res = ''
            #if you see an open double quote pop and 
            #concatenate them until you see a close quote.
            if inner[i][0]=='"':
                while inner[i][-1] != '"' and i<len(inner):
                    res += inner[i]+","
                    inner.pop(i)
                #when you find the close quote,
                #replace it with the completed string.
                inner[i]=(res+inner[i]).strip('"')
            i+=1
            
def makeList(s):
    y=0
    fixCommas(s)
    ans=s.split("\n")
    for each in range(len(ans)):
        ans[each]=ans[each].split(",")
        for num in each:
            y += int(num)
        each.append(y)
    return ans
t = '''1,2,3
4,5,6
8,fish,10'''
print makeList(t)

def makeTableBody(L):
    ans=""
    for each in L:
        ans += "<tr>"
        while len(each) > 0:
            ans += "<td>" + str(each[0]) + "</td>"
            each=each[1:]
        ans += "</tr>\n"
    return ans
#print makeTableBody( [ [1,2],['a','b'] ] )


