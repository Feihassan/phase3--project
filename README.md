# Restaurant Ordering System

This is a Python-based CLI application for managing restaurant orders. The system allows users to interact with a database of menu items, place orders, and manage restaurant operations.

## Features

- **Menu Management**: View and manage menu items.
- **Order Management**: Place, view, and manage customer orders.
- **Database Integration**: Uses SQLite for data storage.
- **Seed Data**: Pre-populated database with sample data for testing.

## Project Structure

```
Restaurant_ordering/
├── cli.py          # Command-line interface for the application
├── database.py     # Database connection and setup
├── seed.py         # Script to seed the database with initial data
├── models/         # Contains ORM models for the database
│   ├── __init__.py
│   └── models.py
├── restaurant.db   # SQLite database file
├── Pipfile         # Pipenv dependencies
├── Pipfile.lock    # Locked Pipenv dependencies
└── README.md       # Project documentation
```

## Requirements

- Python 3.8 or higher
- Pipenv for dependency management

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Feihassan/phase3--project.git
   cd Restaurant_ordering
   ```

2. Install dependencies:
   ```bash
   pipenv install
   ```

3. Activate the virtual environment:
   ```bash
   pipenv shell
   ```

4. Seed the database:
   ```bash
   python seed.py
   ```

## Usage

Run the CLI application:
```bash
python cli.py
```

Follow the on-screen instructions to interact with the system.

## Contributing

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Submit a pull request with a detailed description of your changes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments

- SQLite for database management.
- Pipenv for dependency management.