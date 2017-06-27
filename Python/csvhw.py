#def makeTable( allLines ):
#   ans = "<table>\n"
#   for each in allLines:
#      ans += "<tr>"
#      comma=allLines.split(",")
#      for each in comma:
#        ans += "<td>" + str(comma[0]) + "</td> \n"
#        ans += "</tr>"
#   return ans+"</table>\n"

#def makTable(allLines):
#  ans = "<table>\n"
#  for each in allLines:
#    ans += "<tr>"
#    comma= allLines.split(",")
#    i = 0
#    while len(comma[i]) > 0:
#      ele = comma.split(",")
#      ans += "<td>" + ele[0] + "</td> \n"
#      ele = ele[1:]
#      if len(ele) == 0:
#        comma[i] = ""
#    i += 1
#    ans += "</tr>\n"
#  return ans + "</table>\n"
text = """a,b,c
d,e,f"""

def makeTable( allLines ):
   ans = "<table>\n"            
   for row in allLines:
      ans += "<tr>"             
      comma = row.split(",")    
      for value in comma:    
         ans += "<td>" + value + "</td>"
      ans += "</tr>\n"       
   return ans + "</table>\n" 

#text2="""fish,dog,cat
#1,99,3
#o o,this is, so strange
#"""
data=text.split("\n")
print makeTable(data)
