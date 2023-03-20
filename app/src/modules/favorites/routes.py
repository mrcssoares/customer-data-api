from fastapi import APIRouter, HTTPException, Path, Depends, Query, status
from sqlalchemy.orm import Session
from .schemas import RequestCustomerCreate, CustomerSchema, RequestCustomerUpdate
from app.src.config import get_db
from app.src.modules.customer.commands.list_one import list_one
from app.src.modules.customer.commands.create import create
from app.src.modules.customer.commands.update import update
from app.src.modules.customer.commands.remove import remove


customer_router = APIRouter()


@customer_router.get("/favorite/{customer_id}", response_model=CustomerSchema)
async def get(customer_id: int, db: Session = Depends(get_db)):
    return list_one(db, customer_id)


@customer_router.post("/favorite")
async def post(request: RequestCustomerCreate, db: Session = Depends(get_db)):
    return create(db, customer=request.parameter)


@customer_router.patch("/favorite/{customer_id}", response_model=CustomerSchema)
async def patch(customer_id: int, request: RequestCustomerUpdate, db: Session = Depends(get_db)):
    return update(db, customer_id, customer_data=request.parameter)


@customer_router.delete("/favorite/{customer_id}")
async def delete(customer_id: int, db: Session = Depends(get_db)):
    return remove(db, customer_id)
