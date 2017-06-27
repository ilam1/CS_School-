/*****************************************************
 * class LLNode
 * Implements a node, for use in lists and other container classes.
 *****************************************************/

public class LLNode 
{

    private String _cargo;    //cargo may only be of type String
    private LLNode _nextNode; //pointer to next LLNode

    // constructor -- initializes instance vars
    public LLNode( String value, LLNode next ) 
    {

    }


    //--------------v  ACCESSORS  v--------------
    public String getCargo() { return _cargo; }

    public LLNode getNext() { return _nextNode; }
    //--------------^  ACCESSORS  ^--------------


    //--------------v  MUTATORS  v--------------
    public String setCargo( String newCargo ) 
{

    }

    public LLNode setNext( LLNode newNext ) 
{
    }
    //--------------^  MUTATORS  ^--------------


    // override inherited toString
    public String toString() { return _cargo.toString(); }


    //main method for testing
    public static void main( String[] args ) 
{

	/*~~~~s~l~i~d~e~~~m~e~~~d~o~w~n~~~~~~~~~~~~~~~~~~~~ (C-k, C-k, C-y) 
	//Below is an exercise in creating a linked list...

	//Create a node
	LLNode first = new LLNode( "cat", null );

	//Create a new node after the first
	first.setNext( new LLNode( "dog", null ) );

	//Create a third node after the second
	first.getNext().setNext( new LLNode( "cow", null ) );
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/

	/* A naive list traversal:
	while( first != null ) {
	    System.out.println( first );
	    first = first.getNext();
	}
	*/

	//Q: When head ptr moves to next node in list,
	//   what happens to the node it just left?
	}

    }//end main

}//end class LLNode
