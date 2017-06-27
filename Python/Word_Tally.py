def lowerletters(string):
    x=""
    while len(string) > 0:
        if string[0] == " ":
            x += " "
        if 'a' <= string[0] <= 'z':
            x += string[0] 
        elif 'A' <= string[0] <= 'Z':
            x += chr(ord(string[0]) + 32)
        elif "'" == string[0]:
            x += string[0]
        elif "\n" == string[0]:
            x += " "
        elif "--" == string[0:2]:
            x += " "
        elif "-" == string[0]:
            x += string[0]
        string=string[1:]
    return x
#print lowerletters("a b a c a b fish happy meal fish")
#print lowerletters("""a b a c a b
#     fish    
#happy     meal
#         fish""")
#print lowerletters("""a 
#b a C a b Fish haPpy mEaL 
#fiSH""")
#print lowerletters("""a 
#b a! C a b!!!! "Fish" happy meal. 
#fish?""")
def findword(string):
    x=""
    while len(string) > 0:
        if string[0] == " ":
            return x
        else:
            x += string[0]
        string = string[1:]
    return x
#print findword("a b a c a b fish happy meal fish")

def TallyWords(text):
    words = []
    tally = []
    x=0
    text = lowerletters(text)
    text = text.split()
    while x < len(text):
        y=text[x]
        if words.count(y) == 0:
            words.append(y)
            tally.append(1)
        else:
            tally[words.index(y)] += 1
        x += 1
        #text=text[len(y) + 1:]
        #print words,tally
    return words,tally

#print TallyWords("a b a c a b fish happy meal fish")
#print TallyWords("""a b a c a b
#     fish    
#happy     meal
#         fish""")
#print TallyWords("""a 
#b a C a b Fish haPpy mEaL 
#fiSH""")
#print TallyWords("""a 
#b a! C a b!!!! "Fish" happy meal. 
#fish?""")
#print TallyWords("The great hero bob was the best hero the the.")

def printlist(a,b):
  x=""
  i=0
  while len(a) > i:
    #print str(a[i]) + ":" + str(b[i]) + "\n"
    x += str(a[i]) + ":" + str(b[i]) + "\n"
    i += 1
  return x
#print printlist([1,2,3,4], ["a","b","c","d"])
#print printlist(TallyWords("a b a c a b fish happy meal fish"))
#a=TallyWords("a b a c a b fish happy meal fish")
#print printlist(a[0], a[1])
b=TallyWords("The great hero bob was the best hero the the.")
#print printlist(b[0], b[1])
#print printlist(a)

fileName = 'dante.txt'
f = open(fileName, 'r')
text = f.read()
f.close()
w,t=TallyWords(text)
print printlist(w,t)

