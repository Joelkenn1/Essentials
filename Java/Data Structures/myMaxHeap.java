// Java program for Max-Heap from Array

/*

// ===============================================
// CSCI 3230A Data Structures
// Fall 2024
// Instructor: M Arif Rahman, Ph.D.
// THA-3; Closed-Resources, Individual Test.

// ==============****FILL IN YOUR INFO HERE****======================
//Name:Caleb Kenney
//Eagle ID:901345675
// ==============****FILL IN YOUR INFO HERE****======================

// ======================= IMPORTANT NOTES ======================== 
//  1. DO NOT DELETE ANY COMMENT OR ANY CODE FROM THE TEMPLATE PROVIDED!!! 
//  2. DO NOT MAKE ANY CHANGES TO THE MAIN FUNCTION!!!
//  3. You will only need to fill in the blocks with comment "COMPLETE THIS BLOCK".
//  4. Modify the file name to "myMaxHeap.java" before compiling and submitting it.
//  5. DON’T FORGET TO INPUT YOUR NAME AND EAGLE ID AT THE TOP!!!

// ====================== Requirements ========================
// Implement Max-Heapify functionality in an Array of integers. 
// which was illustrated during the lecture slides "Lecture7-SpecialsQueuesHeaps.pdf".
// That is, you need to translate the following algorithm to Java code for the Max-Heapify.


I.  Algorithm Max-HeapifyFromArray ( Array arr[] )
1.	You are given an array, arr[] of integers representing the complete binary tree. That is, the left and the right child of ith node are in indices 2*i+1 and 2*i+2 in the array.
2.	We set the index of the current element, i, as the ‘MAXIMUM’.
3.	If arr[2 * i + 1] > arr[i], i.e., the left child is larger than the current value, it is set as ‘MAXIMUM’.
4.	Similarly if arr[2 * i + 2] > arr[i], i.e., the right child is larger than the current value, it is set as ‘MAXIMUM’.
5.	Swap the ‘MAXIMUM’ with the current element.
6.	Repeat steps 2 to 5 till the property of the heap is restored.


// Please use appropriate data types and access modifiers
// to demonstrate the correctness of your code.
//
// Inputs are already provided in the driver Main() function. 
// Your output will look as follows if your implementation is correct:
// ------------------------------------
// Before MaxHeapify:
// 1 3 5 4 6 13 10 9 8 15 17 
// After MaxHeapify:
// 17 15 13 9 6 5 10 4 8 3 1


*/

public class myMaxHeap {


    static void maxHeapify(int arr[], int N, int i)
    {
		    // COMPLETE THIS BLOCK
			// WRITE YOUR CODE HERE
			// DO NOT DELETE ANY OF THE TEMPLETE CODE
			
		    // heapify a subtree rooted with node i which is an index in arr[].
			// N is size of heap

        
        int currentMaxIndex = i;
        
        int leftChildIndex = (2 * currentMaxIndex) + 1;

        int rightChildIndex = (2 * currentMaxIndex) + 2;

        int temp = 0;


        // check if rightChild is greater than parent/leftChild
        if (arr[rightChildIndex] > arr[currentMaxIndex] && arr[rightChildIndex] > arr[leftChildIndex]){

            temp = arr[rightChildIndex];
            arr[rightChildIndex] = arr[currentMaxIndex];

            // currentMax = rightChild (set parent equal to rightChild)
            arr[currentMaxIndex] = temp;

             /* Now that the rightChild is in the parent position, the process is repeated checking
                the latest parent */
            buildMyMaxHeapFromArray(arr, N);}    
        

        // check if leftChild is greater than parent/rightChild
        if (arr[leftChildIndex] > arr[currentMaxIndex] && arr[leftChildIndex] > arr[rightChildIndex]){
            
            temp = arr[leftChildIndex];
            arr[leftChildIndex] = arr[currentMaxIndex];

            // currentMax = leftChild (set parent equal to leftChild)
            arr[currentMaxIndex] = temp; 

            /* Now that the leftChild is in the parent position, the process is repeated checking 
               the latest parent.*/
            buildMyMaxHeapFromArray(arr, N); }


        /*  The else statement allows the next parent's children to be checked after the previous subtree
            has been properly sorted.  */
        else {
            return;
        }


    }


    static void buildMyMaxHeapFromArray(int arr[], int N)
    {
        int indexOfLastNonLeafNode = (N / 2) - 1;

        // reverse traversal from last non-leaf node to root and max-heapify
        for (int i = indexOfLastNonLeafNode; i >= 0; i--) {
            for (int x = 0; x < N; x++)
                System.out.print(arr[x] + " ");
            System.out.println();
            maxHeapify(arr, N, i);
        }
    }


    // Driver
    public static void main(String args[])
    {
        int randomArray[] = {1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17}; //test purposes
        int N = randomArray.length; //size of Array

        System.out.println("Before MaxHeapify:");
        for (int i = 0; i < N; i++)
            System.out.print(randomArray[i] + " ");
        System.out.println();

        // Initial heap of input array
        //             1
        //           /    \
        //         3        5
        //       /  \      /  \
        //     4   6  13  10
        //    / \    / \
        //   9 8 15 17

        buildMyMaxHeapFromArray(randomArray, N);

        System.out.println("After MaxHeapify:");
        for (int i = 0; i < N; i++)
            System.out.print(randomArray[i] + " ");
        System.out.println();

        // Final Heap:
        //             17
        //            /    \
        //          15   13
        //         /   \     /  \
        //        9   6  5  10
        //      /  \   /  \
        //    4   8 3  1
    }
}
