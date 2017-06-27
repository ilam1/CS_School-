//Irene Lam
//APCS1 pd5
//HW14 - stAtistically sPeaking
//10-06-16

public class Stats {
    public static int mean(int a, int b) {
	return (a+b)/2;
    } //Computes the mean by adding the numbers and dividing by 2
    
    public static double mean(double a, double b) {
	return (a+b)/2;
    } //Doesn't lose precision, therefore same expression is sufficient
    
    public static int max(int a, int b) {
	if (a > b) {
	    return a; }
	else {
	    return b; }
    } //If a is greater than b, a is the only maximum and should be returned. If a is equal to or less than b, then b is either the only max or the same as b, both of which can be seen by just b.
    
    public static double max(double a, double b) {
	if (a > b) {
	    return a; }
	else {
	    return b; }
    } // Doesn't lose precision, therefore same boolean expression is sufficient
    
    public static int geoMean(int a, int b) {
	return (int) Math.sqrt(a*b);
    } //Loses precision without (int) because Math.sqrt() produces a long (64 bits) whereas int is only 32 bits. Thus (int) forces Math.sqrt() to become an int, bypassing the precision error and thus returning an integer geometric mean.
    
    public static double geoMean(double a, double b) {
	return Math.sqrt(a*b);
    } // Does not lose precision (because this returns a double and not an integer), thus the expression without something like (double) works.
    public static int max(int a, int b, int c) {
	if ((a > b && a > c) || (a > b && a == c) || (a > c && a == b) || (a == b && a == c)) {
	    return a;
	}
	if ((b > a && b > c) || (b > a && b == c)) {
	    return b;
	}
	else {
	    return c; }
    }
    public static double max(double a, double b, double c) {
	if ((a > b && a > c) || (a > b && a == c) || (a > c && a == b) || (a == b && a == c)) {
	    return a;
	}
	if ((b > a && b > c) || (b > a && b == c)) {
	    return b;
	}
	else {
	    return c; }
    }	    
}
