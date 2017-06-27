//Team JIM (Jeffrey Weng, Irene Lam, Mark Shafran)
//APCS1 pd5
//HW#32: Ye Olde Role Playing Game, Expanded
//2016-11-20

public class Ranger extends Character {
    /* Default constructor
       Precondition: Instance variables declared
       Postcondition: Initializes instance variables of Character (with the exception of name) */    
    public Ranger(){
	_hitPts = 130;
	_strength = 80;
	_defense = 30;
	_attack = 0.4;
    }

    /*Overloaded constructor
      Precondition: Instance variable _name declared
      Postcondition: Initializes instance variable _name */    
    public Ranger(String name){
	this();
	_name = name;
    }

    //Ranger's special attack
    public void specialize() {
	_attack = .75;
	_defense = 15;
    }

    //revert to normal mode
    public void normalize() {
	_attack = .4;
	_defense = 30;
    }
}
