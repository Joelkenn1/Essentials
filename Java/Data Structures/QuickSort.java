 import java.util.Arrays;
import java.util.*;

public class H1{

   static int key_comp = 0;
   static int swaps = 0;
   
   static ArrayList<Integer> swapTotal = new ArrayList<>();
   

   public static void main(String args[]){ 

      // This is just a test array. The provided inputs in columns 1 and 2 of the pdf have been already tested.
      //int [] test = {1, 2, 3, 0, 4};

      int[] arr1 = new int[100];
      int[] arr2 = {1, 2, 3, 4};
      int y = 10000;
      

      for(int i = 0; i < arr1.length; i++){
         //arr1[i] = y;
         //y--;
         arr1[i] = (int) (1 + Math.random() * 100000);

         
      }
      
     // //For Verifying The Initial Order Before Swapping
     //  System.out.println("Initial List: " + Arrays.toString(arr2)); 

     //  //Comment Out Whichever Algorithm Isn't Being Used At The Moment
     //  HOARE_QUICKSORT(arr2 , 0, arr2.length - 1);

     //  System.out.println("HOARE-QUICKSORT, size "  + arr2.length + ": " + Arrays.toString(arr2)); 


      LOMUTO_QUICKSORT(arr2 , 0, arr2.length - 1);
      System.out.println("LOMUTO-QUICKSORT, size "  + arr2.length + ": " + Arrays.toString(arr2));

      printKeyComp(key_comp);
      printSwaps(swaps);

      //To See The Number Of Swaps Per Iteration
      System.out.println("Swap Total: " + swapTotal.toString());
   

   }

   public static void HOARE_QUICKSORT(int[] A, int p, int r){ 
   
    if (p < r){

      int q = HOARE_PARTITION(A, p, r);
      HOARE_QUICKSORT(A, p, q);
      HOARE_QUICKSORT(A, q + 1, r);
            
        }
   }   

   public static int HOARE_PARTITION(int[] A, int p, int r){  

      int x = A[p];
      int i = p - 1;
      int j = r + 1;
      int temp;
         
     
      while(true){
            
         do {
            j--;
            key_comp++;
         } while(A[j] > x);

         do {
            i++;
            key_comp++;
         } while(A[i] < x);

         if(i < j){
            temp = A[i];
            A[i] = A[j];
            A[j] = temp;
            swaps++;
               
            }
               swapTotal.add(key_comp);
               return j;
    
      }

      
      

   }

   public static void LOMUTO_QUICKSORT(int[] A, int p, int r){ 
   
      if (p < r){
  
        int q = LOMUTO_PARTITION(A, p, r);
        LOMUTO_QUICKSORT(A, p, q - 1);
        LOMUTO_QUICKSORT(A, q + 1, r);
              
          }
     } 

   public static int LOMUTO_PARTITION(int[] A, int p, int r){
      
      int x = A[r];
      int i = p - 1;
      int temp;
      
      for(int j = p; j <= r - 1; j++){
         if(A[j] <= x){

            i = i + 1;
            key_comp++;
            

            temp = A[i];
            A[i] = A[j];
            A[j] = temp;
            swaps++;
            
            
         }
        swapTotal.add(key_comp);
      }

      temp = A[i + 1];
      A[i + 1] = A[r];
      A[r] = temp;
      swaps++;

      return i + 1;

   }


   public static void printKeyComp(int kc){
      System.out.print("Key Comparsions: " + kc + "\n");
   }


   public static void printSwaps(int swaps){
      System.out.print("Swaps: " + swaps + "\n");
   }




   }

     










