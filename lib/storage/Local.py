import csv
import json
import gzip
import codecs
from lib.storage.Storage import Storage
from lib.storage.FileTypes import FileType


class Local(Storage):

    def __init__(self, source, extension=FileType.csv, compress=True):
        self._compress = compress
        self._source = source
        self._extension = extension

        folder_path = '/Users/danstanhope/Documents/'  # this will come from config
        file_name = self.fileName()

        if(self._compress):
            self._file_object = gzip.open(folder_path + file_name + '.gz', 'w')
        else:
            self._file_object = open(folder_path + file_name, 'w')

    def write(self):
        if(self._extension == FileType.json):
            self.__write_json(self._source)
        elif(self._extension == FileType.csv):
            self.__write_csv(self._source)
        else:
            print("invalid extension")

    def __write_csv(self, source):
        with self._file_object as f:
            json_source = json.loads(source)

            writer = csv.DictWriter(f, json_source[0].keys())
            writer.writeheader()
            writer.writerows(json_source)

    def __write_json(self, source):
        with self._file_object as f:
            json.dump(source, codecs.getwriter('utf-8')(f), sort_keys=True, indent=4, ensure_ascii=False)
