import click
from lib.configuration import write_configuration


@click.command()
##@click.echo("Please provide your AWS Credentials")
@click.option('--aws_access_key_id', prompt='AWS Access Key ID')
@click.option('--aws_secret_access_key', prompt='AWS Secret Access Key')
@click.option('--default_region_name', prompt='Default region name')
@click.option('--default_output_format', prompt='Default output format')
def configuration(aws_access_key_id, aws_secret_access_key, default_region_name, default_output_format):
    try:
        write_configuration.write_config(aws_access_key_id, aws_secret_access_key, default_region_name,
                                         default_output_format)
    except Exception as e:
        print "Unable to write config to file: {0}".format(e.message)

if __name__ == '__main__':
    configuration()