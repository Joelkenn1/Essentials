
import java.util.*;
import java.util.LinkedList;
import java.util.List;

public class myDFSBFS {
	
    static void RecursiveDFS(List<List<Integer> > adj, boolean[] visited, int s){
        
		// COMPLETE THIS BLOCK
        Stack<Integer> stackDFS = new Stack<>();
        ArrayList<Integer> visited_nums = new ArrayList<>();

        stackDFS.push(s);
        visited[s] = true;

        System.out.print(stackDFS.peek().toString() + " ");
        

        for (List<Integer> x : adj){
            if(adj.indexOf(x) == stackDFS.peek()){
                
                for(int i : x){
                    if(visited[i] == false){
                        visited[i] = true;
                        visited_nums.add(i);
                        break;
                    }  
                }
            }
        }
        
        
        for (int i : visited_nums){

            if (stackDFS.empty() == true) {
                System.out.print("");
            }
            else if(visited[i] == true && stackDFS.contains(i) == false){
                stackDFS.push(i);
                RecursiveDFS(adj, visited, stackDFS.peek());
                
            }
            else {
                RecursiveDFS(adj, visited, stackDFS.pop());
            }
        }
		
    }


    static void nonRecursiveBFS(List<List<Integer>> adj, int s) {

        // COMPLETE THIS BLOCK
        Queue<Integer> queueBFS = new LinkedList<>();
        ArrayList<Integer> visited_nums = new ArrayList<>();
        queueBFS.add(s);

        for(List<Integer> x : adj){

            if(adj.indexOf(x) == s){

                for(int y: x){
                    
                    if (visited_nums.contains(y) == false && y != s) {
                        visited_nums.add(y);
                        queueBFS.add(y);
                    }
                }
            }
        }

        for(List<Integer> z : adj){

            if (adj.indexOf(z) != s){

                for(int y: z){

                    if (visited_nums.contains(y) == false && y != s) {
                        visited_nums.add(y);
                        queueBFS.add(y);}

                }

             }

        }

        int i = 0;

        while (i < adj.size()){
            System.out.print(queueBFS.remove() + " ");
            i++;
        }
            
    }

    // adjacency list
    static void addEdge(List<List<Integer> > adj, int s, int t){
		//undirected
        adj.get(s).add(t);
        adj.get(t).add(s);
    }


    public static void main(String[] args) {
	// DRIVER FUNCTION DO NOT MODIFY ANYTHING
   
        int V = 5; // number of vertices 

        // adjacency list 
        List<List<Integer> > adj = new ArrayList<>(V);
        for (int i = 0; i < V; i++) {
            adj.add(new ArrayList<>());
        }

		// add edges
        addEdge(adj, 0, 1);
        addEdge(adj, 0, 4);
        addEdge(adj, 1, 2);
        addEdge(adj, 1, 3);
        addEdge(adj, 2, 4);

        // DFS
        boolean[] visitedDFS = new boolean[adj.size()];
        int source = 0;
        System.out.println("DFS from source: " + source);
        RecursiveDFS(adj, visitedDFS, source);

        visitedDFS = new boolean[adj.size()];
        source = 3;
        System.out.println("\nDFS from source: " + source);
        RecursiveDFS(adj, visitedDFS, source);

        // BFS
        source = 0;
        System.out.println("\nBFS from source: " + source);
        nonRecursiveBFS(adj, source);

        source = 4;
        System.out.println("\nBFS from source: " + source);
        nonRecursiveBFS(adj, source);
    }
}