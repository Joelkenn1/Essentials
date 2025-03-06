package ex2;

public class ProductDriver {

	public static void main(String[] args) {
		
		Product p1 = new Product();
		
		p1.setProdName("Pepsi");
		
		p1.setProdPrice(1.0);
		
		System.out.println("This " + p1.getProdName() + " cost " + p1.getProdPrice() + " dollars");
		
		Product p2 = new Product();
		
		p2.setProdPrice(2.5);
		p2.setProdName(null);
		
		System.out.println("This " + p2.getProdName() + " cost " + p2.getProdPrice() + " dollars");
		
		Product p3 = new Product("cola");
	}

}
