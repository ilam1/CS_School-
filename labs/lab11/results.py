#!/usr/bin/python
print "content-type: text/html\n"

from cmath import sqrt

import cgi
import cgitb
cgitb.enable()
formresults = cgi.FieldStorage()

print formresults

#for each in formresults:
#    print each 
#    print formresults.getvalue(each) + "<br>"

if "value1" in formresults and "value2" in formresults:
    if formresults.getvalue("value1").isdigit() and formresults.getvalue("value2").isdigit():
        print "<br>" + formresults.getvalue("value1"), formresults.getvalue("value2") +"<br>"
        print str(int(formresults.getvalue("value1")) + int(formresults.getvalue("value2"))) + "<br>"
        if "Sqrt" in formresults:
            print str(sqrt(float(formresults.getvalue("value1")))), str(sqrt(float(formresults.getvalue("value2"))))
