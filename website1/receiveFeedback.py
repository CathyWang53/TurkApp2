from flask import (
    Blueprint, render_template, request, flash
)

bp = Blueprint('receiveFeedback', __name__, url_prefix='/receiveFeedback')

from website1 import db
from website1.models import ResultTable
from website1.models import Results
from website1.models import feedbacks

@bp.route('', methods=('POST','GET'))
def wlcm():
    if request.method == 'POST':
        print("feedback")
        print("successfully add to database1")

        userID=request.form['userID']
        feedback=request.form['feedback']
        timer=request.form['timer']
        version=request.form['version']
        print(feedback)
        print(timer)

        if not feedback:
            print("successfully add to database2")
            flash('result is required.')
        else:
            print("successfully add to database3")
            # db.session.add(ResultTable(answer=name))
            db.session.add(feedbacks( userid = userID, feedback=feedback, duration=timer, version=version))
            db.session.commit()
            print("successfully add to database4")
    return 'success'
