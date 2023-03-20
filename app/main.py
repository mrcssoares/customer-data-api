from fastapi import FastAPI, Depends
from .src import models
from .src.config import engine, SessionLocal
from .src.modules.customer.routes import customer_router
app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(customer_router, tags=["customer"])
