import json
import datetime


class Storage:
    _source = ''
    _extension = ''

    def __init__(self, source, extension):
        self._source = source
        self._extension = extension

    def fileName(self):
        date = datetime.datetime.now().strftime("%Y-%m-%d-%H")

        return 'test' + "_" + date + "." + self._extension

    @staticmethod
    def toJSON(source):
        is_json = True

        try:
            json.loads(source)
        except ValueError, e:
            is_json = False

        return is_json
