package ex2;

public class Product {

	// state or class fields
	private double prodPrice;
	private String prodName;
	
	//constructors
	public Product(String prodName, double prodPrice) {
		this.setProdName(prodName);
		this.setProdPrice(prodPrice);
	}
	
	public Product() {
		this("did not enter", 0.25);
	}
	
	public Product(String prodName) {
		this(prodName, 10.0);
	}
	
	//operations
	public void setProdName(String prodName) {
		
		if(prodName == null) {
			this.prodName = "no name";
		}
		else {
			this.prodName = prodName;
		}
	
	}
	
	public String getProdName() {
		
		return this.prodName;
	}
	
	public void setProdPrice(Double prodPrice) {
		
		if(prodPrice < 0) {
			this.prodPrice = 0.25;
		}
		
		else {
			
			this.prodPrice = prodPrice;
		}
	
		
	}
	
	public double getProdPrice() {
		
		return this.prodPrice;
	}
	
	public boolean equals(Object o) {
		
		Product p = (Product)o;
		
		if(this.prodName.equals(p.prodName)) {
			return true;
		}
		else {
			return false;
		}
	}
}
