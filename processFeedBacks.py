import csv
from sqlalchemy import create_engine
import base64
import os

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

db_string = "postgres://xhbzhbafkdxrar:8b8215b86776c132f55cc829c96ddc821d3ae50f5bcd07f9e27a84d54853fb75@ec2-174-129-32-37.compute-1.amazonaws.com:5432/d93uramn84njs4"

db = create_engine(db_string)
result_ver_poster = db.execute("SELECT version,id,userid,duration,feedback FROM feedbacks where userid like 'A%%'")
print(type(result_ver_poster))
# for row in result_ver_poster:
#      b = base64.b64decode(row[4][22:])
#      mp3file = open(THIS_FOLDER +"/voice/posterVer+"+row[2]+"+"+row[2]+".mp3", "wb")
#      mp3file.write(b)
#      mp3file.close()


with open('results/feedbacks_r_1.csv','w') as csv_file:
    w = csv.writer(csv_file, result_ver_poster.keys())
    #w.writeheader()
    w.writerow(("version","id","userid","duration","feedback"))

    for row in result_ver_poster:
        w.writerow(row)
