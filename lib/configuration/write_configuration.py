import os
import json
from lib.configuration import file_location


def write_config(aws_access_key_id, aws_secret_access_key, default_region_name, default_output_format):

    config_dic = {
        'aws_access_key_id': aws_access_key_id,
        'aws_secret_access_key': aws_secret_access_key,
        'default_region_name': default_region_name,
        'default_output_format': default_output_format
    }

    if not os.path.exists(file_location.directory):
        os.makedirs(file_location.directory)
    config_file = open('{0}/{1}'.format(file_location.directory, file_location.file_name), "w")
    config_file.write(json.dumps(config_dic, sort_keys=True, indent=4, separators=(',', ': ')))
    config_file.close()

    print "Configuration file has been created at {0}/{1}".format(file_location.directory, file_location.file_name)
