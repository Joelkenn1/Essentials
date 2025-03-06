import java.util.Date;

public class Order {
		
	// Declaration of order status constant variables
		public static final int ON_ORDER = 0;
		
		public static final int CANCELED = 1;
		
		public static final int SHIPPED = 2;
		

		// Declaration of variables in the Order constructor
		private static int totalOrder = 0;
		
		private String OrderName;
		
		private Date date;
		
		private int status;
		
	// Declaration of variables to be later used in set methods to complete the toString method
		private String shippingAddress;
		
		private String phoneNumber;
		
		private String billingAddress;
		
		
		// Creation of the Order constructor
		public Order(String Name) {
			
			this.totalOrder = totalOrder + 1;
			
			this.OrderName = Name;
			
			this.status = ON_ORDER;
			
			this.date = new Date();
		}
		
		// Creation of the cancel method which also returns the current date when invoked
		public void cancel() {
			
			this.date = new Date();
			
			this.status = CANCELED;
		}
		
		// Creation of the ship method which also returns the current date when invoked
		public void ship() {
			
			this.date = new Date();
			
			this.status = SHIPPED;
		}
		
		// Creation of the date method which returns the current date
		public Date getDate() {
			
			return date;
		}
		
		// Creation of the setShippingAddress method which returns the address passed into its parameter
		public void setShippingAddress(String a) {
			
			shippingAddress = a;
		}
		
		// Creation of the setphoneAddress method which returns the phone number passed into its parameter
		public void setPhoneNumber(String p) {
			
			phoneNumber = p;
		}
		
		// Creation of the setBillingAddress method which returns the address passed into its parameter
		public void setBillingAddress(String add) {
			
			billingAddress = add;
		}
		
		// Creation of the getTotalOrder method which returns the total order when called
		public static int getTotalOrder() {
			
			return totalOrder;
		}
		
		// Creation of the getStatus method which returns the status of the order when called
		public int getStatus() {
			
			return this.status;
		}
		
		// Creation of the getShippingAddress method which returns the shipping address when called
		public String getShippingAddress() {
			
			return this.shippingAddress;
		}
		
		// Creation of the getPhoneNumber method which returns the phone number when called
		public String getPhoneNumber() {
			
			return this.phoneNumber;
		}
		// Creation of the getBillingAddress method which returns the billing address when called
		public String getBillingAddress() {
			
			return this.billingAddress;
		}
		
		// Creation of the toString method which returns the order name, date, status, shipping/billing address and phone number
		public String toString() {
				
			if(shippingAddress == billingAddress) {
				
				return this.OrderName + " " + this.date + " " + this.status + " " + this.shippingAddress + " " + this.phoneNumber;
			}
			else {
				return this.OrderName + " " + this.date + " " + this.status + " " + this.shippingAddress + " " + this.billingAddress + " " + this.phoneNumber;
			}

			}
		}


