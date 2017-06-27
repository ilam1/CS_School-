x = open('values.txt','r')
y = open('operations.txt','r')
a=x.read()
b=y.read()

x.close()
y.close()

#varnames (lookup table) = header
def hw(operation,value):
  operationLine=operation.split('\n')
  operationLine=[x for x in operationLine if x]
  valueLine=value.split('\n')
  valueLine=[x for x in valueLine if x]
  header = valueLine[0].split(',')
  valueLine=valueLine[1:]
#  print header
#  print valueLine
#  print operationLine
  ans=""
  #op=["+","-","*","/"]
  for index in range(len(operationLine)):
      line = operationLine[index].split(' ')
      #print operationLine
#      print line
      for char in range(len(header)):
        if line[0] == header[char]:
            first = char                      
        if line[2] == header[char]:
            sec = char                      
      num = valueLine[index].split(',')
#      nums = valueLine[index + 1].split(',')
#      print num[first]
#      print num[sec]
#      print num[first] + num[sec]
      if line[1] == "+":
        ans += str(float(num[first]) + float(num[sec]))
      if line[1] == "-":
        ans += str(float(num[first]) - float(num[sec]))
      if line[1] == "*":
        ans += str(float(num[first]) * float(num[sec]))
      if line[1] == "/":  
        ans += str(float(num[first]) / float(num[sec]))
      ans += "\n"
##      for opp in range(len(op)):
##        if opp == 0:
##            ans += "?"+str(int(float(num[first])) * int(float(num[sec])))
##        if opp == 1:
##            ans += "?"+str(int(float(num[first])) - int(float(num[sec])))
##        if opp == 2:
##            ans += "?"+str(int(float(num[first])) + int(float(num[sec])))
##        if opp == 3:
##            if num[sec] == "0":
##              ans += "Undefined"
##            else:
##              ans += "?"+str(float(num[first]) / float(num[sec]))
##      ans += "\n"
  return ans 

#print hw(b, a)

outfile = open('output.txt','w')
outfile.write(hw(b,a))
outfile.close()
