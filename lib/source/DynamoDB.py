from lib.configuration import read_configuration
import boto3

class DynamoDB:
    _table_name = ""
    _aws_config = {}

    def __init__(self, table_name):
        self._table_name = table_name
        self._aws_config = read_configuration.read_config()

    def getAWSClient(self):
        return boto3.client(
            'DyanmoDB',
            aws_access_key_id=self._aws_config["aws_access_key_id"],
            aws_secret_access_key=self._aws_config["aws_secret_access_key"]
        )

    def read(self):
        client = self.getAWSClient()
        client.response = client.create_backup(
            TableName='string',
            BackupName='string'
        )
