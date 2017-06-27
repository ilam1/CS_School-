//Team JIM (Jeffrey Weng, Irene Lam, Mark Shafran)
//Irene Lam
//APCS1 pd5
//HW#32: Ye Olde Role Playing Game, Expanded
//2016-11-20

public class Mage extends Character {
    /* Default constructor
       Precondition: Instance variables declared
       Postcondition: Initializes instance variables of Character (with the exception of name) */
    public Mage(){
	_hitPts = 90;
	_strength = 80;
	_defense = 30;
	_attack = 1;
    }

    /*Overloaded constructor
      Precondition: Instance variable _name declared
      Postcondition: Initializes instance variable _name */    
    public Mage(String name){
	this();
	_name = name;
    }

    //Mage's special attack
    public void specialize() {
	//    	System.out.println(_attack);
	//    	System.out.println(_defense);
	_attack = 1.35;
	_defense = 15;
    }

    //revert to normal mode
    public void normalize() {
	_attack = 1;
	_defense = 30;
    }
}
