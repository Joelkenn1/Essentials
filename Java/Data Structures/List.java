import java.util.LinkedList;
import java.util.ArrayList;

public class List {

    public static void main(String args[]){

        LinkedList<Integer> list1 = new LinkedList<>();
        
        list1.add(1);
        list1.add(10);
        list1.add(100);

        System.out.println("The output of the linked list " + list1.toString());

        System.out.println("The third element of the linked list is " + list1.get(2));

        System.out.println("The first element of the linked list is " + list1.getFirst());


        System.out.println();



        ArrayList<String> list2 = new ArrayList<>();

        list2.add("Apples");
        list2.add("Oranges");
        list2.add("Bananas");


        System.out.println("The output of the array list " + list2.toString());

        System.out.println("The second element of the array list is " + list2.get(1));

        


    }
    
}
