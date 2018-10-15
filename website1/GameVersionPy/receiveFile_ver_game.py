from flask import (
    Blueprint, render_template, request, flash
)
import time

bp = Blueprint('receiveFile_ver_game', __name__, url_prefix='/receiveFile_ver_game')

from website1 import db
from website1.models import results_ver_game

@bp.route('', methods=('POST','GET'))
def wlcm():
    if request.method == 'POST':
        print("gameVersion")
        print("successfully add to database1")
        text = request.form['text']
        print(text)
        Mp3url =request.form['Mp3url']
#        Mp3url = Mp3url[:100]
        print(Mp3url[:100])
        queryName = request.form['queryName']
        print(queryName)
        userID=request.form['userID']
        print(userID)
        answerTime=request.form['answerTime']
        timeStamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print(timeStamp)
        category = request.cookies.get('category')
        if not Mp3url:
            print("successfully add to database2")
            flash('result is required.')
        else:
            print("successfully add to database3")
            # db.session.add(ResultTable(answer=name))
            db.session.add(results_ver_game( userid = userID, text=text,
            mp3url= Mp3url, queryname=queryName,answertime2=answerTime,
            answerTime=answerTime,datetime=timeStamp, category = category))
            db.session.commit()
            print("successfully add to database4")
    return 'success'
