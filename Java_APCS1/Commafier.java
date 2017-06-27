public class Commafier {
    public static String commafyR (int num) {
        String x = String.parseStr(num);
	if (x.length() <= 3) {
	    return x; }
	return x.substring(x.length(), x.length()-3) + "," + commafyR(Integer.parseInt(x.substring(0,x.length()-3)));
    }

    public static void main(String[] args){
	System.out.println(commafyR(1));
	System.out.println(commafyR(10));
	System.out.println(commafyR(100));
	System.out.println(commafyR(1000));
	System.out.println(commafyR(12345));



    }
}
