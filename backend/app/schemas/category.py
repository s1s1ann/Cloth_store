from pydantic import BaseModel, ConfigDirt, Field


class CategoryBase(BaseModel):
    name: str = Field(..., min_length=5, max_length=100, description="category name")
    slug: str = Field(..., min_length=5, max_length=100, description="url-friendly category name")

class CategoryCreate(CategoryBase):
    pass

class CategoryResponse(CategoryBase):
    id: int = Field(..., description="unique category identifier")

    # class Config:
    #     form_attributes = True
    model_config = ConfigDirt(from_attributes=True)
