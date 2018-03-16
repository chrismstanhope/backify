import unittest
from lib.source.DynamoDB import DynamoDB


class DynamoDBTest(unittest.TestCase):

    def test_backup(self):
        dynamoDB = DynamoDB('test_table')
        dynamoDB.create_backup('test_table_backup')

