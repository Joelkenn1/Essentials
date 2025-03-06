
import java.io.*;

public class LinkedList {

    Node head; // head reference of the linked list
    // Need a Linked list Node.
    // Static so main() can access it
    static class Node {
        int data;
        Node next;
		
        // Constructor, only stores Integers
        Node(int d)
        {
            data = d;
            next = null;
        }
    }

    // Method to insert a new node
    public static LinkedList insert(LinkedList list, int data)
    {
        // Create a new node first with given data
        Node new_node = new Node(data);
        new_node.next = null;

        // Make the new node as head if the list was empty
        if (list.head == null) {
            list.head = new_node;
        }
        else {
            // Else insert the new_node at last
            Node last = list.head;
            while (last.next != null) {
                last = last.next;
            }

            last.next = new_node;
        }
        return list;
    }

    // Method to traverse/print the list
    public static void printList(LinkedList list)
    {
        Node currNode = list.head;

        System.out.print("LinkedList: ");

        // Traverse through the LinkedList and print
        while (currNode != null) {

            System.out.print(currNode.data + " ");
            currNode = currNode.next;
        }
		
        System.out.println();
        System.out.println();
    }


    // Method to delete a node in the LinkedList by KEY
    public static LinkedList deleteByKey(LinkedList list, int key)

    //COMPLETE THIS BLOCK
    //BY IMPLEMENTING THIS FUNCTION
    {
        Node currNode = list.head;
        Node prevNode = currNode;

        // CASE 1:
        // If head node itself holds the key to be deleted
           if(currNode.data == key){
                
                list.head = currNode.next;
                System.out.println(key + " found and deleted");
            
               }


        // CASE 2:
        // If the key is somewhere other than at head
        try {

            if(currNode.data != key) {
                
                while(currNode.data != key){

                    prevNode = currNode;
                    currNode = currNode.next;
                    
               }

               prevNode.next = currNode.next;
               System.out.println(key + " found and deleted");
            }
            


        // CASE 3: The key is not present
        } catch (NullPointerException n) {
            System.out.println(key + " is not within the list!!");
        }



        // return the List
        return list;
    }


    // Method to delete a node by POSITION
    public static LinkedList deleteAtPosition(LinkedList list, int index)
    {

        //COMPLETE THIS BLOCK
        //BY IMPLEMENTING THIS FUNCTION
        Node currNode = list.head;
        Node prevNode = currNode;
        int count = 0;

        // CASE 1:
        // If index is 0, then head node itself is to be deleted
           if(index == 0){
            currNode = currNode.next;
            list.head = currNode;
            System.out.println(index + " position element deleted");
           }


        // CASE 2:
        // If the index is greater than 0 but less than the size of LinkedList
        try {
           if(index > 0){
                while(count < index){
                    
                    prevNode =  currNode;
                    currNode = currNode.next;
                    count++;
            }

            prevNode.next = currNode.next;
            System.out.println(index + " position element deleted");
        }


         // CASE 3: The index is greater than the size of the LinkedList
        } catch(NullPointerException n){
            System.out.println(index + " position does not exist!!");
        }
 
          

        // return the List
        return list;
    }


    public static void main(String[] args)
    {

        LinkedList list = new LinkedList();

        // Insert the values
        list = insert(list, 1);
        list = insert(list, 2);
        list = insert(list, 3);
        list = insert(list, 4);
        list = insert(list, 5);
        list = insert(list, 6);
        list = insert(list, 7);
        list = insert(list, 8);

        // Print
        printList(list);

        // Delete node
        deleteByKey(list, 1);
        printList(list); // Print to verify

        deleteByKey(list, 4);
        printList(list); // Print to verify

        deleteByKey(list, 10);
        printList(list); // Print to verify


        deleteAtPosition(list, 0);
        printList(list); // Print to verify

        deleteAtPosition(list, 2);
        printList(list); // Print to verify

        deleteAtPosition(list, 3);
        printList(list); // Print to verify

        deleteAtPosition(list, 7);
        printList(list); // Print to verify
        
    }

}
