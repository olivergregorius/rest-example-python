from typing import List

from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.session import get_db_session
from app.models.customer import Customer
from app.schemas.customer import CustomerSchema

router = APIRouter()

@router.get("/customers", response_model=List[CustomerSchema])
async def get_customers(db: Session = Depends(get_db_session)):
    customers = db.scalars(select(Customer)).all()
    return customers
