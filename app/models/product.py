# Changes for Pydantic v2+ with Annotated types
from pydantic import Field, field_validator, BaseModel
from typing import Annotated

class Product(BaseModel):
    title: str
    price: float
    image_path: str

    @field_validator('price')
    def price_must_be_positive(cls, value):
        if value <= 0:
            raise ValueError('Price must be positive')
        return value