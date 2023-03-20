from sqlalchemy.orm import Session
from app.src.models import Customer
from app.src.modules.customer.schemas import CustomerSchema
from app.src.modules.customer.exceptions import CustomerNotFound


def remove(db: Session, id: int):
    customer = db.query(Customer).filter(
        Customer.id == id).first()

    if customer is None:
        CustomerNotFound(customer_id=id)

    db.delete(customer)
    db.commit()

    return {"message": "Customer deleted successfully"}
