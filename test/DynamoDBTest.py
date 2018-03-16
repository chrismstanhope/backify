import unittest
from lib.job.jobs import Jobs
from lib.job.frequency import Frequency
from lib.source.DynamoDB import DynamoDB
from lib.storage.local import Local
from lib.storage.storage import Storage


class DynamoDBTest(unittest.TestCase):
    def backup(self):
        print "stating backup"
        dynamoDB = DynamoDB('test_table')
        data = dynamoDB.create_backup("test")
        print data
        storage = Local(data)
        storage.write()

    def test_backup(self):
        dynamoDB = DynamoDB('test_table')
        dynamoDB.create_backup('test_table_backup')

    def test_scheduler(self):
        job = Jobs()
        job.add(Frequency.day, '21:49', self.backup)
        job.run()