//Irene Lam
//APCS1 pd5
//HW#37 -- Be More Rational
//2016-12-01

//Java class used to represent rational numbers
public class Rational { 
    //Initializing instance variables
    private int numerator;
    private int denominator;

    /*Default constructor
      Precondition: 
      Postcondition: new Rational with value 0/1 */
    public Rational() {
	numerator = 0;
	denominator = 1;
    }

    /*Overloaded constructor
      Precondition: Two integer parameters 
      Postcondition: Assigns number to numerator and denominator based on the parameter, unless it is undefined, which changes to numerator and denominator to 0 and 1 respectively */
    public Rational(int num, int den) {
	if (den == 0) {
	    System.out.println("Invalid Denominator"); //States the error
	    numerator = 0;
	    denominator = 1; }
	numerator = num;
	denominator = den; }

    /* toString
       Precondition:
       Postcondition: Produces a string representation of the number */
    public String toString() {
	return "" + numerator + "/" + denominator; }

    /* Returns a floating point value of the number
       Precondition:
       Postcondition: Produces a double representation of the rational number */
    public double floatValue() {
	return (double) numerator/denominator;
    }

    /* Multiplies the fractional numerator and denominator  by this Rational object
       Precondition: a Rational object
       Postcondition: Fractional numerator annd denominator multiplied by the parameter object */
    public void multiply (Rational rat) {
	numerator *= rat.numerator;
	denominator *= rat.denominator;
    }

    /*Multiplies the fractional numerator and denominator by the reciprocal of rat
      Precondition: a Rational object
      Postcondition: Fractional numerator and denominator divided by the parameter object */
    public void divide (Rational rat) {
	numerator *= rat.denominator;
	denominator *= rat.numerator; }

    /* Adds this rational object by the rational object
      Precondition: a Rational object
      Postcondition: Sum of the Rational object and parameter */
    public void add (Rational rat) {
	numerator = numerator*rat.denominator + denominator*rat.numerator;
	denominator = rat.denominator*denominator; }

    /* Subtracts this rational object by the rational object
      Precondition: a Rational object
      Postcondition: Difference of the Rational object and parameter */
    public void subtract (Rational rat) {
	numerator = numerator*rat.denominator - denominator*rat.numerator;
	denominator = rat.denominator*denominator; }

    //Brute-force approach, where a number increment is added by 1 until it reaches the minimum of a and b, during which answer is updated if the increment is divisible by both a and b. Answer is returned when increment stops incrementing.
    public  int gcd() {
	int increment = 1;
	int answer = 1;
	while (increment <= numerator && increment <= denominator) {
	    if (numerator%increment == 0 && denominator%increment == 0) {
		answer = increment;
		increment += 1;
	    }
	    else {
		increment += 1;}
	}
	return answer;
    }

    public void reduce() {
	numerator /= this.gcd();
	denominator /= this.gcd(); }

    //GCD Recursive, where the method is called continuously on b and the remainder of a and b until their remainder is 0
    public static int gcdER(int a, int b) {
	int temp = 0;
	if (a < b ) {
	    temp = a;
	    a = b;
	    b = temp;
	}
	if (a%b == 0) {
	    return b; }
	return gcdER(b, a%b);
    }

    /* compareTo: Compares a Rational object to the calling object
       Precondition: Takes a Rational object
       Postcondition: Returns 0 if equal, -1 if the calling object is smaller than the rational object, and 1 if the calling object is larger than the rational object*/
    public int compareTo(Rational rat) {
	if ((double)rat.numerator/rat.denominator > (double)numerator/denominator) {
	    return 1; }
	if (rat.numerator/rat.denominator == numerator/denominator) {
	    return 0; }
	else {
	    return -1; }
    }

    //Test
    public static void main(String[] args) {
	Rational r = new Rational(2,3); //Stores the rational number 2/3
	System.out.println(r.toString());
	Rational s = new Rational(1,2); //Stores the rational number 1/2
	System.out.println(s.toString());
	r.multiply(s); //Multiplies r by s, changes r to 2/6.  s remains 1/2
	System.out.println(r.toString());
	System.out.println(s.toString());
	Rational t = new Rational(2,3); //Stores the rational number 2/3
	Rational u = new Rational(1,2); //Stores the rational number 1/2
	t.divide(u); //Divides r by s, changes r to 2/1
	System.out.println(t.toString());
	Rational a = new Rational(2,3); //Stores the rational number 2/3
	Rational b = new Rational(1,2); //Stores the rational number 1/2
	Rational c = new Rational(4,18); //Stores the rational number 4/18
	a.add(b);  //Adds a to b, changes a to 7/6.  b remains 1/2
	System.out.println(a.toString());
	c.reduce(); //Changes c to 2/9
	System.out.println(c.toString());
	Rational d = new Rational(2,9);
	System.out.println(c.compareTo(d)); //Ans: 0
	Rational e = new Rational(4,18);
	System.out.println(c.compareTo(e)); //Ans: 0
	System.out.println(a.compareTo(e)); //Ans: -1
	System.out.println(e.compareTo(b)); //Ans: 1
    }

}
