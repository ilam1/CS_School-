#!/usr/bin/python
print "content-type: text/html\n"
print "<!DOCTYPE html>"
print "<html>"
print " <head> </head>"
print " <body>"
print "<h1> Big Table </h1>"
print '''  <table border="1">'''
x=1
print "    <tr> <td> x </td> <td> x<sup>2</sup> </tr>"
while x <= 100:
    print "    <tr> <td>" + str(x) + "</td> <td>" + str(x**2) + "</td> </tr>"
    x=x+1
print "  </table>"
print " </body>"
print "</html>"
