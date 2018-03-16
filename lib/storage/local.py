import csv
import json
from lib.storage.storage import Storage
from lib.storage.FileTypes import FileType

class Local(Storage):

    def __init__(self, source, extension = FileType.json):
        self._source = source
        self._extension = extension

    def write(self):
        folder_path = '/Users/stanhope/Documents/' #this will come from config
        file_name = self.fileName()

        json_data = '{"name": "smith", "email": "smithjack @ gmail.com"}'

        with open(folder_path + file_name, 'w') as file:

            if(self._extension == FileType.json):
                print('json')
            elif(self._extension == FileType.json):
                print('csv')

            file.write(self._source);