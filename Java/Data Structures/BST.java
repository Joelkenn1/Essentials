

class Nodes {

    int key;
    Nodes left;
    Nodes right;
    Nodes parent;

    public Nodes(int k)
    {
        key = k;
        left = null;
        right = null;
        parent = null;
    }  

    Nodes root;
}


public class BST {

    static int key_comp = 0;
    
    public static void main(String args[]){

      int[] arr1 = new int[100];
      int y = 100;
      
      for(int i = 0; i < arr1.length; i++){

        arr1[i] = i; 
      //arr1[i] = y;
      //y--;
      //arr1[i] = (int) (1 + Math.random() * 100000);
      }

        //fillArray(arr1, 0, arr1.length - 1);

        System.out.println("Array Size: " + arr1.length);

        System.out.print("The First 20 Elements In The Array: ");

        for(int x = 0; x < 20; x++){
            System.out.print(arr1[x] + " ");
        }
            

        System.out.print("\nThe First 20 Elements In The Sorted Array: ");

        BST_Sort(arr1, arr1.length);

        System.out.println("\nKey Comparsions: " + key_comp);


        

        
    }

    
    public static Nodes Tree_Insert(Nodes root, Nodes newNode){

        if(root == null){
            return newNode;
        }

        key_comp++;
        if(newNode.key < root.key){
            root.left = Tree_Insert(root.left, newNode);
            root.left.parent = root;
        }

        else{
            root.right = Tree_Insert(root.right, newNode);
            root.right.parent = root;
        }

        return root;
  
    }

    private static int count = 0;
    
    public static void ioTreeWalk(Nodes root){
        
        if(root != null){

            ioTreeWalk(root.left);

            while(count < 20){
                System.out.print(root.key + " ");
                count++;
                break;}
                
            ioTreeWalk(root.right);
            }
    }

    
    public static void BST_Sort(int[] array, int size){

        Nodes root = null;

        for(int i = 0; i < size; i++){

            Nodes newNode = new Nodes(array[i]);

            root = Tree_Insert(root, newNode);
        }

        ioTreeWalk(root);
    }

    public static void decreaseKey(int[] arr, int i, int k){
            if(k > arr[i]){
                System.out.print("error");
                }

            arr[i]=k;

            while(i > 1 && arr[
        }

    
    private static int index = 0;
    
    public static void fillArray(int[] arr, int low, int high) {
        
        if (low <= high) {
            
            int mid = (low + high) / 2;
            
            arr[index++] = mid + 1;
            
            fillArray(arr, low, mid - 1);
            fillArray(arr, mid + 1, high);
        }
    }

}