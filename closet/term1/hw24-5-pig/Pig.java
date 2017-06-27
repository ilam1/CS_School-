//class Pig
//a Pig Latin translator
//SKELETON

/*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
           9
     ,--.-'-,--.
     \  /-~-\  /
    / )' a a `( \
   ( (  ,---.  ) )
    \ `(_o_o_)' /
     \   `-'   /
      | |---| |     
      [_]   [_]
      PROTIP: Make this class compilable first, 
      then develop and test one method at a time.
      NEVER STRAY TOO FAR FROM COMPILABILITY/RUNNABILITY!
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/

public class Pig 
{
    //Q: How does this initialization make your life easier?
    private static final String VOWELS = "aeiou";


    /*=====================================
      boolean hasA(String,String) -- checks for a letter in a String
      pre:  w != null, letter.length() == 1
      post: hasA("cat", "a") → true  
      hasA("cat", "p") → false
      =====================================*/
    public static boolean hasA( String w, String letter ) 
    {
	/* YOUR IMPLEMENTATION HERE */
    }//end hasA()


    /*=====================================
      boolean isAVowel(String) -- tells whether a letter is a vowel
      precondition: letter.length() == 1
      =====================================*/
    public static boolean isAVowel( String letter ) 
    {
	/* YOUR IMPLEMENTATION HERE */
    }


    /*=====================================
      int countVowels(String) -- counts vowels in a String
      pre:  w != null
      post: countVowels("meatball") → 3
      =====================================*/
    public static int countVowels( String w ) 
    {
	/* YOUR IMPLEMENTATION HERE */
    }


    /*=====================================
      boolean hasAVowel(String) -- tells whether a String has a vowel
      pre:  w != null
      post: hasAVowel("cat") → true
      hasAVowel("zzz") → false
      =====================================*/
    public static boolean hasAVowel( String w ) 
    {
	/* YOUR IMPLEMENTATION HERE */
    }


    /*=====================================
      String allVowels(String) -- returns vowels in a String
      pre:  w != null
      post: allVowels("meatball") → "eaa"
      =====================================*/
    public static String allVowels( String w ) 
    {
	/* YOUR IMPLEMENTATION HERE */
    }


    /*=====================================
      String firstVowel(String) -- returns first vowel in a String
      pre:  w != null
      post: firstVowel("") --> ""
      firstVowel("zzz") --> ""
      firstVowel("meatball") --> "e"
      =====================================*/
    public static String firstVowel( String w ) 
    {
	/* YOUR IMPLEMENTATION HERE */
    }


    /*=====================================
      boolean beginsWithVowel(String) -- tells whether a String begins with a vowel
      pre:  w != null and w.length() > 0
      post: beginsWithVowel("apple")  --> true
      beginsWithVowel("strong") --> false
      =====================================*/
    public static boolean beginsWithVowel( String w ) 
    {
	/* YOUR IMPLEMENTATION HERE */
    }


    /*=====================================
      String engToPig(String) -- converts an English word to Pig Latin
      pre:  w.length() > 0
      post: engToPig("apple")  --> "appleway"
      engToPig("strong") --> "ongstray"
      engToPig("java")   --> "avajay"
      =====================================*/
    public static String engToPig( String w ) 
    {
	/* YOUR IMPLEMENTATION HERE */
    }


    public static void main( String[] args ) {

	/* YOUR TEST CALLS HERE */
	
    }//end main()

}//end class Pig


