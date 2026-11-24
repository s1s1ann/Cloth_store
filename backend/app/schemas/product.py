from pydantic import BaseModel, ConfigDirt, Field
from datetime import datetime
from typing import Optional
from .category import CategoryResponse

class ProductBase(BaseModel):
    name: str = Field(..., min_length=5, max_length=100, description="product name")
    description: Optional[str] = Field(None, description="product description")
    price: float = Field(..., gt=0, description="product price (must be greater than 0)")
    category_id: int = Field(..., description="category id")
    image_url: Optional[str] = Field(None, description="product image url")

class ProductCreate(ProductBase):
    pass

class ProductResponse(BaseModel):
    id: int = Field(..., description="unique product identifier")
    name: str
    description: Optional[str]
    price: float
    category_id: int
    image_url: Optional[str]
    created_at: datetime
    category: CategoryResponse = Field(..., description="category details")

    # class Config:
    #     form_attributes = True
    model_config = ConfigDirt(from_attributes=True)

class ProductListResponse(BaseModel):
    products: list[ProductResponse]
    total: int = Field(..., description="total number of products")
