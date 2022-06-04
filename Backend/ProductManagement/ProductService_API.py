from fastapi import FastAPI,HTTPException
from fastapi.middleware.cors import CORSMiddleware
from ProductModel import Product
from CloudStoreDB import CloudStoreDB
from ProductService import ProductService




#app object
app=FastAPI()

db:CloudStoreDB=CloudStoreDB('ap-south-1','AKIAQOYUIMVCDPUYUJN5','pIP+CWaEraicE0qLId2a6kyLH/kymmaUKYXuepbO')
productservice=ProductService(db)


# origins=['http://localhost:3000']
#app.add_middleware(
# CORSMiddleware,allow_origins=origins,allow_Credentials=True,
#allow_methods=["*"],allow_headers=["*"])



@app.get("/")
def read_root():
    return {"ping":"pong"}

@app.get("/api/product")
async def getAllProducts():
    response=productservice.get_all_products()
    return response

@app.get("/api/product{id}",response_model=Product)
async def getOneProduct(id):
    response=productservice.get_one_product(id)
    if response:
        return response
    raise HTTPException(404,f"There is no product with this id {id}")

@app.post("/api/product")
async def createProduct(product:Product):
    response=productservice.create_product(product)
    if response==200:
        return "Successfully created product"
    raise HTTPException(400,"Bad Request")


@app.put("/api/product{id}/",response_model=Product)
async def updateProduct(id:str,data:Product):
    response=productservice.update_product(id,data)
    if response:
        return "Successfully updated product with id {id}"
    raise HTTPException(404,f"There is no product with this id {id}")


@app.delete("/api/product{id}")
async def deleteProduct(id):
    response=productservice.delete_product(id)
    if response:
        return "Successfully Deleted Product Item"
    raise HTTPException(404,f"There is no product with this id {id}")
