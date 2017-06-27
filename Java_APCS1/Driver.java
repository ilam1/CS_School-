public class Driver {
    public static void main (String [] args) {
	System.out.println(Stats.mean (1, 3)); //Expected result: 2
	System.out.println(Stats.mean (58.4, 5.02)); //Expected result: 31.71
	System.out.println(Stats.max (0, 100)); //Expected result: 100
	System.out.println(Stats.max (1.05, 1.951)); //Expected result: 1.951
	System.out.println(Stats.geoMean (4, 17));//Expected result: 8
	System.out.println(Stats.geoMean (12.54, 78.96)); //Expected result: 31.46678248567 (Produces 31.466782485662556 due to a more precise calculation)
	System.out.println(Stats.max(1,2,3));
    } //Test
}
