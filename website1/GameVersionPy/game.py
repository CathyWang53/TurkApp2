from flask import (
    Blueprint, render_template, request, url_for,redirect, make_response
)
from random import choice

pyint=0
skipTime=0

bp = Blueprint('game', __name__, url_prefix='/game/<int:pyint>/<int:skipTime>')
queries = [[["Comedy"]],
[["Brad Pitt"],["Harrison Ford"],["Jennifer Lawrence"]],
[["Wes Anderson"],["Alfred Hitchcock"],["Hayao Miyazaki"]],
[["Romance"],["Disney"]],
[["<2000"],["2010s"],["2000s"]],
[["France"],["China"],["Mexico"]],
[["Explosions"], ["Robots"],["Time travel"]],
[["Exciting plot"],["Interesting charactors"]],
[["Best"],["popular"]],
[["Friday night"],["Weekend"]],
[["similar to Titanic"],["Like Titanic"],["≈Titanic"]],
[["The Hunger Games"],["The Aviator"], ["When Harry Met Sally..."]],
[[">2010","➕", "Horror"],["Japan","➕","Animation"],["Funny","➕","Romantic"]]
]

categories = ["genre",
"actor",
"director",
"genre",
"time",
"region",
"deep feature 1",
"deep feature 2",
"quality",
"scene",
"movie based",
"name",
"combination"]


@bp.route('/', methods=('GET', 'POST'))
def game(pyint,skipTime):
    #return "This is the game version."
    # if request.method == 'POST':
    #     name = request.form['name']
    #
    #     # redirect
    #     return redirect(url_for('tutorial.scene1', id=name, pyint=0, skipTime=0))

    queryName=choice(queries[pyint+skipTime])

    resp = make_response(render_template('GameVersionHtml/game.html',
    htmlint=pyint,
    SkipTime=skipTime,
    queryName=queryName
    ))

    resp.set_cookie('category', categories[pyint+skipTime])

    return resp
