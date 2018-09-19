from flask import (
    Blueprint, render_template, request, flash
)

bp = Blueprint('receiveFile', __name__, url_prefix='/receiveFile')

from website1 import db
from website1.models import ResultTable
from website1.models import Results

@bp.route('', methods=('POST','GET'))
def wlcm():
    if request.method == 'POST':
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

        if not text or not Mp3url:
            print("successfully add to database2")
            flash('result is required.')
        else:
            print("successfully add to database3")
            # db.session.add(ResultTable(answer=name))
            db.session.add(Results( userID = userID, text=text, Mp3url= Mp3url, queryname=queryName))
            db.session.commit()
            print("successfully add to database4")
    return 'success'
