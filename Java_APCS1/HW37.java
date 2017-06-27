public class HW37 {
    public static String arrToString(int[][] arr) {

	String ans = "";
	for (int x = 0; x < arr.length; x += 1) {
	    
	    int a = 1;
	    ans += arr[x][a];
	}
	return ans;
    }

    public static void main(String[] args) {
	int[][] a2 = new int[4][5];
	int x = 0;
	for (int a=0; a < a2.length; a++) {
	    for (int i=0; i < a2[a].length; i++) {
		a2[a][i] = x;
		x++;
		System.out.print(a2[a][i] + " ");
	    }
	    System.out.print("\n");
	}

	//	System.out.println(arrToString(a2));
    }
}
