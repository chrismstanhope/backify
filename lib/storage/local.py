from lib.storage.storage import Storage

class Local(Storage):

    def __init__(self, source, extension = 'json'):
        self._source = source
        self._extension = extension

    def write(self):
        folder_path = '/Users/danstanhope/Documents/' #this will come from config
        file_name = self.fileName()

        with open(folder_path + file_name, 'w') as file:
            file.write('testing th local storage write');