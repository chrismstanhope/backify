import os
import boto3
from os.path import expanduser
from lib.storage.Storage import Storage
from lib.storage.FileTypes import FileType
from lib.configuration import read_configuration


class S3(Storage):

    def __init__(self, source, bucket_name, extension=FileType.csv, compress=True):
        self._compress = compress
        self._source = source
        self._extension = extension
        self._bucket_name = bucket_name
        self._file_name = self.file_name()
        self._aws_config = read_configuration.read_config()
        self._folder_path = "{0}/.backify/tmp/".format(expanduser("~"))
        self._directory = os.path.dirname(self._folder_path)

    def getAWSResource(self):
        return boto3.resource(
            's3',
            aws_access_key_id=self._aws_config["aws_access_key_id"],
            aws_secret_access_key=self._aws_config["aws_secret_access_key"],
            region_name=self._aws_config['default_region_name']
        )

    def write(self):
        resource = self.getAWSResource()

        if not os.path.exists(self._directory):
            os.makedirs(self._directory)

        print(self._file_name)
        if self._extension == FileType.json:
            self.write_json(self._source, self._folder_path)
        elif self._extension == FileType.csv:
            self.write_csv(self._source, self._folder_path)
        else:
            print("invalid extension")

        file_source = open(self.get_full_filepath(), 'rb')

        resource.Bucket(self._bucket_name).put_object(Key=self._file_name, Body=file_source)

        self.remove(self.get_full_filepath())