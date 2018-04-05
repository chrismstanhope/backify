import json
import boto3
from lib.configuration import read_configuration
from lib.source.DecimalEncoder import DecimalEncoder

class DynamoDB:
    _table_name = ""
    _aws_config = {}

    def __init__(self, table_name):
        self._table_name = table_name
        self._aws_config = read_configuration.read_config()

    def getAWSResource(self):
        return boto3.resource(
            'dynamodb',
            aws_access_key_id=self._aws_config["aws_access_key_id"],
            aws_secret_access_key=self._aws_config["aws_secret_access_key"],
            region_name=self._aws_config['default_region_name']
        )
    def getTableItems(self):
        resource = self.getAWSResource()
        table = resource.Table(self._table_name)
        results = table.scan()
        return results

    def create_backup(self):
        results = self.getTableItems()
        return json.dumps(results["Items"], cls=DecimalEncoder)

