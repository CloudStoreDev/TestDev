from ProductModel import Product
from CloudStoreDB import CloudStoreDB

class ProductService:
    TABLENAME='Product'
    def __init__(self,databaseConnection:CloudStoreDB):
        self.databaseConnection=databaseConnection
        self.table=databaseConnection.getTableConnect(ProductService.TABLENAME)

    #getoneproduct function
    def get_one_product(self,id:str):
        response= self.table.get_item(Key={'id': id})
        result = response['Item']
        return result


    #getallproducts function
    def get_all_products(self):
        response=self.table.scan()
        data = response['Items']
        while 'LastEvaluatedKey' in response:
            response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
            data.extend(response['Items'])
        return data

    #create function
    def create_product(self,product):
        item=product.dict()
        result= self.table.put_item(
        Item={'id':item['id'],'productname':item['productname'],'description':item['description'],'categoryId':item['categoryId'],'brandId':item['brandId'],'comments':item['comments'],'product_qr_code':item['product_qr_code'],'metadata':item['metadata']}
        )

        return result["ResponseMetadata"]["HTTPStatusCode"]

    #update function
    def update_product(self,id,product):
        item=product.dict()
        result=self.table.update_item(Key={'id':id},UpdateExpression='set productname= :n,description= :d,categoryId= :c,brandId= :b,comments= :co',
        ExpressionAttributeValues={':n':item['productname'],':d':item['description'],':c':item['categoryId'],':b':item['brandId'],':co':item['comments']},
        ReturnValues="UPDATED_NEW"
        )
        return result

    #delete function
    def delete_product(self,id):
        response= self.table.delete_item(Key={'id': id})
        return response

'''
if __name__ == '__main__':
    db:CloudStoreDB=CloudStoreDB('ap-south-1','AKIAQOYUIMVCDPUYUJN5','pIP+CWaEraicE0qLId2a6kyLH/kymmaUKYXuepbO')
    service=ProductService(db)

    res = service.get_one_product('777')
    print(res)
'''
