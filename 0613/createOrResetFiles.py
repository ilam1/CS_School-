#!/usr/bin/python
print 'content-type: text/html'
print ''
import cgitb
cgitb.enable()
print "Attempt to write file<br>"
directory = "data/"
f = open(directory+"users.txt",'w')
f.close()
f = open(directory+"loggedin.txt",'w')
f.close()
f = open(directory+"amity.txt",'w')
f.close()
f = open(directory+"abnegation.txt",'w')
f.close()
f = open(directory+"dauntless.txt",'w')
f.close()
f = open(directory+"erudite.txt",'w')
f.close()
f = open(directory+"candor.txt",'w')
f.close()
f = open(directory+"am.txt",'w')
f.close()
f = open(directory+"ab.txt",'w')
f.close()
f = open(directory+"da.txt",'w')
f.close()
f = open(directory+"er.txt",'w')
f.close()
f = open(directory+"ca.txt",'w')
f.close()
f = open(directory+"description.txt",'w')
f.close()
print "Completed attempt<br>"

