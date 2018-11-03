from flask import (
    Blueprint, render_template, request, url_for,redirect, make_response
)
from random import choice

pyint=0
skipTime=0

bp = Blueprint('easy', __name__, url_prefix='/easy/<int:pyint>/<int:skipTime>')
queries = [[["comedy"]],
[["romance"],["action"]],
[["France"],["China"],["Mexico"]],
[["after 2000"],["since 2000"],["2010s"],["1980s"]],
[["Wes Anderson"],["George Lucas"],["Stephen Spielberg"]],
[["explosions"], ["robots"],["time travel"]],
[["exciting plot"],["interesting charactors"],["great acting"]],
[["The Hunger Games"],["The Aviator"], ["When Harry Met Sally..."]],
[["best"],["popular"],["critically acclaimed"]],
[["Brad Pitt"],["Harrison Ford"],["Jennifer Lawrence"]],
[["similar to Titanic"],["like Titanic"]],

[["2010s","➕", "sci-fi"],["sci-fi","➕", "2010s"]],
[["Japan","➕","animation"],["animation","➕","Japan"]],
[["funny","➕","romantic"],["romantic","➕","funny"]],
[["family movie" ,"➕","no animation"],["no animation","➕","family movie"]],
[["horror","➕","not thriller"],["not thriller","➕","horror"]],
[["comedy","➕", "not stupid"],["not stupid","➕","comedy"]],


[["Friday night"],["weekend"]],
[["with a group of friends"],["with your family"]],
[["in theaters now"]]
]

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
"no-combination",
"no-combination",
"no-combination",
"context",
"context",
"context"]

# queries = [
# [["comedy"]],
# [["France"],["China"],["Mexico"]],
# [["after 2000"],["since 2000"],["2010s"],["1980s"]],
#
# [["2010s","➕", "sci-fi"],["sci-fi","➕", "2010s"]],
#
#
# [["action","➕","no violence"],["no violence","➕","action" ]],
# [["family movie","➕","no animation"],["no animation","➕","family movie"]],
# [["comedy","➕", "not stupid"],["not stupid","➕","comedy"]],
# [["horror","➕","not thriller"],["not thriller","➕","horror"]],
# [["similar to Titanic","➕", "not sad"],["not sad","➕","similar to Titanic"]],
# [["drama","➕","not old"],["not old","➕","drama"]],
# [["Leonardo DiCaprio","➕","have not watched"],["have not watched","➕","Leonardo DiCaprio"]]
# ]
#helps = ["0","Brad Pitt is a famous film star","0"]

# categories = ["genre",
# "Region",
# "time",
# "combination",
# "no-combination",
# "no-combination",
# "no-combination",
# "no-combination",
# "no-combination",
# "no-combination",
# "no-combination"]



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
