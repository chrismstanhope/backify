from lib.jobs import Jobs
from lib.frequency import Frequency


def job():
    print("I'm working...")


myobjectx = Jobs()

myobjectx.add(Frequency.tuesday, "10:09", job)

print(myobjectx.list())

myobjectx.run()
#myobjectx.clear()

#print(myobjectx.list())

#print(myobjectx.list())



#schedule.every(1).minutes.do(function)