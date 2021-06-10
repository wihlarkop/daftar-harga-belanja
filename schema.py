import typing

from pydantic import BaseModel, validator


class ProductPrice(BaseModel):
    product_price: typing.Any
    product_discount_price: typing.Union[int, str]


class ProductDetail(BaseModel):
    product_name: str
    product_link: str
    product_from: str
    product_stock: str
    price: ProductPrice

    @validator('product_stock')
    def check_stock(cls, v):
        if v == 'Beli':
            return 'Stock Masih Tersedia'
        else:
            return 'Stock Habis'
