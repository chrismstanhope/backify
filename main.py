import click
import json
import os
from os.path import expanduser

__default_configuration_directory = "{0}/.backify".format(expanduser("~"))
__default_configuration_file = "configuration"

@click.command()
@click.echo("Please provide your AWS Credentials")
@click.option('--aws_access_key_id', prompt='AWS Access Key ID')
@click.option('--aws_secret_access_key', prompt='AWS Secret Access Key')
@click.option('--default_region_name', prompt='Default region name')
@click.option('--default_output_format', prompt='Default output format')
def configuration(aws_access_key_id, aws_secret_access_key, default_region_name, default_output_format):
    config_dic = {
        'aws_access_key_id': aws_access_key_id,
        'aws_secret_access_key': aws_secret_access_key,
        'default_region_name': default_region_name,
        'default_output_format': default_output_format
    }

    if not os.path.exists(__default_configuration_directory):
        os.makedirs(__default_configuration_directory)
    file = open('{0}/{1}'.format(__default_configuration_directory, __default_configuration_file), "w")
    file.write(json.dumps(config_dic, sort_keys=True, indent=4, separators=(',', ': ')))
    file.close()

    print "Configuration file has been created at {0}/{1}".format(__default_configuration_directory,
                                                                   __default_configuration_file)

if __name__ == '__main__':
    configuration()