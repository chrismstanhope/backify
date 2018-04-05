from lib.source.DynamoDB import DynamoDB
from lib.storage.Local import Local
from lib.storage.S3 import S3


def backup(table_name, location, location_path, file_type):
    print "stating backup"
    dynamo_db = DynamoDB(table_name)
    data = dynamo_db.create_backup()

    if location.lower() == 'local':
        storage = Local(data, location_path, file_type)
    elif location.lower() == 's3':
        storage = S3(data, location_path, file_type)
    else:
        raise Exception("Invalid save location")
    storage.write()
