import typing

from pydantic import BaseModel


class ProductPrice(BaseModel):
    product_price: int
    product_discount_price: typing.Any


class ProductDetail(BaseModel):
    product_name: str
    product_link: str
    price: ProductPrice
    product_from: str
