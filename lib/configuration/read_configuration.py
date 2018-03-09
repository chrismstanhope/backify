import json
from lib.configuration import file_location


def read_config():
    config_file = open('{0}/{1}'.format(file_location.directory, file_location.file_name), "r")

    try:
        config_dic = json.loads(config_file.readall())
    except Exception as e:
        "Error {0}".format(e.message)

    return config_dic