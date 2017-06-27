//Team JIM (Jeffrey Weng, Irene Lam, Mark Shafran)
//APCS1 pd5
//HW#32: Ye Olde Role Playing Game, Expanded
//2016-11-20

public class Rogue extends Character {
    /* Default constructor
       Precondition: Instance variables declared
       Postcondition: Initializes instance variables of Character (with the exception of name) */ 
    public Rogue(){
	_hitPts = 100;
	_strength = 90;
	_defense = 20;
	_attack = 1.5;
    }
    
    /*Overloaded constructor
      Precondition: Instance variable _name declared
      Postcondition: Initializes instance variable _name */
    public Rogue(String name){
	this();
	_name = name;
    }

    //Describes the characteristics and stats	
    public String about() {
	    return "Rogues are stealthy. Stats:\nHP: " + _hitPts+"\nStrength: " + _strength+"\nDefense: " + _defense+"\nAttack: " + _attack;
    }
	
    //Rogue's special attack
    public void specialize() {
	_attack = 1.85;
	_defense = 10;
    }

    //revert to normal mode
    public void normalize() {
	_attack = 1.5;
	_defense = 20;
    }
}
