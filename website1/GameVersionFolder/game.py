from flask import (
    Blueprint, render_template, request, url_for,redirect
)

pyint=0
skipTime=0

bp = Blueprint('game', __name__, url_prefix='/game/<int:pyint>')



@bp.route('/', methods=('GET', 'POST'))
def game(pyint):
    #return "This is the game version."
    # if request.method == 'POST':
    #     name = request.form['name']
    #
    #     # redirect
    #     return redirect(url_for('tutorial.scene1', id=name, pyint=0, skipTime=0))

    

    return render_template('GameVersionFolder/game.html',
    htmlint=pyint,
    SkipTime=skipTime
    )
