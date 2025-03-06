
public class ImplementClass implements InterfacePractice{
	
	public String name;
	public boolean studentstatus;
	public int gradyear;
	
	
	public void isStudent() {
		studentstatus = true;
		System.out.println("We're so glad you chose to come to school in Statesboro.");
	}
	
	public void getName() {
		System.out.println("Welcome to Georgia Southern " + name);
	}
	
	public void getGradYear() {
		System.out.println("Your currently expected to graduate in " + (gradyear - 2023) + " years");
	}
	
	
	public void showInfo() {
		System.out.println("Name: " + name);
		
		if(studentstatus == true) {
			System.out.println("Is this a Student? Yes");
		}
		else {
			System.out.println("Is this a Student? No");
		}
		
		System.out.println("Graduation Year" + gradyear);
		
		
	}
}
