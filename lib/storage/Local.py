from lib.storage.Storage import Storage
from lib.storage.FileTypes import FileType
from lib.storage.Converter import Converter

class Local(Storage):

    def __init__(self, source, extension = FileType.json):
        self._source = source
        self._extension = extension

    def write(self):
        folder_path = '/Users/danstanhope/Documents/' #this will come from config
        file_name = self.fileName()

        with open(folder_path + file_name, 'w') as file:

            if(self._extension == FileType.json):
                Converter.toJSON(self._source)
            elif(self._extension == FileType.csv):
                Converter.toCSV(self._source)
            elif(self._extension == FileType.xml):
                Converter.toXML(self._source)
            else:
                print("invalid extension")

            #file.write(self._source);