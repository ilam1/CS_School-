def Bondify(name):
    x=""
    while len(name) > 0:
        if name[0]==" ":
            return name[1:len(name)] + ", " + x + name
        else:
            x= x+ name[0]
            name=name[1:len(name)]
print Bondify("James Kim")
print Bondify("Xiao-Xiao Zhou")

#A. upper(s)
def upper(s):
    x=""
    while len(s) > 0:
        if s[0] >= 'a' and s[0] <= 'z':
            x=x+ chr(ord(s[0]) - 32)
            s=s[1:len(s)]
        else:
            x=x+s[0]
            s=s[1:len(s)]
    return x
print upper('Bing! Wah?')
print upper('upper')

#B. reverse(s)
def reverse(s):
    x=""
    while len(s) > 0:
        x=s[0] + x
        s=s[1:len(s)]
    return x
print reverse('hello')
print reverse('python')

#C. countCharInString(s,c)
def countCharInString(s,c):
    x=0
    while len(s) > 0:
        if s[0] == c:
            x=x+1
            s=s[1:len(s)]
        else:
            s=s[1:len(s)]
    return x
print countCharInString('Bobby Brown', 'b')
print countCharInString('Too Hot To Hoot','o')

#D. makeBoxOfNumbers(rows,cols)
def makeBoxOfNumbers(rows,cols):
    x=""
    z=0
    a=rows
    while a > 0:
        b = cols
        while b > 0:
            x=x+str(z%10)
            z=z+1
            b=b-1
        x=x+"\n"
        a=a-1
    return x
print makeBoxOfNumbers(3,6)
print makeBoxOfNumbers(4,12)

#E. findInString(part,target)
def findInString(part,target):
    x=-1        
    while len(target) > 0:
        if target[0:len(part)] == part:
            return x+1
        else:
            x=x+1
            target=target[1:len(target)]
    return -1
print findInString('bob','Bobby') 
print findInString('bob','bobby') 
print findInString('by','Abbye by bye') 
            
#F. removeFromString(s,c)
def removeFromString(s,c):
    x=""
    while len(s) > 0:
        if c == s[0:len(c)]:
            s=s[len(c):len(s)]
        else:
            x=x+s[0]
            s=s[1:len(s)]
    return x
print removeFromString('Bloop pow woot', 'o')
print removeFromString('ich bin ein holtzfäller', ' ')
