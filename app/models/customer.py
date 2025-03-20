from typing import Optional

from sqlalchemy.orm import DeclarativeBase, Mapped
from sqlalchemy.testing.schema import mapped_column


class Base(DeclarativeBase):
    pass


class Customer(Base):
    __tablename__ = 'customers'

    customerId: Mapped[str] = mapped_column(primary_key=True, index=True)
    companyName: Mapped[Optional[str]] = mapped_column()
    contactName: Mapped[Optional[str]] = mapped_column()
    contactTitle: Mapped[Optional[str]] = mapped_column()
    address: Mapped[Optional[str]] = mapped_column()
    city: Mapped[Optional[str]] = mapped_column()
    region: Mapped[Optional[str]] = mapped_column()
    postalCode: Mapped[Optional[str]] = mapped_column()
    country: Mapped[Optional[str]] = mapped_column()
    phone: Mapped[Optional[str]] = mapped_column()
    fax: Mapped[Optional[str]] = mapped_column()
