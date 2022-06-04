from pydantic import BaseModel

class Product(BaseModel):
    id:str
    productname:str
    description:str
    categoryId:str
    brandId:str
    comments:str
    product_qr_code:str
    metadata:str
