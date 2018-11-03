import csv
from sqlalchemy import create_engine
import base64
import os

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

db_string = "postgres://xhbzhbafkdxrar:8b8215b86776c132f55cc829c96ddc821d3ae50f5bcd07f9e27a84d54853fb75@ec2-174-129-32-37.compute-1.amazonaws.com:5432/d93uramn84njs4"

db = create_engine(db_string)
#result_ver_poster = db.execute("SELECT id,userid,queryname,text,mp3url FROM results where userid like 'A%%'")
result_ver_easy = db.execute("SELECT id,userid,category,queryname,text,mp3url,datetime FROM results_ver_easy where userid like 'A%%'")
#result_ver_easy = db.execute("SELECT id,userid,category,queryname,text,mp3url,datetime FROM results_ver_easy where userid like 'A2KYOM2ZGYDJGT'")
#result_ver_game = db.execute("SELECT id,userid,queryname,text,mp3url,answerTime FROM results_ver_game where userid like 'A%%'")
#result_ver_game = db.execute("SELECT * FROM results_ver_game where userid like 'A%%'") #id,userid,text,mp3url,queryname,answerTime,datetime,category,answertime2

#print(type(result_ver_poster))
# for row in result_ver_poster:
#      b = base64.b64decode(row[4][22:])
#      mp3file = open(THIS_FOLDER +"/voice/posterVer+"+row[2]+"+"+row[2]+".mp3", "wb")
#      mp3file.write(b)
#      mp3file.close()


with open('results/results_ver6.csv','w') as csv_file:
    w = csv.writer(csv_file, result_ver_easy.keys())
    #w.writeheader()
    w.writerow(("version","id","userid","category","queryname","text","mp3Link","timestamp"))

    # for row in result_ver_poster:
    #      row1 = []
    #      row1.append("posterVer")
    #      row1.append(row[0])
    #      row1.append(row[1])
    #      row1.append(row[2])
    #      row1.append(row[3])
    #
    #      tmp="[]&#39;,➕"
    #      for char in tmp:
    #          row1[3] = row1[3].replace(char,"") #modify the queryName
    #
    #      b = base64.b64decode(row[4][22:])
    #      mp3fileName=THIS_FOLDER +"/voice1/posterVer+"+row1[3]+"+"+row[1]+".mp3"
    #      mp3file = open(mp3fileName, "wb")
    #      mp3file.write(b)
    #      mp3file.close()
    #
    #      mp3fileName = "file://"+mp3fileName
    #      row1.append("=HYPERLINK(\""+mp3fileName+"\")")
    #      w.writerow(row1)

    for row in result_ver_easy:

         row1 = []
         row1.append("easyVer")
         row1.append(row[0])
         row1.append(row[1])
         row1.append(row[2])
         row1.append(row[3])
         row1.append(row[4])


         tmp="[]&#39;,➕"
         for char in tmp:
             row1[4] = row1[4].replace(char,"") #modify the queryName

         b = base64.b64decode(row[5][22:])
         mp3fileName=THIS_FOLDER +"/results/voice6/easyVer+"+row1[4]+"+"+row[1]+".mp3"
         mp3file = open(mp3fileName, "wb")
         mp3file.write(b)
         mp3file.close()

         mp3fileName = "file://"+mp3fileName
         row1.append("=HYPERLINK(\""+mp3fileName+"\")")

         row1.append(row[6])

         w.writerow(row1)

    # for row in result_ver_game:
    #
    #     row1 = []
    #     row1.append("gameVer")
    #     row1.append(row[0])
    #     row1.append(row[1])
    #     row1.append(row[4])
    #     row1.append(row[2])
    #
    #     tmp="[]&#39;,➕?|"
    #     for char in tmp:
    #         row1[3] = row1[3].replace(char,"") #modify the queryName
    #
    #     b = base64.b64decode(row[3][22:])
    #     mp3fileName=THIS_FOLDER +"/voice2/gameVer+"+row1[3]+"+"+row[1]+"+"+str(row[5])+".mp3"
    #     mp3file = open(mp3fileName, "wb")
    #     mp3file.write(b)
    #     mp3file.close()
    #
    #     mp3fileName = "file://"+mp3fileName
    #     row1.append("=HYPERLINK(\""+mp3fileName+"\")")
    #     row1.append(row[5])
    #     row1.append(row[6])
    #     row1.append(row[7])
    #
    #     w.writerow(row1)
