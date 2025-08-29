# Import necessary modules from SQLAlchemy
from sqlalchemy.orm import sessionmaker  # To create sessions for interacting with the database
from sqlalchemy import create_engine  # To create the database engine (connection)
from models import Customer, MenuItem, Order  # Import the ORM models (tables)

# Database setup
engine = create_engine("sqlite:///restaurant.db")  # Create a SQLite database called restaurant.db
Session = sessionmaker(bind=engine)  # Bind the sessionmaker to the engine to manage transactions

# ---------- CUSTOMER FUNCTIONS ----------

def add_customer(session):
    print("\n--- Add New Customer ---")  # Display section header
    name = input("Enter customer name: ").strip()  # Get name from user
    email = input("Enter customer email: ").strip()  # Get email from user
    phone = input("Enter customer phone: ").strip()  # Get phone from user

    # Validate required fields
    if not name or not email:
        print("Name and email are required.")
        return

    # Check if email already exists in database
    if session.query(Customer).filter_by(email=email).first():
        print("Email already exists. Try again.")
        return

    # Create new customer object
    new_customer = Customer(name=name, email=email, phone=phone)
    session.add(new_customer)  # Add to session
    try:
        session.commit()  # Save changes to database
        print(f"Customer '{name}' added successfully!")
    except Exception as e:
        session.rollback()  # Undo changes if error occurs
        print(f"Error adding customer: {e}")

def view_customers(session):
    print("\n--- All Customers ---")
    customers = session.query(Customer).all()  # Fetch all customers
    if not customers:
        print("No customers found.")
    else:
        for c in customers:  # Loop through customers and display
            print(f"[{c.id}] {c.name} | {c.email} | {c.phone}")

def update_customer(session):
    view_customers(session)  # Show current customers
    try:
        customer_id = int(input("Enter customer ID to update: ").strip())  # Get ID
    except ValueError:
        print("Invalid input. ID must be a number.")
        return

    customer = session.get(Customer, customer_id)  # Fetch customer by ID
    if not customer:
        print("Customer not found.")
        return

    # Prompt user for new details (leave blank to keep old value)
    new_name = input(f"New name (leave blank to keep '{customer.name}'): ").strip()
    new_email = input(f"New email (leave blank to keep '{customer.email}'): ").strip()
    new_phone = input(f"New phone (leave blank to keep '{customer.phone}'): ").strip()

    # Update fields if user provided new values
    if new_name: customer.name = new_name
    if new_email: customer.email = new_email
    if new_phone: customer.phone = new_phone

    try:
        session.commit()  # Save changes
        print("Customer updated successfully!")
    except Exception as e:
        session.rollback()
        print(f"Error updating customer: {e}")

def delete_customer(session):
    view_customers(session)  # Show customers
    try:
        customer_id = int(input("Enter customer ID to delete: ").strip())  # Get ID
    except ValueError:
        print("Invalid input. ID must be a number.")
        return

    customer = session.get(Customer, customer_id)  # Fetch customer
    if not customer:
        print("Customer not found.")
        return

    session.delete(customer)  # Delete customer
    try:
        session.commit()
        print("Customer deleted successfully!")
    except Exception as e:
        session.rollback()
        print(f"Error deleting customer: {e}")

# ---------- MENU ITEM FUNCTIONS ----------

def add_menu_item(session):
    print("\n--- Add New Menu Item ---")
    name = input("Enter item name: ").strip()  # Get item name
    price = input("Enter price: ").strip()  # Get price

    try:
        price = float(price)  # Convert to float
    except ValueError:
        print("Invalid price. Must be a number.")
        return

    if not name:
        print("Item name is required.")
        return

    new_item = MenuItem(name=name, price=price)  # Create menu item
    session.add(new_item)
    try:
        session.commit()
        print(f"Menu item '{name}' added successfully!")
    except Exception as e:
        session.rollback()
        print(f"Error adding menu item: {e}")

def view_menu(session):
    print("\n--- Menu Items ---")
    items = session.query(MenuItem).all()  # Fetch all menu items
    if not items:
        print("No menu items found.")
    else:
        for i in items:
            print(f"[{i.id}] {i.name} - Ksh{i.price * 140:.2f}")

def update_menu_item(session):
    view_menu(session)
    try:
        item_id = int(input("Enter item ID to update: ").strip())  # Get ID
    except ValueError:
        print("Invalid input. ID must be a number.")
        return

    item = session.get(MenuItem, item_id)
    if not item:
        print("Menu item not found.")
        return

    new_name = input(f"New name (leave blank to keep '{item.name}'): ").strip()
    new_price = input(f"New price (leave blank to keep '{item.price}'): ").strip()

    if new_name:
        item.name = new_name
    if new_price:
        try:
            item.price = float(new_price)
        except ValueError:
            print("Invalid price. Skipping price update.")

    try:
        session.commit()
        print("Menu item updated successfully!")
    except Exception as e:
        session.rollback()
        print(f"Error updating menu item: {e}")

def delete_menu_item(session):
    view_menu(session)
    try:
        item_id = int(input("Enter item ID to delete: ").strip())  # Get ID
    except ValueError:
        print("Invalid input. ID must be a number.")
        return

    item = session.get(MenuItem, item_id)
    if not item:
        print("Menu item not found.")
        return

    session.delete(item)
    try:
        session.commit()
        print("Menu item deleted successfully!")
    except Exception as e:
        session.rollback()
        print(f"Error deleting menu item: {e}")

# ---------- ORDER FUNCTIONS ----------

def add_order(session):
    print("\n--- Add New Order ---")
    view_customers(session)  # Show customers
    try:
        customer_id = int(input("Enter customer ID: ").strip())  # Get customer ID
        print(f"Selected Customer ID: {customer_id}")
    except ValueError:
        print("Invalid input.")
        return

    customer = session.get(Customer, customer_id)
    if not customer:
        print("Invalid customer.")
        return

    view_menu(session)  # Show menu
    try:
        item_id = int(input("Enter menu item ID: ").strip())  # Get item ID
        print(f"Selected Menu Item ID: {item_id}")
    except ValueError:
        print("Invalid input.")
        return

    item = session.get(MenuItem, item_id)
    if not item:
        print("Invalid menu item.")
        return

    try:
        quantity = int(input("Enter quantity: ").strip())  # Get quantity
        if quantity <= 0:
            print("Quantity must be greater than 0.")
            return
    except ValueError:
        print("Invalid input. Quantity must be a number.")
        return

    new_order = Order(customer_id=customer.id, menu_item_id=item.id, quantity=quantity, status="Pending")  # Create order
    print(f"New Order: Customer ID = {new_order.customer_id}, Menu Item ID = {new_order.menu_item_id}, Quantity = {new_order.quantity}, Status = {new_order.status}")

    session.add(new_order)
    try:
        session.commit()
        print("Order added successfully!")
    except Exception as e:
        session.rollback()
        print(f"Error adding order: {e}")

def view_orders(session):
    print("\n--- All Orders ---")
    orders = session.query(Order).all()  # Fetch all orders
    if not orders:
        print("No orders found.")
    else:
        for o in orders:
            customer_name = o.customer.name if o.customer else "Unknown"
            item_name = o.menu_item.name if o.menu_item else "Unknown"
            print(f"[{o.id}] {customer_name} ordered {item_name} | Status: {o.status}")

def update_order_status(session):
    view_orders(session)
    try:
        order_id = int(input("Enter order ID to update: ").strip())  # Get order ID
    except ValueError:
        print("Invalid input.")
        return

    order = session.get(Order, order_id)
    if not order:
        print("Order not found.")
        return

    new_status = input("Enter new status (Pending/Completed/Cancelled): ").strip()
    if new_status not in ["Pending", "Completed", "Cancelled"]:
        print("Invalid status.")
        return

    order.status = new_status
    try:
        session.commit()
        print("Order status updated successfully!")
    except Exception as e:
        session.rollback()
        print(f"Error updating order: {e}")

def delete_order(session):
    view_orders(session)
    try:
        order_id = int(input("Enter order ID to delete: ").strip())  # Get order ID
    except ValueError:
        print("Invalid input.")
        return

    order = session.get(Order, order_id)
    if not order:
        print("Order not found.")
        return

    session.delete(order)
    try:
        session.commit()
        print("Order deleted successfully!")
    except Exception as e:
        session.rollback()
        print(f"Error deleting order: {e}")

# ---------- MAIN MENU ----------

def main():
    session = Session()  # Create a session for DB operations
    while True:
        print("\n===== Restaurant Ordering System =====")  # Main menu
        print("1. Manage Customers")
        print("2. Manage Menu Items")
        print("3. Manage Orders")
        print("0. Exit")
        choice = input("Select an option: ").strip()

        if choice == "1":
            manage_customers(session)
        elif choice == "2":
            manage_menu_items(session)
        elif choice == "3":
            manage_orders(session)
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

# Submenu for customers
def manage_customers(session):
    while True:
        print("\n--- Manage Customers ---")
        print("1. Add Customer")
        print("2. View Customers")
        print("3. Update Customer")
        print("4. Delete Customer")
        print("0. Back to Main Menu")
        choice = input("Select an option: ").strip()

        if choice == "1": add_customer(session)
        elif choice == "2": view_customers(session)
        elif choice == "3": update_customer(session)
        elif choice == "4": delete_customer(session)
        elif choice == "0": break
        else: print("Invalid choice.")

# Submenu for menu items
def manage_menu_items(session):
    while True:
        print("\n--- Manage Menu Items ---")
        print("1. Add Menu Item")
        print("2. View Menu")
        print("3. Update Menu Item")
        print("4. Delete Menu Item")
        print("0. Back to Main Menu")
        choice = input("Select an option: ").strip()

        if choice == "1": add_menu_item(session)
        elif choice == "2": view_menu(session)
        elif choice == "3": update_menu_item(session)
        elif choice == "4": delete_menu_item(session)
        elif choice == "0": break
        else: print("Invalid choice.")

# Submenu for orders
def manage_orders(session):
    while True:
        print("\n--- Manage Orders ---")
        print("1. Add Order")
        print("2. View Orders")
        print("3. Update Order Status")
        print("4. Delete Order")
        print("0. Back to Main Menu")
        choice = input("Select an option: ").strip()

        if choice == "1": add_order(session)
        elif choice == "2": view_orders(session)
        elif choice == "3": update_order_status(session)
        elif choice == "4": delete_order(session)
        elif choice == "0": break
        else: print("Invalid choice.")

# Entry point of the program
if __name__ == "__main__":
    main()
