/*=============================================
  class Monster -- Represents random incarnations of 
  the adventurer's natural enemy in Ye Olde RPG
  =============================================*/

public class Monster extends Character {

    // ~~~~~~~~~~~ INSTANCE VARIABLES ~~~~~~~~~~~
    // inherited from superclass
    // ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


    /*=============================================
      default constructor
      pre:  instance vars are declared
      post: initializes instance vars.
      =============================================*/
    public Monster() {
	super();
	_hitPts = 150;
	_strength = 20 + (int)( Math.random() * 45 ); // [20,65)
	_defense = 20;
	_attack = 1;
    }


}//end class Monster


/*
-----------------------------------
      -. -. `.  / .-' _.'  _
     .--`. `. `| / __.-- _' `
    '.-.  \  \ |  /   _.' `_
    .-. \  `  || |  .' _.-' `.
  .' _ \ '  -    -'  - ` _.-.
   .' `. %%%%%   | %%%%% _.-.`-
 .' .-. ><(@)> ) ( <(@)>< .-.`.
   (("`(   -   | |   -   )'"))
  / \\#)\    (.(_).)    /(#//\
 ' / ) ((  /   | |   \  )) (`.`.
 .'  (.) \ .md88o88bm. / (.) \)
   / /| / \ `Y88888Y' / \ | \ \
 .' / O  / `.   -   .' \  O \ \\
  / /(O)/ /| `.___.' | \\(O) \
   / / / / |  |   |  |\  \  \ \
   / / // /|  |   |  |  \  \ \  
 _.--/--/'( ) ) ( ) ) )`\-\-\-._
( ( ( ) ( ) ) ( ) ) ( ) ) ) ( ) )
-----------------------------------
 */
