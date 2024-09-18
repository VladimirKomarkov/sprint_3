from fastapi import FastAPI
from app.db.base import engine
from app.models.base import Base
from app.routers import order
from app.consumers.order_consumer import start_order_consumer
from app.consumers.notification_consumer import start_notification_consumer
import threading

app = FastAPI()

app.include_router(order.router)


@app.on_event('startup')
async def startup():
    print("App started")
    Base.metadata.create_all(bind=engine)
    threading.Thread(target=start_order_consumer, daemon=True).start()
    threading.Thread(target=start_notification_consumer, daemon=True).start()


@app.get('/')
async def read_root():
    return {"Hello": "World"}
