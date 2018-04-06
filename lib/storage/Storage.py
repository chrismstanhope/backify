import os
import csv
import json
import gzip
import codecs
import datetime


class Storage:

    def file_name(self):
        date = datetime.datetime.now().strftime("%Y-%m-%d-%H")

        return 'test' + "_" + date + "." + self._extension

    def get_file_object(self, path):
        if self._compress:
            return gzip.open(path + self._file_name + '.gz', 'w')
        else:
            return open(path + self._file_name, 'w')

    def write_csv(self, source, path):
        file_object = self.get_file_object(path)

        with file_object as f:
            json_source = json.loads(source)

            writer = csv.DictWriter(f, json_source[0].keys())
            writer.writeheader()
            writer.writerows(json_source)

    def write_json(self, source, path):
        file_object = self.get_file_object(path)

        with file_object as f:
            json.dump(source, codecs.getwriter('utf-8')(f), sort_keys=True, indent=4, ensure_ascii=False)

    def remove(self, path):
        os.remove(path)

    def get_full_filepath(self):
        if self._compress:
            return self._folder_path + self._file_name + '.gz'
        else:
            return self._folder_path + self._file_name

    @staticmethod
    def is_json(source):
        is_json = True

        try:
            json.loads(source)
        except ValueError, e:
            is_json = False

        return is_json
