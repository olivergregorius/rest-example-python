from pydantic import BaseModel


class CustomerSchema(BaseModel):
    customerId: str
    companyName: str | None
    contactName: str | None
    contactTitle: str | None
    address: str | None
    city: str | None
    region: str | None
    postalCode: str | None
    country: str | None
    phone: str | None
    fax: str | None
