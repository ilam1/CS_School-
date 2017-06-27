//Irene Lam && Lisa Eng
//APCS1 pd05
//HW17 -- Do I repeat myself? Very well, then I repeat myself
//2016-10-17

public class Repeater {
    /*Utilizes the while loop. The method prevents an infinite while loop by subtracting 1 until the answer reaches 1, during which it will return the answer. The method has a base case (for 0) because the neither the answer or while loop involves an empty string.*/
    public static String fenceW(int posts) {
	String ans;
	ans = "|";
	if (posts == 0) {
	    return "";}
	while (posts > 1) {
	    ans += "--|";
	    posts -= 1;
	}	
	return ans;
    }

    //Utilizes recursion by calling fenceR on one less post, which prevents an infinite loop
    public static String fenceR(int posts) {
	String ans;
	ans = "--";
	if (posts == 0) {
	    return "";}
	if (posts == 1) {
	    return "|"; }
	else {
	    return "|" + ans + fenceR(posts - 1);
	}
    }

    //Test cases
    public static void main( String[] args) {
	System.out.println(fenceW(1));
	System.out.println(fenceW(2));
	System.out.println(fenceW(3));
	System.out.println(fenceR(1));
	System.out.println(fenceR(2));
	System.out.println(fenceR(3));
    }
}
