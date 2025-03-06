package ex2;

import java.util.ArrayList;

public class Basket {
	
	/*private Product[] prods = new Product[3];
	
	private int[] numUnits = new int[3];*/
	
	private ArrayList<Product> prods = new ArrayList<Product>();
	
	private ArrayList<Integer> numUnits = new ArrayList<Integer>();
	
	//private int index = 0;
	
	
	public ArrayList<Product> getProds(){
		
		return this.prods;
	}
	public void addProduct(Product prod, int qty) {
		
		/*this.prods[index] = prod;
		
		this.numUnits[index] = this.numUnits[index] + qty;
		index++;*/
		
		if(prods.contains(prod)) {
			
			int index = prods.indexOf(prod);
			
			int num = this.numUnits.get(index);
			
			num += qty;
			
			this.numUnits.set(index, num);
		}
		else {
			
		this.prods.add(prod);
		
		this.numUnits.add(qty); }
	}

	public double total() {
		
		double sum = 0.0;
		
		/*for(int i = 0; i < prods.size(); i++) {
			
			double price = prods[i].getProdPrice();
			
			int units = numUnits[i];
			
			double calc = price + units;
			
			sum += calc;
		}*/
		
		for(int i = 0; i < prods.size(); i++) {
			
			double price = prods.get(i).getProdPrice();
			
			int units = numUnits.get(i);
			
			double calc = price + units;
			
			sum += calc;
		}
		
		return sum;
	}
}
