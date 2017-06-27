def numToWords9(i):
    if i==1: 
      return "one"
    if i==2:  
      return "two"
    if i==3:  
      return "three"
    if i==4:  
      return "four"
    if i==5:  
      return "five"
    if i==6:
      return "six"
    if i==7:
      return "seven"
    if i==8:
      return "eight"
    if i==9:
      return "nine"

def numToWords10s(i):
    if (i- (i % 10))/10 == 2:  
      return "twenty"
    if  (i- (i % 10))/10  == 3:
      return "thirty"
    if  (i- (i % 10))/10   == 4:
      return "fourty"
    if  (i- (i % 10))/10  == 5:
      return "fifty"
    if  (i- (i % 10))/10  == 6:
      return "sixty"
    if  (i- (i % 10))/10 == 7:
      return "seventy"
    if  (i- (i % 10))/10  == 8:
      return "eighty"
    if  (i- (i % 10))/10  == 9:
      return "ninety"

def numToWords99(i):
    if i<10:
      return numToWords9(i)
    elif i<20:
      if i==10: 
        return "ten"
      elif i==11:
        return "eleven"
      elif i==12:
        return "twelve"
      elif i==13:
        return "thirteen"
      elif i==14:
        return "fourteen"
      elif i==15:
        return "fifteen"
      elif i==16:
        return "sixteen"
      elif i==17:
        return "seventeen"
      elif i==18:
        return "eighteen"
      else:
        return "nineteen"
    else:
      if i % 10 == 0: 
        return numToWords10s(i)
      else:
        return numToWords10s(i) + "-" + numToWords9(i % 10)
#x=1
#while x < 100:
#    print numToWords99(x)
#    x=x+1  

def numToString(x):
    if x<0:
        return "negative "+numToString(abs(x)) 
    if x==0:
        return "zero"
    else:
        return numToWordsBig(x) 

def numToWords100s(i):
    if (i-(i % 100))/100 == 1:
        return "one hundred"
    if (i- (i % 100))/100 == 2:  
      return "two hundred"
    if  (i- (i % 100))/100 == 3:
      return "three hundred"
    if  (i- (i % 100))/100 == 4:
      return "four hundred"
    if  (i- (i % 100))/100 == 5:
      return "five hundred"
    if  (i- (i % 100))/100 == 6:
      return "six hundred"
    if  (i- (i % 100))/100 == 7:
      return "seven hundred"
    if  (i- (i % 100))/100 == 8:
      return "eight hundred"
    if  (i- (i % 100))/100 == 9:
      return "nine hundred"
#print numToWords100s(234)

def numToWords999(i):
    if i==000:
        return ""
    if i<100:
        return numToWords99(i)
    elif i%100==0:
        return numToWords100s(i)
    else:
        return numToWords100s(i) + " " + numToWords99(i-(i-i%100))
#print numToWords999(100)
#print numToWords999(105)

#y=1
#while y < 1000:
#    print numToString(y)
#    y=y+1  
#print numToString(-123)    

def numToWordsBig(x):
    if x < 1000:
        return numToWords999(x)
    elif x < 1000000:
        return (numToWords999(x/1000)) + " thousand " + (numToWords999(x%1000))
    elif x%1000000==0:
        return (numToWords999(x/1000000)) + " million"
    else:
        return (numToWords999(x/1000000) + " million " + numToWords999((x-(x/1000000 * 1000000)-x%1000)/1000) + " thousand " + numToWords999(x%1000))
print numToWordsBig(123456789)
print numToWordsBig(100020)
print numToWordsBig(100000000)
print numToWordsBig(1000)

y=1
while y < 1000000000:
    numToString(y)
    y=y+1
    
