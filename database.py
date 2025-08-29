from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///restaurant.db"  # Still SQLite but via SQLAlchemy ORM

# Create engine
engine = create_engine(DATABASE_URL, echo=True)

# Base class for models
Base = declarative_base()

# Session factory
SessionLocal = sessionmaker(bind=engine)

def get_session():
    return SessionLocal()

def init_db():
    from models import Customer, MenuItem, Order  # I Import models here to avoid circular import
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()
    print("✅ Database and tables created successfully!")
