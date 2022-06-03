from model import Product

#DynamoDB Driver
import boto3;

#making connection to DynamoDB
client = boto3.resource(
    'dynamodb',
    region_name='ap-south-1',
    aws_access_key_id='AKIAQOYUIMVCDPUYUJN5',
    aws_secret_access_key='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',
)
#product table
table = client.Table('Product')

#getoneproduct function
def get_one_product(name):
    response= table.get_item(Key={'name': name})
    return response

#getallproducts function
def get_all_products():
    response=table.scan()
    data = response['Items']
    while 'LastEvaluatedKey' in response:
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        data.extend(response['Items'])
    return data

#create function
def create_product(product):
    item=product.dict()
    result= table.put_item(
    Item={'id':item['id'],'name':item['name'],'description':item['description'],'categoryId':item['categoryId'],'brandId':item['brandId'],'comments':item['comments'],'product_qr_code':item['product_qr_code'],'metadata':item['metadata']}
    )
    return result

#update function
def update_product(name,product):
    item=product.dict()
    result=table.update_item(Key={'name':name},UpdateExpression='set name= :n,description= :d,categoryId= :c,brandId= :b,comments= :co',
    ExpressionAttributeValues={':n':item['name'],':d':item['description'],':c':item['categoryId'],':b':item['brandId'],':co':item['comments']},
    ReturnValues="UPDATED_NEW"
    )
    return result

#delete function
def delete_product(name):
    response= table.delete_item(Key={'name': name})
    return response
