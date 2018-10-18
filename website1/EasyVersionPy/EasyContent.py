from flask import (
    Blueprint, render_template, request, url_for,redirect, make_response
)
from random import choice

pyint=0
skipTime=0

bp = Blueprint('easy', __name__, url_prefix='/easy/<int:pyint>/<int:skipTime>')
queries = [[["comedy"]],
[["romance"],["Disney"]],
[["France"],["China"],["Mexico"]],
[["<2000"],["2010s"],["2000s"]],
[["Wes Anderson"],["George Lucas"],["Stephen Spielberg"]],
[["explosions"], ["robots"],["time travel"]],
[["exciting plot"],["interesting charactors"],["great acting"]],
[["The Hunger Games"],["The Aviator"], ["When Harry Met Sally..."]],
[["best"],["popular"],["critically acclaimed"]],
[["Brad Pitt"],["Harrison Ford"],["Jennifer Lawrence"]],
[["similar to Titanic"],["like Titanic"]],
[[">2010","➕", "horror"],["horror","➕", ">2010"]],
[["Japan","➕","animation"],["animation","➕","Japan"]],
[["funny","➕","romantic"],["romantic","➕","funny"]],
[["Friday night"],["with a group of friends"]]
]
#helps = ["0","Brad Pitt is a famous film star","0"]
categories = ["genre",
"genre",
"region",
"time",
"director",
"deep feature 1",
"deep feature 2",
"name",
"quality",
"actor",
"movie based",
"combination",
"combination",
"combination",
"context"]

@bp.route('/', methods=('GET', 'POST'))
def game(pyint,skipTime):
    #return "This is the game version."
    # if request.method == 'POST':
    #     name = request.form['name']
    #
    #     # redirect
    #     return redirect(url_for('tutorial.scene1', id=name, pyint=0, skipTime=0))

    queryName=choice(queries[pyint+skipTime])

    resp = make_response(render_template('EasyVersionHtml/easy.html',
    htmlint=pyint,
    SkipTime=skipTime,
    queryName=queryName,
    ))

    resp.set_cookie('category', categories[pyint+skipTime])

    return resp
