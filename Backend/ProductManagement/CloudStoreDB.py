import boto3

class CloudStoreDB:

    def __init__(self,region_name,aws_access_key_id,aws_secret_access_key,resource='dynamodb'):

        self.region_name=region_name
        self.aws_access_key_id=aws_access_key_id
        self.aws_secret_access_key=aws_secret_access_key
        self.resource=resource
        self.databaseConnection=None
        self.tablecache={}
        self.isConnected=False
        self.databaseConnect()


    def databaseConnect(self):
        self.databaseConnection=boto3.resource(
                self.resource,
                region_name=self.region_name,
                aws_access_key_id=self.aws_access_key_id,
                aws_secret_access_key=self.aws_secret_access_key,
            )
        self.isConnected=True

    def getTableConnect(self,tablename:str):
        if self.isConnected:
            if tablename in self.tablecache:
                return self.tablecache[tablename]
            else:
                table = self.databaseConnection.Table(tablename)
                # if no errors
                self.tablecache[tablename] = table
                return self.tablecache[tablename]
        else:
            self.databaseConnect()
            self.getTableConnect(tablename)
