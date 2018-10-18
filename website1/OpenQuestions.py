from flask import (
    Blueprint, render_template, request, make_response
)

questionNum=1
htmlint=0 #no use at all, only a variable in base.html

queryFiles=["open Question 1", "open Question 2", "open Question 3"]

bp = Blueprint('OpenQuestions', __name__, url_prefix='/OpenQuestions/<int:questionNum>')

@bp.route('/', methods=('GET', 'POST'))
def OpenQuestions(questionNum):

    resp = make_response( render_template('OpenQuestions.html',
                           questionNum = questionNum,
                           htmlint=htmlint,
                           queryName="movie"+queryFiles[questionNum]
                           ))
    resp.set_cookie('category', "Open question")
    return resp
