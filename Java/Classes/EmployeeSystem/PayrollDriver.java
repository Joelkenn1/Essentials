package ex4;

import java.util.ArrayList;

public class PayrollDriver {

	public static void main(String[] args) {
		
		ArrayList <Employee> payroll = new ArrayList<Employee>();
		
		WeeklyEmployee we = new WeeklyEmployee();
		
		WeeklyEmployee we2 = new WeeklyEmployee();
		
		WeeklyEmployee we3 = new WeeklyEmployee();
		
		we.setHours(20);
		
		we.setRate(10);
		
		MonthlyEmployee me = new MonthlyEmployee(2000);
		
		MonthlyEmployee me2 = new MonthlyEmployee(1000);
		
		MonthlyEmployee me3 = new MonthlyEmployee(500);
		
		payroll.add(we);
		
		payroll.add(me);
		
		payroll.add(me2);
		
		payroll.add(me3);
		
		payroll.add(we2);
		
		payroll.add(we3);
		
		
		double all_emp_total = 0;
		
		double month_emp_total = 0;
		
		double weekly_emp_total = 0;
		
		for(int i = 0; i < payroll.size(); i++) {
			
			if(payroll.get(i) instanceof MonthlyEmployee) {
				
				month_emp_total += payroll.get(i).CalcPay();
				all_emp_total += payroll.get(i).CalcPay();
			}
			
			else if(payroll.get(i) instanceof WeeklyEmployee) {
				
				weekly_emp_total += payroll.get(i).CalcPay();
				all_emp_total += payroll.get(i).CalcPay();
			}
			else {}
		}
		System.out.println("Total for all employees is: " + all_emp_total);
		System.out.println("Total for weekly employees is: " + weekly_emp_total);
		System.out.println("Total for monthly employees is: " + month_emp_total);
	}
	

}
