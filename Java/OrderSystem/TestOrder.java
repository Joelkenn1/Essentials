
public class TestOrder {

	public static void main(String[] args) {
		
		// Creation of the order 1 object
		Order order1 = new Order("First Order");
		
		// Initiation of the methods which set order 1's shipping/billing address and phone number
		order1.setShippingAddress("1324 Washington Lane");
		
		order1.setBillingAddress("1324 Washington Lane");
		
		order1.setPhoneNumber("777-777-7777");
		
		// Initiation of the toString method which prints out the contents of order1
		System.out.print(order1.toString());
		
		System.out.println();
		
		
		// Creation of the order 2 object
		Order order2 = new Order("Second Order");
		
		// Sets order 2's status to canceled
		order2.cancel();
		
		// Initiation of the methods which set order 2's shipping/billing address and phone number
		order2.setShippingAddress("2222 2nd Street");
		
		order2.setBillingAddress("2222 2nd Street");
		
		order2.setPhoneNumber("506-907-4455");
		
		// Initiation of the toString method which prints out the contents of order2
		System.out.print(order2.toString());
		
		System.out.println();
		

		
		// Creation of the order 3 object
		Order order3 = new Order("Third Order");
		
		// Sets order 3's status to shipped
		order3.ship();
		
		// Initiation of the methods which set order 3's shipping/billing address and phone number
		order3.setShippingAddress("8585 85th Avenue");
		
		order3.setBillingAddress("8585 85th Avenue");
		
		order3.setPhoneNumber("801-382-2937");
		
		// Initiation of the toString method which prints out the contents of order3
		System.out.print(order3.toString());
		
		System.out.println();
		

	}

}
