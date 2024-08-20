from ..schemas.order import OrderCreate


def validate_order_data(order_data: OrderCreate) -> bool:
    if not order_data.customer_name or not order_data.item or order_data.quantity <= 0:
        return False
    return True
