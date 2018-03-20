import csv
import json
from lib.storage.Storage import Storage
from lib.storage.FileTypes import FileType
from lib.storage.Converter import Converter

class Local(Storage):

    def __init__(self, source, extension = FileType.csv):
        self._source = source
        self._extension = extension

    def write(self):
        folder_path = '/Users/danstanhope/Documents/' #this will come from config
        file_name = self.fileName()

        with open(folder_path + file_name, 'w') as file:

            if(self._extension == FileType.json):
                print("to json")
            elif(self._extension == FileType.csv):
                json_source = json.loads(self._source)

                writer = csv.DictWriter(file, json_source[0].keys())
                writer.writeheader()
                writer.writerows(json_source)

            elif(self._extension == FileType.xml):
                print("xml")
            else:
                print("invalid extension")

            #file.write(self._source);