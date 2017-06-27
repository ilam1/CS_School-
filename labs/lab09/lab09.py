#!/usr/bin/python
print "content-type: text/html\n"

import random
def oneof(L):
    return L[random.randint(0,len(L)-1)]

def madlibs(storyString, randomnoun, randcolor, randadj, randadv, SubChar, weirdnoun, mainnoun, Char2, sameverb):
    while "randomnoun" in storyString or "randcolor" in storyString or \
          "randadj" in storyString or "randverb" in storyString or \
          "randadv" in storyString:
        storyString = storyString.replace("randomnoun", oneof(randomnoun), 1)
        storyString = storyString.replace("randcolor", oneof(randcolor), 1)
        storyString = storyString.replace("randadj", oneof(randadj), 1)
        storyString = storyString.replace("randverb", oneof(randverb), 1)
        storyString = storyString.replace("randadv", oneof(randadv), 1)
    while "SubChar" in storyString or "mainnoun" in storyString or \
          "weirdnoun" in storyString or "Char2" in storyString or \
          "sameverb" in storyString:
        storyString = storyString.replace("SubChar", oneof(SubChar))
        storyString = storyString.replace("weirdnoun", oneof(weirdnoun))
        storyString = storyString.replace("mainnoun", oneof(mainnoun))
        storyString = storyString.replace("Char2", oneof(Char2))
        storyString = storyString.replace("sameverb", oneof(sameverb))
    return storyString

#x="""Whether 'tis nobler in the NOUN to VERB The NOUNs and NOUNs of ADJECTIVE fortune"""
#nouns=["dog", "cat", "bird", "sheep","pig", "dragon", "snake", "tiger"]
#verbs=["run", "fly", "jog", "eat", "bite", "twist", "kick", "insult"]
#adjectives=["red", "blue", "green", "mean", "dark", "black", "tall", "short"]

#print madlibs(x,nouns,verbs,adjectives)
randomnoun=["cat", "alien", "devil", "duck", "God", "angel", "bacon", "bedroom", "doctor", "king", "villager", "shirt", "wolf", "computer", "bamboo", "note", "nitrogen", "apple", "basket", "tissue", "water", "textbook"]
randcolor=["purple", "blue", "yellow", "pink", "orange", "magenta"]
randadj=["volatile", "bizarre", "proud", "quiet", "truthful", "hush", "lazy", "educate", "mature", "silent", "hideous"]
randverb=["receive", "search", "laugh", "vanish", "delight", "irritate", "destroy", "paint", "dance", "eat", "collect", "educate", "sneeze", "whirl", "dream", "ban", "harm", "rhyme", "wrestle", "flow", "ban", "challenge", "travel", "accept", "explain", "watch", "escape", "groan", "spoil", "scrath"]
randadv=["enormously", "ofensively", "rightfully", "bitterly", "truthfully", "longingly", "physically", "reporachfully", "upliftingly", "deceivingly", "terrifically", "rapidly", "vainly"]
SubChar=["spy", "stew", "staircase", "cattle", "Mr. K", "rifle", "flower", "cone", "scarecrow", "ox", "thunder", "lightnin", "garlic", "gasoline", "Mickey Mouse", "Prince Charming"]
mainnoun=["Evil Queen", "Snow White", "Cinderella", "Donald Duck", "Ariel", "Mulan", "Nemo", "Merida", "Rapunzel", "Belle", "Aurora", "Jasmine"]
weirdnoun=["cabbage", "salad", "potato", "glitter", "bushes", "cookies", "ice cream", "rainbow", "bunny", "pancake", "statue", "unicorn", "pillow", "rain", "suitcase", "hot dog", "circus", "Patrick", "CS Dojo"]
sameverb=["perform", "appreciate", "prick", "drown", "nod", "smell", "rescue", "crawl", "preserve", "sneeze", "wipe", "serve", "crack", "scare", "welcome", "increase", "wail", "murder", "destroy", "choke", "amuse", "command", "count", "surprise"]
Char2=["pig", "dog", "dragon", "cat", "villager", "human", "turkey", "bank", "Stuyvesant", "turtle", "horse", "lightning", "poodle", "bear", "cave", "brownie", "omelette", "trash can", "mountain"]

v=random.randint(0,1)
a=""
if v == 0:
    f = open('The_man_who_never_lied','r').read()
    f = madlibs(f, randomnoun, randcolor, randadj, randadv, SubChar, weirdnoun, mainnoun, Char2, sameverb)
    a="Retelling of <i> The Man Who Never Lied </i>" + f
else:
    f = open('The_Story_of_the_Lightning_and_the_Thunder', 'r').read()
    f = madlibs(f, randomnoun, randcolor, randadj, randadv, SubChar, weirdnoun, mainnoun, Char2, sameverb)
    a="Retelling of <i> The Story of the Lightning and the Thunder </i>" + f

b=random.randint(0,1)
c=""
if b == 0:
    #fileName = 'Who_Was_the_Sinner?'
    f = open('Who_Was_the_Sinner?','r').read()
    f = madlibs(f, randomnoun, randcolor, randadj, randadv, SubChar, weirdnoun, mainnoun, Char2, sameverb) 
    c="Retelling of <i> Who Was the Sinner? </i>" + f
else:
#    fileName = 'The_Magic_Cask'
    f = open('The_Magic_Cask','r').read()
    f = madlibs(f, randomnoun, randcolor, randadj, randadv, SubChar, weirdnoun, mainnoun, Char2, sameverb)
    c="Retelling of <i> The Magic Cask </i>" + f
f = open('The_Princess_and_the_Pea','r').read()
f = madlibs(f, randomnoun, randcolor, randadj, randadv, SubChar, weirdnoun, mainnoun, Char2, sameverb)
d="Retelling of <i> The Princess and the Pea </i>" + f

def html():
    ans = """<!DOCTYPE html> \n <html> \n <head> \n <title> Fairytales and Fables </title> \n <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js"></script>
  <script src="https://ajax.googleapis.com/ajax/libs/webfont/1.4.7/webfont.js"></script>
<script>
      WebFont.load({
      google: {
      families: ["Lato:100,300,400,700,900","Karla:regular","Cookie:regular"]
    }
    });
</script>
  <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script> 
 <style>"""
    ans += "\n body { background-image: url(\"http://www.intrawallpaper.com/static/images/518164-backgrounds.jpg\")}"
    ans += """  h2 {
    color: Yellow;
    text-align: center;
    font-family: "Cookie";
    font-size: 90px;
    }
    p {
    color: Black;
    text-align: left;
    font-family: "Calibri";
    font-size: 15px;
    }"""
    ans += "  img.displayed {    display: block;    margin-left: auto;    margin-right: auto;  width: 1200px }"
    ans += " img.displaying {display:block; margin-left: auto; margin-right: auto; width: 80px; height: auto; vertical-align:bottom; }"
    ans += "</style> \n </head> \n <body> \n"
    ans += "<img class='displayed' src='http://www.kidsgen.com/fables_and_fairytales/img/fable-and-fairytale.png'/>"
    ans += """<div class="container">
  <ul class="list-inline nav nav-pills">
    <li><a data-toggle="pill" href="#African">African Folktales</a></li>
    <li> <a data-toggle="pill" href="#Asian">Asian Folktales</a></li>
    <li> <a data-toggle="pill" href="#European">European Fairytales</a></li>
  </ul>
  <div class="tab-content">
   <div id="African" class="tab-pane fade in active">
    <h2>African Folktales</h2>
    """ + a + """
    <br><br>
    <img class='displaying' src='http://static.tumblr.com/1613d25b69aa8c1e62f1b3963b26899a/h7biwlp/wFknyg5ko/tumblr_static_7dka9qx8hs000cg4448k0wk4c.png'/>
    </div>
    <div id="Asian" class="tab-pane fade">
    <h2>Asian Folktales</h2>
    """ + c + """
    <br> <br>
    <img class='displaying' src='http://static.tumblr.com/1613d25b69aa8c1e62f1b3963b26899a/h7biwlp/wFknyg5ko/tumblr_static_7dka9qx8hs000cg4448k0wk4c.png'/>
    </div>
    <div id="European" class="tab-pane fade">
    <h2>European Fairytales</h2>""" + d + """
    <br> <br>
    <img class='displaying' src='http://static.tumblr.com/1613d25b69aa8c1e62f1b3963b26899a/h7biwlp/wFknyg5ko/tumblr_static_7dka9qx8hs000cg4448k0wk4c.png'/>
    </div>"""
    ans += "\n </body> \n </html>"
    return ans
    
print html()
