#!/usr/bin/python
print "content-type: text/html\n"
def startPage(title):
    return "<!DOCTYPE html>\n<html>\n <head><title>" + title + "</title></head>\n <body>"
def makeRow(numCols, startValue):
    x="   <tr>"
    while numCols > 0:
      x=x+"<td>" + str(startValue) + ": '" + str(chr(startValue)) + "'" + "</td>"
      numCols=numCols-1
      startValue=startValue+1
    return x + "</tr>\n" 
def makeTable(Rows,Cols,startValue):
    x=" <table>\n"
    while Rows>0:
      x=x+makeRow(Cols,startValue)
      Rows=Rows-1
      startValue=startValue+Cols
    return x + " </table>"
#print startPage("Bazinga")
#print makeRow(2,1)
#print makeRow(2,12)
#print makeRow(4,99)
#print makeTable(2,4,11)
#print makeTable(4,2,133) 
#print startPage("ASCII")
#print makeTable(3,4,5)
#print "</body> </html>"

print startPage("FINAL STEP!")
print makeTable(14,16,32)
print " </body>\n</html>"
