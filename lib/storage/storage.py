import datetime

class Storage:
    _source = ''
    _extension = ''

    def __init__(self, source, extension):
        self._source = source
        self._extension = extension

    def fileName(self):
        date = datetime.datetime.now().strftime("%Y-%m-%d-%H")

        return self._source + "_" + date + "." + self._extension
