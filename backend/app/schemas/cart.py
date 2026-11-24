from pydantic import BaseModel, Field
from typing import Optional

class CartItemBase(BaseModel):
    product_id: int = Field(..., description="product id")
    quantity: int = Field(..., gt=0, description="quantity (must be greater than 0)")

class CartItemCreate(CartItemBase):
    pass

class CartItemUpdate(BaseModel):
    product_id: int = Field(..., description="product id")
    quantity: int = Field(..., gt=0, description="new quantity (must be greater than 0)")

class CartItem(BaseModel):
    product_id: int
    name: str = Field(..., description="product name")
    price: float = Field(..., description="product price")
    quantity: int = Field(..., description="quantity in cart")
    subtotal: float = Field(..., description="subtotal price for this item (price * quantity)")
    image_url: Optional[str] = Field(None, description="product image url")

class CartResponse(BaseModel):
    items: list[CartItem] = Field(..., description="list of items in the cart")
    total: float = Field(..., description="total cart price")
    items_count: int = Field(..., description="total number of items in cart")
