from pydantic import BaseModel

class Product(BaseModel):
    id:str
    name:str
    description:str
    categoryId:str
    brandId:str
    comments:str
    product_qr_code:str
    metadata:str
