from typing import List

from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.session import get_db_session
from app.models.customer import Customer
from app.schemas.customer import CustomerSchema

router = APIRouter()


@router.get('/customers', response_model=List[CustomerSchema])
async def get_customers(db: Session = Depends(get_db_session)):
    customers = db.scalars(select(Customer)).all()
    response = [CustomerSchema.model_validate(customer) for customer in customers]
    return response


@router.get('/customers/{customer_id}', response_model=CustomerSchema)
async def get_customer(customer_id: str, db: Session = Depends(get_db_session)):
    customer = db.get(Customer, customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return CustomerSchema.model_validate(customer)


@router.post('/customers', response_model=CustomerSchema)
async def add_customer(customer: CustomerSchema, db: Session = Depends(get_db_session)):
    newCustomer = Customer(**customer.model_dump())
    db.add(newCustomer)
    db.commit()
    db.refresh(newCustomer)
    return CustomerSchema.model_validate(newCustomer)
