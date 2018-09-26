from flask import (
    Blueprint, render_template, request, url_for,redirect
)
from random import choice

pyint=0
skipTime=0

bp = Blueprint('game', __name__, url_prefix='/game/<int:pyint>')
queries = [["A great movie for Friday night.","What movies do you think fit for Firday night?",
"Can you recommend some movies for Friday night?"],
["Find me some movies similar to Titanic.","What would you recommend to a fan of Titanic?",
"Movies like Titanic."],
["Show me love stories with happy ending"],
["Comedy","funny movies"],
["Popular movies", "Movies that many people like"]]


@bp.route('/', methods=('GET', 'POST'))
def game(pyint):
    #return "This is the game version."
    # if request.method == 'POST':
    #     name = request.form['name']
    #
    #     # redirect
    #     return redirect(url_for('tutorial.scene1', id=name, pyint=0, skipTime=0))

    queryName=choice(queries[pyint])

    return render_template('GameVersionFolder/game.html',
    htmlint=pyint,
    SkipTime=skipTime,
    queryName=queryName
    )
