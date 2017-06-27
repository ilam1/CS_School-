/*public class check {
    public static void main( String[] args) {
	String s1 = "foo";
	String s2 = "foo";
	String s3 = new String("foo");
	System.out.println(s1);
	System.out.println(s2);
	System.out.println(s3);
	System.out.println(s1 == s2);
	System.out.println(s1 == s3);
	System.out.println(s1.equals(s2));
	System.out.println(s1.equals(s3));
    }
}
*/
/*
public class check {
    public static void main (String[] args) {
	//	int i1 = 120;
	//	double d1;
	//	d1 = i1;
	//       System.out.println( d1);
		int i2;
		double d2 = 3.8644f;
		//		System.out.println( d2);
		i2 = d2;
    }
}
*/

//10-17
public class check {
    public static String countDown(int n) {
	for (int test = n; test > 0; test -= 1) {
	    System.out.println(test);
	}
	return "Success!";
    }
    public static String arrToString(int[] arr) {

	String ans = "";
	for (int x = 0; x < arr.length; x += 1) {
	    
	    ans += arr[x];
	}
	return ans;
    }
    public static void main(String[] args) {
	/*	System.out.println( -9 % 5);
	System.out.println( -3 % 9);
	System.out.println( 3 % -8);
	System.out.println(-9 % -3);
	System.out.println( -3 % -9);
	System.out.println("hi".length());
	System.out.println("q  q".length());
	System.out.println("Hello".substring(2));
	System.out.println("Hello".substring(2,4));
	System.out.println(countDown(5));
	System.out.println("bar".substring(0,2));
	System.out.println("bar".substring(0,3));
	//	System.out.println("bar".substring(0,4));
	System.out.println("bar".substring(1,2));
	System.out.println("bar".substring(1,1));
	System.out.println("bar".substring(1)); */
	//	for (String s : args) {
	//    System.out.println(s) ;
	//	}
	/*	int[] arr = new int[3];
	arr[1]= 3;
	String ans = "";
	for (int x = 1; x < arr.length; x += 1) {
	    ans += "" + arr[x];}
	    
	    System.out.println(ans);*/
	int [] data = {1,2,3,4,5,6};
	data[0]=3;
	System.out.println(arrToString(data));
	int i = 0;
	int x = 0;
	x = ++i + 3;
	System.out.println(i);	
	System.out.println(x);	



    }
}
