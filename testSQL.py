import MySQLdb
conn = MySQLdb.connect(host="teccolabs.com", user="teccol5_fathhome",passwd="YuC4aB5N",db="teccol5_fathtest");
cursor = conn.cursor()

from spyrk import SparkCloud

##USERNAME = 'ark02@umail.ucsb.edu'
##PASSWORD = ''

ACCESS_TOKEN = 'da4b33d549355054712269e30b7f9d6240d73e24'
spark = SparkCloud(ACCESS_TOKEN)

##print spark.devices
spark.devices['dozen_mighty']

print spark.dozen_mighty.functions
print spark.dozen_mighty.variables

print spark.dozen_mighty.BoxPressure
