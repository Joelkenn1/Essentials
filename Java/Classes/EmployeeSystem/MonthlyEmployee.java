package ex4;

public class MonthlyEmployee extends Employee{

	private double monthpay;
	
	public MonthlyEmployee(double monthpay) {
		
		this.monthpay = monthpay;
	}
	
	public double CalcPay() {
		
		return this.monthpay;
	}
	
	
}
