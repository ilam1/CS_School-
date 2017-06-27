//Irene Lam
//APCS1 pd5
//HW #26: I Demand Arrays!
//11-02-16

public class ArrayUtils {
	private String test;
    /*Static method that converts arrays to strings
      Precondition: Array composed of integers
      Postconditions: String counterpart of array
     */
    public static String arrToString(int[] arr) {

	String ans = "";
	for (int x = 0; x < arr.length; x += 1) {
	    
	    ans += arr[x];
	}
	return ans;
    }
    /* Static method that makes randomly SINGLE digit integers for the array
       Precondition: Array composed of integers
       Postconditions: Array composed of randomly generated integers
     */
    public static int[] randomarr(int[] arr) {
	for (int x = 0; x < arr.length; x += 1) {
	    arr[x] = (int)(Math.random() * 100)%10;
	}
	return arr;
    }
	
    ArrayUtils[] arr = new ArrayUtils[3];
    public static Object[] randomobj(Object[] arr) {
	for (int x = 0; x < arr.length; x+= 1) {
	    arr[x] = (int)(Math.random() * 100)%10;
	}
	return arr; }

    //Test
    public static void main(String[] args) {
	int [] arr = new int[5];
	System.out.println(arrToString(randomarr(arr)));
	}


}
