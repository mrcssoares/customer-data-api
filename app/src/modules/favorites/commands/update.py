from sqlalchemy.orm import Session
from app.src.models import Customer
from app.src.modules.customer.schemas import CustomerBase
from app.src.modules.customer.exceptions import CustomerNotFound, CustomerException


def update(db: Session, customer_id: int,  customer_data: CustomerBase):
    customer = db.query(Customer).filter(
        Customer.id == customer_id).first()
    if customer is None:
        CustomerNotFound(customer_id=customer_id)

    already_exists = db.query(Customer).filter(
        Customer.email == customer_data.email).first()
    if already_exists and customer.email != customer_data.email:
        CustomerException(message='Email already exist')

    customer.email = customer_data.email
    customer.name = customer_data.name

    db.commit()
    db.refresh(customer)

    return customer
