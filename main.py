from lib.job.jobs import Jobs
from lib.job.frequency import Frequency
from lib.storage.local import Local
from lib.storage.s3 import S3


#def job():
#    print("I'm working...")


#myobjectx = Jobs()

#myobjectx.add(Frequency.tuesday, "10:09", job)

#print(myobjectx.list())

#myobjectx.run()
#myobjectx.clear()

#print(myobjectx.list())

#print(myobjectx.list())

#schedule.every(1).minutes.do(function)

local_storage = Local("test_file_name")
s3_storage = S3("s3_bucket_name")

local_storage.write()

s3_storage.write()