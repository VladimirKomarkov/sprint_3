from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

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
    total_price: float
    status: str


