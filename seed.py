from database import get_session, init_db
from models import Customer, MenuItem, Order

def seed_data():
    session = get_session()

    # Clear existing data
    session.query(Order).delete()
    session.query(MenuItem).delete()
    session.query(Customer).delete()
    session.commit()

    # Add customers
    customers = [
        Customer(name="Alice Johnson", email="alice@example.com"),
        Customer(name="Bob Smith", email="bob@example.com"),
        Customer(name="Charlie Brown", email="charlie@example.com")
    ]
    session.add_all(customers)

    # Add menu items with categories
    menu_items = [
        MenuItem(name="Margherita Pizza", price=8.99, category="Pizza"),
        MenuItem(name="Pepperoni Pizza", price=10.99, category="Pizza"),
        MenuItem(name="Cheeseburger", price=9.49, category="Burgers"),
        MenuItem(name="Veggie Burger", price=8.49, category="Burgers"),
        MenuItem(name="Caesar Salad", price=7.99, category="Salads"),
        MenuItem(name="Greek Salad", price=8.49, category="Salads")
    ]
    session.add_all(menu_items)

    # Add sample orders
    orders = [
        Order(customer=customers[0], menu_item=menu_items[0], quantity=2),
        Order(customer=customers[1], menu_item=menu_items[2], quantity=1),
        Order(customer=customers[2], menu_item=menu_items[4], quantity=3)
    ]
    session.add_all(orders)

    session.commit()
    print("✅ Database seeded with sample data!")

if __name__ == "__main__":
    init_db()  # Ensure tables exist
    seed_data()
