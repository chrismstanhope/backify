import json
from lib.configuration import file_location


def read_config():
    config_file = open('{0}/{1}'.format(file_location.directory, file_location.file_name))
    config_dic = json.load(config_file)

    return config_dic