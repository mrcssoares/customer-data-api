from typing import List
from pydantic import BaseModel, Field


class CustomerBase(BaseModel):
    name: str
    email: str


class CustomerCreate(CustomerBase):
    password: str


class CustomerSchema(CustomerBase):
    id: int

    class Config:
        orm_mode = True


class RequestCustomerCreate(BaseModel):
    parameter: CustomerCreate = Field(...)


class RequestCustomerUpdate(BaseModel):
    parameter: CustomerBase = Field(...)
