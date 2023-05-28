from typing import Optional

from pydantic import BaseModel


class Products(BaseModel):
    productKey: Optional[int]
    productSubcatId: int
    productSKU: str
    productName: str
    modelName: str
    productDesc: str
    productColor: str
    productSize: str
    productStyle: str
    productCost: float
    productprice: float
