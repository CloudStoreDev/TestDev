from fastapi import FastAPI,HTTPException
from fastapi.middleware.cors import CORSMiddleware
from model import Product
from database import(
get_one_product,
get_all_products,
create_product,
update_product,
delete_product
)



#app object
app=FastAPI()

# origins=['http://localhost:3000']
#app.add_middleware(
# CORSMiddleware,allow_origins=origins,allow_Credentials=True,
#allow_methods=["*"],allow_headers=["*"])

@app.get("/")
def read_root():
    return {"ping":"pong"}

@app.get("/api/product")
async def getAllProducts():
    response=await get_all_products()
    return response

@app.get("/api/product{name}",response_model=Product)
aync def getOneProduct(name):
    response=await get_one_product(name)
    if response:
        return response
    raise HTTPException(404,f"There is no product with this name {name}")

@app.post("/api/product",response_model=Product)
aync def createProduct(product:Product):
    response=await create_product(product.dict())
    if response:
        return response
    raise HTTPException(400,"Bad Request")


@app.put("/api/product{name}/",response_model=Product)
async def updateProduct(name:str,data:Product):
    response=await update_product(name,data.dict())
    if response:
        return response
    raise HTTPException(404,f"There is no product with this name {name}")


@app.delete("/api/product{name}")
async def deleteProduct(name):
    response=await delete_product(name)
    if response:
        return "Successfully Deleted Product Item"
    raise HTTPException(404,f"There is no product with this name {name}")
