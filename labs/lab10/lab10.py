#!/usr/bin/python
print "content-type: text/html\n"
f = open("SAT.csv", 'r')
text = f.read()
f.close()

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
#    y=0
#    fixCommas(s)
    ans=s.split("\n")
    ans = ans[1:]
    numStudents=0
    studentTotal=0
    # ans = [each.split(',') for each in ans]
    for each in range(len(ans)-1):
#        fixCommas(ans[each])
#         ans[each] = ans[each].split(",")
#         fixcomma(ans)
#    for each in range(len(ans)-1):
        #fixCommas(ans[each])
        ans[each] = ans[each].split(',')
        each2 = ans[each]
        numStudents += 1
        totalScore=0
#	print each2[3]
        if each2[-4].isdigit() and each2[-3].isdigit() and each2[-2].isdigit() and each2[-1].isdigit():
            totalScore = int(each2[-3])+int(each2[-2])+int(each2[-1])
        if totalScore > 0:
            ans[each].append(str(totalScore))
            studentTotal += totalScore           
        #ans[each] = ans[each].split(",")
    fixCommas(ans)
#	if each2[3].isdigit():
#		totalScore += int(each2[3]) + int(each2[4]) + int(each2[5])
#	if totalScore > 0:
#		ans[each] += "," + str(totalScore)
#		studentTotal += totalScore
#        for num in ans[each]:
#          if num.isdigit():
#            totalScore += int(num)
#        ans[each].append("," + str(totalScore))
#    return ans
#    return numStudents, studentTotal/numStudents
#    for num in range(ans[each]):
#        if str(ans[each]).isalpha() == False:
#           y += int(ans[each])
#        ans[each].append(y/len(ans))
#        print ans[each]
    return ans
#t = '''1,2,3
#4,5,6
#8,fish,10'''
#print makeList(t)

def printing(list):
  for each in list:
    print each + "\n"
#printing( makeList(text))
r= makeList(text)

def totalstudents(L):
    ans=0
    for each in range(len(L)-1):
      if L[each][2].isdigit() == True:
        ans += int(L[each][2])
    return ans 

def averagescore(L): 
    x=0
    for each in range(len(L) - 1):
        if L[each][2].isdigit() and len(L[each]) > 6:#L[each][6].isdigit():
            x += float(L[each][2]) * float(L[each][6])
    return x / totalstudents(L)       

def makeTableBody(L):
    ans = "<!DOCTYPE html> <html> \n <head> \n <title> Lab 10 </title> <body>"
    ans += "<h3> Number of students that took the exam: " + str(totalstudents(r)) + " </h3>"
    ans += "<h3> Average score for ALL students: " + str(averagescore(r)) + " </h3>"
    ans += "<table> <tr><th> DBN </th><th> SCHOOL NAME</th> <th> Num of SAT Test Takers</th> <th> SAT Critical Reading Avg. Score</th> <th> SAT Math Avg. Score</th> <th> SAT Writing Avg. Score</th> <th> Total Score </th> </tr>"
    for each in L:
        ans += "<tr>"
        while len(each) > 0:
            ans += "<td>" + str(each[0]) + "</td>"
            each=each[1:]
        ans += "</tr>\n"
    ans += "</table> </body> </html>"
    return ans
#print makeTableBody( [ [1,2],['a','b'] ] )
print makeTableBody(r)


