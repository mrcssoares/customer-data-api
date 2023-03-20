from sqlalchemy.orm import Session
from app.src.models import Customer
from app.src.modules.customer.schemas import CustomerCreate
from app.src.modules.customer.exceptions import CustomerException


def create(db: Session, customer: CustomerCreate):
    already_exists = db.query(Customer).filter(
        Customer.email == customer.email).first()
    if already_exists:
        CustomerException(message='Email already exist')

    new_customer = Customer(name=customer.name,
                            email=customer.email, password=customer.password)
    db.add(new_customer)
    db.commit()

    return {"message": "Customer created successfully"}
