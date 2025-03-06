package ex2;

import java.time.LocalDate;

public class BasketDriver {

	public static void main(String[] args) {
		
		Product p1 = new Product("Dr. Pepper", 2.0);
		Product p2 = new Product("Sprite", 1.5);
		Product p3 = new Product("Pepsi", 1.75);
		Product p4 = new Product("Pepsi", 1.75);
		
		Perishable a1 = new Perishable(LocalDate.of(2023, 04, 12));
		
		Basket b1 = new Basket();
		b1.addProduct(p1, 2);
		b1.addProduct(p2, 4);
		b1.addProduct(p3, 5);
		b1.addProduct(p4, 1);
		b1.addProduct(a1, 4);
		
		System.out.println(b1.total());
		
		
		for(int i = 0; i < b1.getProds().size(); i++) {
			
			Product prod = b1.getProds().get(i);
			
			System.out.print(" Prod: " + prod.getProdName() +  ", ");
			
			
			
			if(prod instanceof Perishable) {
			Perishable per1 = (Perishable)prod;
			System.out.println();
			System.out.println(per1.getProdName());}
		}
	}

}
