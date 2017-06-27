/*****************************************************
 * class LLQueue
 * uses a singly-linked nodes to implement a QUEUE
 * (a collection with FIFO property)
 *
 *       -------------------------------
 *   end |  --->   Q U E U E   --->    | front
 *       -------------------------------
 *
 ******************************************************/

//import java.util.NoSuchElementException;
//import java.lang.RuntimeException;

public class LLQueue<T> implements Queue<T> 
{
    private LLNode<T> _front, _end;

    // default constructor creates an empty queue
    public LLQueue()
	{ 

	}

    // means of adding a thing to the collection
    public void enqueue( T enQVal ) 
    {

    }//O(?)


    // means of removing a thing from the collection
    // remove and return thing at front of queue
    // assume _queue ! empty
    public T dequeue() 
    { 

    }//O(?)


    // means of peeking at thing next in line for removal
    public T peekFront() 
    {

    }//O(?)


    public boolean isEmpty() 
    {

    }//O(?)


    // print each node, separated by spaces
    public String toString() 
    { 

    }//O(?)



    public static void main( String[] args ) {

	/*v~~~~~~~~~~~~~~MAKE MORE~~~~~~~~~~~~~~v
	  Queue<String> LLQueuelJ = new LLQueue<String>();

	  System.out.println("\nnow enqueuing thrice..."); 
	  LLQueuelJ.enqueue("James");
	  LLQueuelJ.enqueue("Todd");
	  LLQueuelJ.enqueue("Smith");

	  System.out.println("\nnow testing toString()..."); 
	  System.out.println( LLQueuelJ ); //for testing toString()...

	  System.out.println("\nnow dequeuing thrice..."); 
	  System.out.println( LLQueuelJ.dequeue() );
	  System.out.println( LLQueuelJ.dequeue() );
	  System.out.println( LLQueuelJ.dequeue() );

	  System.out.println("\nDequeuing from empty queue should yield error..."); 
	  System.out.println( LLQueuelJ.dequeue() );
	  ^~~~~~~~~~~~~~~~AWESOME~~~~~~~~~~~~~~~^*/

    }//end main

}//end class LLQueue
