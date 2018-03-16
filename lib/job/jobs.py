import time
import uuid
import schedule
import datetime
from lib.job.frequency import Frequency

class Jobs:
    def uuid(self):
        return str(uuid.uuid4())

    def list(self):
        return schedule.jobs

    def clear(self, tag = ''):
        if tag != '':
            schedule.clear(tag)
        else:
            schedule.clear()

    def add(self, frequency, job_time, function):
        job_time = self.validateTime(job_time)
        uuid_tag = self.uuid()

        self.validateFrequency(frequency)
        self.validateFunction(function)

        if frequency == Frequency.day:
            schedule.every().day.at(job_time).do(function).tag(uuid_tag)
        elif frequency == Frequency.week:
            schedule.every().week.at(job_time).do(function).tag(uuid_tag)
        elif frequency == Frequency.monday:
            schedule.every().monday.at(job_time).do(function).tag(uuid_tag)
        elif frequency == Frequency.tuesday:
            schedule.every().tuesday.at(job_time).do(function).tag(uuid_tag)
        elif frequency == Frequency.wednesday:
            schedule.every().wednesday.at(job_time).do(function).tag(uuid_tag)
        elif frequency == Frequency.thursday:
            schedule.every().thursday.at(job_time).do(function).tag(uuid_tag)
        elif frequency == Frequency.friday:
            schedule.every().friday.at(job_time).do(function).tag(uuid_tag)
        elif frequency == Frequency.saturday:
            schedule.every().saturday.at(job_time).do(function).tag(uuid_tag)
        elif frequency == Frequency.sunday:
            schedule.every().sunday.at(job_time).do(function).tag(uuid_tag)
        elif frequency == Frequency.now:
            #TODO implement a way to run job after download and not schedule
            print("now")

    def run(self):
        while True:
            schedule.run_pending()
            time.sleep(1)

    def validateTime(self, time):
        if(len(time.split(":")) == 1):
            time = time + ":00"

        timeformat = "%H:%M"

        try:
            datetime.datetime.strptime(time, timeformat)

            return time
        except ValueError:
            raise TypeError('time must be in specified in H:M format')

    def validateFrequency(self, frequency):
        if not hasattr(Frequency, frequency):
            raise TypeError('frequency must be an instance of Frequency Enum')

    def validateFunction(self, function):
        if not callable(function):
            raise TypeError('function must be passed in order to schedule job')