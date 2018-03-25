import unittest
from lib.job.Jobs import Jobs
from lib.job.Frequency import Frequency
from lib.source.DynamoDB import DynamoDB
from lib.storage.Local import Local
from lib.storage.S3 import S3
from lib.storage.Storage import Storage


class DynamoDBTest(unittest.TestCase):
    def backup(self):
        print "stating backup"
        dynamoDB = DynamoDB('test_table')
        data = dynamoDB.create_backup("test")
        print data
        #storage = Local(data)
        #storage.write()

        storage = S3(data)
        storage.write()

    def test_backup(self):
        dynamoDB = DynamoDB('test_table')
        dynamoDB.create_backup('test_table_backup')

    def test_scheduler(self):
        job = Jobs()
        job.add(Frequency.day, '17:57', self.backup)
        job.run()