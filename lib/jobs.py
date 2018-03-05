import schedule
import time
import datetime
from lib.schedule_frequency import Frequency

class Jobs:

    def list(self):
        return schedule.jobs

    def clear(self):
        return schedule.clear()

    def add(self, frequency, time, function):

        self.validateFrequency(frequency)
        self.validateTime(time)
        self.validateFunction(function)

        #schedule.every(1).minutes.do(function)

    def validateFrequency(self, frequency):
        if not hasattr(Frequency, frequency):
            raise TypeError('frequency must be an instance of Frequency Enum')

    def validateTime(self, time):
        timeformat = "%H:%M"
        try:
            return datetime.datetime.strptime(time, timeformat)
        except ValueError:
            raise TypeError('time must be in specified in H:M format')

    def validateFunction(self, function):
        if not callable(function):
            raise TypeError('function must be passed in order to schedule job')