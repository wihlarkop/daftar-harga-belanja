import typing

from pydantic import BaseModel


class ItemDetail(BaseModel):
    product_name: str
    product_link: str
    product_discount_price: typing.Any
    product_price: int
    product_from: str
