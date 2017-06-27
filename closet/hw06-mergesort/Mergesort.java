/*======================================
  class MergeSort
  Implements mergesort on array of ints.

  Summary of Algorithm: 

  ======================================*/

public class Mergesort {

   /******************************************************
     * int[] merge(int[],int[]) 
     * Merges two input arrays
     * Precond:  Input arrays are sorted in ascending order
     * Postcond: Input arrays unchanged, and 
     * output array sorted in ascending order.
     ******************************************************/
    private static int[] merge( int[] a, int[] b ) 
    {
	int[] ans = new int[a.length+b.length];
	int index = 0;
	int ain = 0;
	int bin = 0;
	while (ain < a.length -1 && bin < b.length -1) {
	    if (a[ain] >= b[bin]) {
		ans[index] = b[bin];
		bin +=1; }
	    else {
		ans[index] = a[ain];
		ain += 1; 
	    }
	    index +=1;
	}
	if (a.length == 0) {
	    for (int each : b) {
		ans[index] = each;
	    }
	}
	else {
	    for (int each : a) {
		ans[index] = each;
	    }
	}
	return ans;
    }//end merge()


    /******************************************************
     * int[] sort(int[]) 
     * Sorts input array using mergesort algorithm
     * Returns sorted version of input array (ascending)
     ******************************************************/
    public static int[] sort( int[] arr ) 
    {
	int[] arr1 = new int[arr.length%2-1];
	int[] arr2 = new int[arr.length - arr.length%2-1];
	//while (arr1.length != 0 && arr2.length != 0) { 
	return merge( sort(arr1), sort(arr2) );
	    
	/*	int origl = arr.length;
	if (arr.length > 1) {
	    for (int i = 0; i < (arr.length -1)/2; i++) {
		int[] part = new int[(arr.length -1)/2];
		part[i] = arr[i];
	    }
	    for (int i = (arr.length-1)/2 +1; i < (arr.length -1); i++) {
		int[] part = new int[(arr.length -1)/2];
		part[i] = arr[i];
	    }
	}
	if (arr.length == 1) {
	    return arr; }
	while (arr.length != origl) {
	    

	} */
	
	    
    }//end sort()



    //-------------------HELPERS-------------------------
    //tester function for exploring how arrays are passed
    //usage: print array, mess(array), print array. Whaddayasee?
    public static void mess( int[] a ) {
	for( int i = 0 ; i<a.length; i++ )
	    a[i] = 0;
    }

    //helper method for displaying an array
    public static void printArray( int[] a ) {
	System.out.print("[");
	for( int i : a )
	    System.out.print( i + ",");
	System.out.println("]");
    }
    //---------------------------------------------------


    //main method for testing
    public static void main( String [] args ) {

	//*~~~~~~~~~~~~~~ Ye Olde Tester Bar ~~~~~~~~~~~~~~
	int[] arr0 = {0};
	int[] arr1 = {1};
	int[] arr2 = {1,2};
	int[] arr3 = {3,4};
	int[] arr4 = {1,2,3,4};
	int[] arr5 = {4,3,2,1};
	int[] arr6 = {9,42,17,63,0,512,23};
	int[] arr7 = {9,42,17,63,0,9,512,23,9};

	System.out.println("\nTesting mess-with-array method...");
	printArray( arr3 );
	mess(arr3);
	printArray( arr3 );

	System.out.println("\nMerging arr1 and arr0: ");
	printArray( merge(arr1,arr0) );

	System.out.println("\nMerging arr4 and arr6: ");
	printArray( merge(arr4,arr6) );

	System.out.println("\nSorting arr4-7...");
	printArray( sort( arr4 ) );
	printArray( sort( arr5 ) );
	printArray( sort( arr6 ) );
	printArray( sort( arr7 ) );
	//	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
    }//end main()

}//end class MergeSort

