from lib.storage.storage import Storage

class S3(Storage):

    def __init__(self, source, extension = 'json'):
        self._source = source
        self._extension = extension

    def write(self):
        file_name = self.fileName()

        print(file_name)
