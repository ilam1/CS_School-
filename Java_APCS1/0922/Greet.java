public class Greet { 

    public static void main( String[] args ) { 
 
	String greeting; //declare var of type String to store a greeting

	//instantiate BigSibs
	BigSib richard = new BigSib();    
	BigSib grizz = new BigSib();    
	BigSib dotCom = new BigSib();    
	BigSib tracy = new BigSib();    

	//assign each BigSib's introduction
	richard.setHelloMsg("Word up"); 
	grizz.setHelloMsg("Hey ya"); 
	tracy.setHelloMsg("Salutations"); 
	dotCom.setHelloMsg("Sup"); 

	//set text to be output, then flush to terminal
	greeting = richard.greet("freshman"); 
	System.out.println(greeting); 

	greeting = tracy.greet("Dr. Spaceman"); 
	System.out.println(greeting); 

	greeting = grizz.greet("Kong Fooey"); 
	System.out.println(greeting); 

	greeting = dotCom.greet("mom"); 
	System.out.println(greeting); 

	/**
	 * Q: The statement below does not work. What single, simple, 
	 * small modification in BigSib.java will enable it to work? 
	 **/ 
	System.out.println( richard.helloMsg ); 

    } //end main() 

} //end Greet
