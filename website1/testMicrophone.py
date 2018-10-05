from flask import (
    Blueprint, render_template, request, url_for,redirect
)
from random import choice

pyint=0
skipTime=0

bp = Blueprint('testMicrophone', __name__, url_prefix='/testMicrophone')


@bp.route('/', methods=('GET', 'POST'))
def game():
    #return "This is the game version."
    # if request.method == 'POST':
    #     name = request.form['name']
    #
    #     # redirect
    #     return redirect(url_for('tutorial.scene1', id=name, pyint=0, skipTime=0))

    # queryName=choice(queries[pyint+skipTime])

    return render_template('testMicrophone.html',
    htmlint=pyint,
    SkipTime=skipTime
    )
