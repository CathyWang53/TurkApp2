from flask import (
    Blueprint, render_template, request, flash
)

from website1 import db
from website1.models import feedbacks

bp = Blueprint('finish', __name__, url_prefix='/finish')

@bp.route('/', methods=('GET', 'POST'))
def wlcm():
    # if request.method == 'POST':
    #     feedback = request.form['name']
    #     print(feedback)
    #     if not text or not Mp3url:
    #         print("successfully add to database2")
    #         flash('result is required.')
    #     else:
    #         print("successfully add to database3")
    #         db.session.add(feedbacks( userid = userID, feedback=feedback,duration=10))
    #         db.session.commit()
    #         # redirect
    #         return redirect(url_for('\code'))

    return render_template('finish.html')
