from lib.jobs import Jobs
from lib.schedule_frequency import Frequency


def job():
    print("I'm working...")


myobjectx = Jobs()

myobjectx.add(Frequency.daily, "10:05", job)

print(myobjectx.list())

#myobjectx.clear()

#print(myobjectx.list())

#print(myobjectx.list())

