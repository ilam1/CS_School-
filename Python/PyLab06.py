def sumList(L):
    n = 0
    while len(L) > 0:
         n += L[0]
         L = L[1:len(L)]
    return n
print sumList([3,4,10])
print sumList([])

def makeSentence(L):
    string = ''
    if L == []:
        return ''
    while len(L) > 1:
        string = string + L[0] + " "
        L = L[1:len(L)]
    return string + L[0]

##def makeSentence(L):
##    string = ''
##    while len(L) > 0:
##        string += L[0] + ' '
##        L = L[1:]
##    return string[:-1]
#-Patrick Chan

print makeSentence( ['The','rain','in','Spain','falls','mainly']) 
print makeSentence( []) 

def makeListOfSquares(n):
    x = 1
    List = []
    while x <= n:
        List += [x**2]
        x += 1
    return List
print makeListOfSquares(5)
print makeListOfSquares(10)

def makeFibList(n):
    x=[0]
    y=0
    z=1
    if n > 0:
      x.append(1)
    while len(x) < n + 1:
      if len(x)%2==0:
        y += z
        x.append(y)
      else:
        z += y 
        x.append(z)
    return x

print makeFibList(0)
print makeFibList(2)
print makeFibList(5)     
