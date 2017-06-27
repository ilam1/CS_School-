public class Test {
    public Test {
	
    public static int ret(int a) {
	return a + 5; }
    public static int[] array(int[] arr) {
	arr[0] = 5;
	return arr;
    }
    public static String arrToString(int[] arr) {
	String ans = "";
	for (int x = 0; x < arr.length; x++) {
	   ans += + arr[x]; }
	return ans;
    }
    
    public static void main(String[] args) {
	//	int b;
	int c = 10;
	//	System.out.println(ret(b));
	System.out.println(c);
	ret(c);
	System.out.println(c);	
	System.out.println(ret(c));
	int[] a = {1,2,3};
	System.out.println(arrToString(a));
	array(a);
	System.out.println(arrToString(a));
	System.out.println(arrToString(array(a)));
    }
}
