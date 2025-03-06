
class MergeSort
{
    // Merges two subarrays of arr[].
    // First subarray is arr[l..m]
    // Second subarray is arr[m+1..r]
    void merge(int arr[], int l, int m, int r)
    { 
        
        int l_size = (m - l) + 1;
        int r_size = r - m;


 
        /* Create temp arrays */
        int L[] = new int[l_size];
        int R[] = new int[r_size];
        int S[] = new int[arr.length];
        int temp[] = new int[arr.length];
  
 



        /*Copy data to temp arrays*/
        for(int i = 0; i < l_size; i++){
            L[i] = arr[l + i];
        
        }

        for(int i = 0; i < r_size; i++){
            R[i] = arr[m + i + 1];
            
        }
        
        int i = 0;
        int j = 0;
        int k = l;

        while (i < l_size && j < r_size){
            if (L[i] <= R[j]){

                arr[k] = L[i];
                i++;
            }
            else {
               
                arr[k] = R[j];
                j++; 
            }
            
            k++;
             
        }
            
        
        /* Copy remaining elements of L[] if any */
        while (i < l_size) {

            arr[k] = L[i];
            
            i++;
            k++;

        }
        
       /* Copy remaining elements of R[] if any */
        while (j < r_size) {

            arr[k] = R[j];
            
            j++;
            k++;

        }
        
}
 
    // Main sorting function that sorts arr[l..r] using
    // merge() above
    void sort(int arr[], int l, int r)
    {
        if (l < r)
        {
            // Find the middle point
            int m = (l+r)/2;
 
            // Sort first and second halves
            sort(arr, l, m);
            sort(arr , m+1, r);
 
            // Merge the sorted halves
            merge(arr, l, m, r);
            
        }
    }

    // void modsort(int arr[], int p, int r){

    //     if(p<r){
    //         int mid = p + (r-p)/3;
    //         int mid2 = p + (2*(r-p))/3;
    //         modsort(arr, p, mid);
    //         modsort(arr, mid + 1, mid2);
    //         modsort(arr, mid2 + 1, r);
    //         merge(arr, p, mid, mid2);
    //         printArray(arr);
    //         merge(arr, p, mid2, r);
    //         printArray(arr);
    //     }
    // }
 
    /* A utility function to print array of size n */
    static void printArray(int arr[])
    {
        int n = arr.length;
        for (int i=0; i<n; ++i)
            System.out.print(arr[i] + " ");
        System.out.println();
    }
 
    // Driver method
    public static void main(String args[])
    {
        // Input Array
		// Modify this to check the correctness of your code
		int arr[] = {9,4,6, 3, 7,2, 8, 1, 5};
 
        System.out.println("Given Array:");
        printArray(arr);
 
        MergeSort ob = new MergeSort();
        //ob.sort(arr, 0, arr.length-1);
        ob.sort(arr, 0, 8);
 
        System.out.println("\nSorted array:");
        printArray(arr);
    }
}

