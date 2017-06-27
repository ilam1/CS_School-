#!/usr/bin/python
print "content-type: text/html\n"

import cgitb,hashlib,cgi
cgitb.enable()
import Cookie,os

form=cgi.FieldStorage()
f = open("data/users.txt","r")
users = f.read().split('\n')
#users.remove([''])
f.close()
username = " "
#D08BE5
print '''<style>
body {
     background-color: #33CCCC;
     background-image: url("pictures/toasty.png");
     background-repeat: no-repeat;
     background-attachment: fixed;
     background-position: top right;

     margin:0;
     padding:0;
  }
</style>'''



def createCookie(c,username,ID):
    c['username']=username
    c['ID']=ID
    c['username']['expires']=USER_EXPIRE_TIME
    c['ID']['expires']=PASSWORD_EXPIRE_TIME

if 'username' in form and 'password' in form: 
    username = form.getvalue('username')
    password = form.getvalue('password')
    if authenticate(username,password):
        import os,random
        IP = os.environ['REMOTE_ADDR']
        ID = random.randint(1000000,9999000)

        #print some debug info at the top of the page:
        #body += "Success!<br>"
        #body += "Random Number: "+str(ID)+"<br>"
        #body += "IP: "+ IP + "<br>"

        #write to a file
        writeOrReplace('data/loggedin.txt',username,ID,IP)

        #create a cookie:
        createCookie(c,username,ID)
        ##debug statements
        #body+= "cookie created<br>"
        #for each in c:
        #	body+= each+":"+c[each].value+"<br>"

        #attach a link:
        #head += '<meta http-equiv="refresh" content="0; url=stuymap.html?username=' + form.getvalue("username") + '">' 
        #body+='<a href="mainpage.py?username=' + username + '">Go To Main Page</a><br>'
    else:
	if 'username' in form and 'password' in form:
	    username = form.getvalue('username')
	    password = form.getvalue('password')
	    if authenticate(username,password):
        	import os,random
	        IP = os.environ['REMOTE_ADDR']
        	ID = random.randint(1000000,9999000)
		writeOrReplace('data/loggedin.txt',username,ID,IP)
		createCookie(c,username,ID)
	else:
	        body += "Failed to authenticate >.< <br> Please log back in"
		body += '''<br> <a href="createaccount.py">Create a new Account</a>'''
else:
    body = '''<h1>Log in:</h1>
    <form action="login.py">
    Username: <input type="text" name="username"><br>
    Password: <input type="password" name="password"><br>
    <input type="submit" value="log in">
    '''

def faction(username):
    f = open("data/users.txt","r")
    text = f.read().split("\n")
    f.close()
    for each in text:
	if (username + ",") in each:
	    if each.split(",")[2] == "Abnegation" or each.split(",")[2] == "Amity" or each.split(",")[2] == "Candor" or each.split(",")[2] == "Dauntless" or each.split(",")[2] == "Erudite":
		return True
    return False

def test():
    ans = "<!DOCTYPE html>"
    ans += '''<html>
<head>
 <title> Stuy Map </title>
 <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css">
  <link rel="stylesheet" href="path/to/balloon.min.css">
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
<style>
  body {
     background-color: #70dbdb;
     background-image: url("pictures/toasty2.png");
     background-repeat: no-repeat;
     background-attachment: fixed;
     background-position: top right;

     margin:0;
     padding:0;
  }
  h1 { 
    color: Yellow;
    text-align: left;
    font-family: "Cookie";
    font-size: 80px;
  }
  h2 {
    color: #FFF763;
    text-align: center;
    font-family: "Verdana";
    font-size: 35px;
  }
  h3 {
    color: Blue;
    text-align: center;
    font-family: "Verdana";
    font-size: 30px;
  }
  p  {
    color: blue;
    text-align: left;
    font-family: "Times New Roman";
    font-size: 20px;
  }
  tr:hover {
    background-color: #F5F5F5
  }
  td {
    color: black;
    text-align: center;
    font-family: "Nyala";
    font-size: 20px;
  }
  table.center {
    margin-left:auto;
    margin-right:auto;
  }
  img.displayed {
    display: blcok;
    margin-left: auto;
    margin-right: auto;
  }
  .resize {
    width: 400px;
    height: 200px;
  }
  .resizelarge {
    width: 300px;
    height: 200px;
  }
  .resizelarger {
    width: 700px;
    height: auto;
    vertical-align:bottom;
  }
  p.groove {
    border-color: purple;
    
    border-style: groove;
    border-width: 10px;
    padding-top: 20px;
    padding-right: 20px;
    padding-bottom: 20px;
    padding-left: 20px;
  }
  
  ul.img-list {
    list-style-type: none;
    margin: 0;
    padding: 0;
    text-align: center;
  }

  ul.img-list li {
    display: inline-block;
    height: 200px;
    margin: 0 1em 1em 0;
    position: relative;
    width: 400px;
  }
  span.text-content {
    background: rgba(0,0,0,0.5);
    color: pink;
    cursor: pointer;
    display: table;
    height: 200px;
    left: 0;
    position: absolute;
    top: 0;
    width: 400px;
    opacity: 0;
  }
  span.text-contentresize {
    background: rgba(0,0,0,0.5);
    color: white;
    cursor: pointer;
    display: table;
    height: 200px;
    left: 0;
    position: absolute;
    top: 0;
    width: 400px;
    opacity: 0;
  }
  span.text-contentresize span {
    display: table-cell;
    text-align: center;
    vertical-align: middle;
  }


  ul.img-list li:hover span.text-content {
    opacity: 1;
  }  

  span.text-content span {
    display: table-cell;
    text-align: center;
    vertical-align: middle;
  }
</style>
</head>
<body>
 <div class="container">'''
    if "username" not in form:
	ans += '''<p style="text-align:right"> <a href="createaccount.py">Create Account</a> <b>|</ba> <a href="login.py">Login</a>'''
    else:       
	if faction(form.getvalue("username")) != True:
	    ans += '''<p style="text-align:right"> <a href="test1.py?username='''+ form.getvalue('username') + '''">Take The Aptitude Test</a> <b>| </b>'''
    	    ans += '''<a href="logOut.py">Log Out</a></p>'''
	else:
            ans += '''<p style="text-align:right"> <a href="blog.py?username='''+form.getvalue('username')+'''">See your faction's blog!</a> <b>| </b>'''
	    ans += '''<a href="profile.py?username='''+form.getvalue('username')+'''">Profile</a> <b>| </b>'''
	    ans += '''<a href="test2.py?username='''+ form.getvalue('username') + '''">Take The Compatibility Test!!</a> <b>| </b>'''
            ans += '''<a href="logOut.py">Log Out</a></p>'''
    ans += ''' <h1> Welcome to the <i> Divergentized </i> Stuyvesant </h1>
  <ul class="list-inline nav nav-pills">
    <li> <a data-toggle="pill" href="#first">First </a></li>
    <li> <a data-toggle="pill" href="#second">Second </a></li>
    <li> <a data-toggle="pill" href="#third">Third </a></li>
    <li> <a data-toggle="pill" href="#fourth">Fourth </a></li>
    <li> <a data-toggle="pill" href="#fifth">Fifth </a></li>
    <li> <a data-toggle="pill" href="#sixth">Sixth </a></li>
    <li> <a data-toggle="pill" href="#seventh">Seventh </a></li>
    <li> <a data-toggle="pill" href="#eigth">Eigth </a></li>
    <li> <a data-toggle="pill" href="#ninth">Ninth </a></li>
    <li> <a data-toggle="pill" href="#tenth">Tenth </a></li>
    <li> <a data-toggle="pill" href="#eleventh">Eleventh </a></li>
  </ul>
  <div class="tab-content">
   <div id="zero" class="tab-pane fade in active">
	<br>
	<br>
    <h1><center>Read Me:</center></h1>
    <p style="text-align:center">Welcome to the Divergentized Stuyvesant!  Here, you will be assigned into a faction and will be able to explore the many areas of Stuyvesant through the eyes of a factioned society! To get started, simply create an account (top right)  and login. From there, you are to take an Aptitude Test, which will permanently determine your faction or if you're divergent, re divergent, you will choose one faction among the many you show aptitude for), so choose your answers wisely!</p>
    <p style="text-align:center">But the journey doesn't end yet. Want to chat with other people from your faction? Then enter your faction's blog where you can post and reply to comments! Want to view another account's profile? Simply click their name on the blog to see it! Want to check out/ customize your personal information? Then click on your profile where you not only see several of your features (i.e. name, faction) but can also update your own description! Curious about your compatibility with your/ other factions? Take the Compatibility Test! Check the boxes you want to check your compatibility for, and optionally change the total number of questions you want to take, and the test will give you your personalized test!</p>
    <p style="text-align:center">Of course, there's no purpose of a faction without a place to call home. Hence, check out the Stuyvesant map (which can be viewed whether you log in or not)! The pill tabs on top represent the floors of Stuyvesant, and the pictures represent separate areas located on their respective floors. Hover over the image to view their description along with information regarding which faction currently dominates each place.</p>
    <p style="text-align:center">Enjoy your adventure, and may you have more fun touring the site than we did coding it!</p>
	<br>
   </div>

   <div id="first" class="tab-pane fade">
   <h2>First Floor</h2>
	<br>
   <ul class="img-list">
        <li> <img class="resize" src="pictures/auditorium.jpg"/>
                <span class="text-content"><span>Auditorium<br>Place of acting, home of Amity</span></span>
        </li>
        <li> <img class="resize" src="pictures/pool.jpg"/>
             <span class="text-content"><span>Swimming pool<br>Just keep going, Just keep going <br> Dauntless </span></span>
        </li>
   </div>

   <div id="second" class="tab-pane fade">
   <h2>Second Floor</h2>
	<br>
   <ul class="img-list">
	<li> <img class="resize" src="pictures/bridge.jpg"/>
        	<span class="text-content"><span>Bridge Entrance<br>We welcome all factions!<br>(aka if you have not taken the Aptitude Test yet, you're Factionless, so take the test!)</span></span>
        </li>
        <li> <img class="resize" src="pictures/counselors.jpg"/>
             <span class="text-content"><span>Guidance Counselors <br>Selfless and giving, Abnegation of course</span></span>
	</li>
	<br>
	<li> <img class="resize" src="pictures/store.jpg"/>
             <span class="text-content"><span>School Store<br>Candor - You get what you see</span></span>
        </li>

   </div>
  
   <div id="third" class="tab-pane fade">
    <h2>Third Floor</h2>
        <br>
   <ul class="img-list">
        <li> <img class="resize" src="pictures/apush.gif"/>
                <span class="text-content"><span>US History<br>History of interfaction war<br>Erudite</span></span>
        </li>
        <li> <img class="resize" src="pictures/european.jpg"/>
             <span class="text-content"><span>European History<br>Intrafaction studies<br>Erudite</span></span>
        </li>
		<br>

	<li> <img class="resize" src="pictures/geopolitics.jpg"/>
                <span class="text-content"><span>GeoPolitics<br>Global Inter[f]actions<br>Erudite</span></span>
        </li>
                <br>

	<li> <img class="resize" src="pictures/jewish.jpg"/>
                <span class="text-content"><span>Jewish History<br>Faction disapora, culture, and history<br>Erudite</span></span>
        </li>
        <li> <img class="resize" src="pictures/world.jpg"/>
             <span class="text-content"><span>World History<br>Factions 101<br>Erudite</span></span>
        </li>
        <li> <img class="resize" src="pictures/cry.gif"/>
             <span class="text-content"><span> Computer Science<br>Dauntless-It takes courage to take comp sci<br>Sink or swim</span></span>
        </li>
                <br>
	
   </div>
  
   <div id="fourth" class="tab-pane fade">
    <h2>Fourth Floor</h2>

   <ul class="img-list">
        <li> <img class="resize" src="pictures/algebra.jpg"/>
                <span class="text-content"><span>Algebra<br>Erudite</span></span>
        </li>
        <li> <img class="resize" src="pictures/geometry.jpg"/>
             <span class="text-content"><span>Geometry<br>Erudite</span></span>
        </li>
        
		<h3>MATH</h3>
	<br><br>
        <li> <img class="resize" src="pictures/trigonometry.jpg"/>
             <span class="text-content"><span>Trigonometry<br>Erudite</span></span>
        </li>
	<li> <img class="resize" src="pictures/calculus.jpg"/>
             <span class="text-content"><span>Calculus<br>Erudite</span></span>
        </li>

   </div>
  
   <div id="fifth" class="tab-pane fade">
    <h2>Fifth Floor</h2>
	<ul class="img-list">
        <li> <img class="resize" src="pictures/cafeteria.jpg"/>
                <span class="text-content"><span>Cafeteria<br>Food makes people happy<br>-Amity</span></span>
        </li>
        <li> <img class="resize" src="pictures/gym.jpg"/>
             <span class="text-content"><span>Gym<br>Dauntless</span></span>
        </li>


   </div>
  
   <div id="sixth" class="tab-pane fade">
    <h2>Sixth Floor</h2>
	<ul class="img-list">
        <li> <img class="resize" src="pictures/library.jpg"/>
                <span class="text-content"><span>Library<br>Manned by Candor, frequented by Erudite</span></span>
        </li>
        <li> <img class="resize" src="pictures/engDept.jpg"/>
             <span class="text-content"><span>English<br>Erudite through and through</span></span>
        </li>
	<br>
	<li> <img class="resize" src="pictures/speech.jpg"/>
             <span class="text-content"><span>Speech and Debate<br>DAUNTLESS</span></span>
        </li>

   </div>
  
   <div id="seventh" class="tab-pane fade">
    <h2>Seventh Floor</h2>
	<ul class="img-list">
        <li> <img class="resize" src="pictures/bio.jpg"/>
                <span class="text-content"><span>Biology<br>Erudite</span></span>
        </li>
        <li> <img class="resize" src="pictures/biolab.jpg"/>
             <span class="text-content"><span>Biology Lab<br>Erudite</span></span>
        </li>

   </div>
  
   <div id="eigth" class="tab-pane fade">
    <h2>Eigth Floor</h2>
        <ul class="img-list">
        <li> <img class="resize" src="pictures/gas-laws.gif"/>
                <span class="text-content"><span>Physics<br>Erudite</span></span>
        </li>
        <li> <img class="resize" src="pictures/physicsLab.jpg"/>
             <span class="text-content"><span>Physics Lab<br>Erudite</span></span>
        </li>

   </div>
  
   <div id="ninth" class="tab-pane fade">
    <h2>Ninth Floor</h2>
        <ul class="img-list">
        <li> <img class="resize" src="pictures/atom.gif"/>
                <span class="text-content"><span>Chemistry<br>Erudite</span></span>
        </li>
        <li> <img class="resize" src="pictures/chemLab.jpg"/>
             <span class="text-content"><span>Chemistry Lab<br>Erudite</span></span>
        </li>

   </div>
  
   <div id="tenth" class="tab-pane fade">
    <h2>Tenth Floor</h2>
        <ul class="img-list">
        <li> <img class="resize" src="pictures/art.jpg"/>
                <span class="text-content"><span>Art<br>Pastels and Michelangelo</span></span>
        </li>
        <li> <img class="resize" src="pictures/art2.jpg"/>
             <span class="text-content"><span>Appreciation<br>Amity</span></span>
        </li>

   </div>
  
   <div id="eleventh" class="tab-pane fade">
    <h2>Eleventh Floor</h2>
	<center><img class="resizelarger" src="pictures/waterPark2.jpg"/></center>
        <h3>Swimming Pool</h3>
        

   </div>
 </div>
</body>
</html>
'''
    return ans

	#print body
print test()
