import os
import click
import datetime

from lib.configuration import write_configuration
from lib.job.Frequency import Frequency
from lib.job.Jobs import Jobs
from lib.storage.FileTypes import FileType
from lib.storage.backup import backup


@click.command()
@click.option('--aws_access_key_id', prompt='AWS Access Key ID')
@click.option('--aws_secret_access_key', prompt='AWS Secret Access Key')
@click.option('tes--default_region_name', prompt='Default region name')
@click.option('--default_output_format', prompt='Default output format')
def configuration(aws_access_key_id, aws_secret_access_key, default_region_name, default_output_format):
    try:
        write_configuration.write_config(aws_access_key_id, aws_secret_access_key, default_region_name,
                                         default_output_format)
    except Exception as e:
        print "Unable to write config to file: {0}".format(e.message)


@click.command()
@click.option('--table_name', prompt='Enter the table name')
@click.option('--output_type', prompt='Please specify the output type (json | csv)', default='csv')
@click.option('--output_destination', prompt='Please specify the output destination (local | s3)', default='local')
def run(table_name, output_type, output_destination,):
    path = None
    time = None

    frequency = click.prompt(
        'Please Enter Frequency  (now | daily | monday | tuesday | wednesday | thursday | friday | saturday| sunday)')
    if not hasattr(Frequency, frequency.lower()):
        print "Please Enter a valid Frequency: \n now | daily | monday | tuesday | wednesday | " \
              "thursday | friday | saturday| sunday"
        exit()

    if frequency.lower() != Frequency.now:
        time = click.prompt('Enter the time of day to backup DynamoDB(24hr)')

    if output_destination.lower() == 's3':
        path = click.prompt("Please enter bucket location")
    elif output_destination.lower() == 'local':
        path = click.prompt("Please Enter folder location")
        if not os.path.exists(path):
            if click.prompt("Directoy Doesn't Exist can I create it? (y|n)") == "y":
                os.makedirs(path)
            else:
                exit()
    else:
        print "Output Type must be local or s3"
        exit()

    if not hasattr(FileType, output_type.lower()):
        print "Output Type must be json or csv"
        exit()

    if frequency.lower() == Frequency.now:
        backup(table_name, output_destination, path, output_type.lower())
    else:
        if time:
            try:
                datetime.datetime.strptime(time, '%H:%M')
            except ValueError:
                print "Incorrect data format, should be %H:%M"
                exit()

        job = Jobs()
        job.add(frequency.lower(), time, lambda: backup(table_name, output_destination, path, output_type.lower()))
        job.run()


if __name__ == '__main__':
    run()