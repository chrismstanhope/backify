from lib.storage.Storage import Storage
from lib.storage.FileTypes import FileType


class Local(Storage):

    def __init__(self, source, folder_path, extension=FileType.csv, compress=True):
        self._compress = compress
        self._source = source
        self._extension = extension
        self._file_name = self.file_name()
        self._folder_path = folder_path

    def write(self):
        if self._extension == FileType.json:
            self.write_json(self._source, self._folder_path)
        elif self._extension == FileType.csv:
            self.write_csv(self._source, self._folder_path)
        else:
            print("invalid extension")
