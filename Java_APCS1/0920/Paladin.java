//Team JIM (Jeffrey Weng, Irene Lam, Mark Shafran)
//Irene Lam
//APCS1 pd5
//HW#32: Ye Olde Role Playing Game, Expanded
//2016-11-20

public class Paladin extends Character {
    /* Default constructor
       Precondition: Instance variables declared
       Postcondition: Initializes instance variables of Character (with the exception of name) */
    public Paladin(){
	_hitPts = 125;
	_strength = 100;
	_defense = 50;
	_attack = 0.3;
    }

    /*Overloaded constructor
      Precondition: Instance variable _name declared
      Postcondition: Initializes instance variable _name */    
    public Paladin(String name){
	this();
	_name = name;
    }

    //Paladin's special attack (or defense rather...)
    public void specialize() {
	_attack = 0.65;
	_defense = 25;
    }

    //revert to normal mode
    public void normalize() {
	_attack = .3;
	_defense = 50;
    }
}
