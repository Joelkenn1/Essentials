package ex4;

public class WeeklyEmployee extends Employee {
	
	private double rate;
	
	private int hours;
	
	public double CalcPay() {
		
		return this.getHours() + this.getRate();
	}

	public double getRate() {
		return rate;
	}

	public void setRate(double rate) {
		this.rate = rate;
	}
	

	public int getHours() {
		return hours;
	}

	public void setHours(int hours) {
		this.hours = hours;
	}

}
