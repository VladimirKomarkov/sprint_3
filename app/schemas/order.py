from pydantic import BaseModel


class OrderCreate(BaseModel):
    customer_name: str
    item: str
    quantity: int
    total_price: float
    status: str


class OrderResponse(BaseModel):
    id: int
    customer_name: str
    item: str
    quantity: int
    status: str

    class Config:
        orm_model = True
