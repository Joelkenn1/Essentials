package ex2;

import java.time.LocalDate;
import java.time.Period;

public class Perishable extends Product{

	private LocalDate date;
	
	public Perishable(LocalDate date){
		
		super("carrots", 2);
		this.date = date;
		
	}
	
	public void setProdName(String prodName) {
		
		super.setProdName(prodName + " PER");
	}
	
	public void setProdPrice(double prodPrice) {
		
		super.setProdPrice(prodPrice + 1.0);
		System.out.println("$1 fee");
	}
	
	public static void main(String args[]) {
		
		Perishable p = new Perishable(LocalDate.of(2023, 04, 9));
		
		p.setProdName("apple");
	
		System.out.println(p.getProdName());
		
		p.setProdPrice(0);
		
		System.out.println(p.getProdPrice());
		
		System.out.println(p.date);
		
		Period period = Period.between(LocalDate.now(), p.date);
		
		System.out.println(period.getMonths());
		

	}
}
