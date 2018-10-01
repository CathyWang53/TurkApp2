from flask import (
    Blueprint, render_template, request, url_for,redirect
)
from random import choice

pyint=0
skipTime=0

bp = Blueprint('easy', __name__, url_prefix='/easy/<int:pyint>/<int:skipTime>')
queries = [["comedy"],
["Brad Pitt"],
["interesting characters"],
["Titanic"],
["France"],
["2010s","➕","Superhero"],
["explosion"],
["popular"],
["Best","➕",">2000"]
]
#helps = ["0","Brad Pitt is a famous film star","0"]


@bp.route('/', methods=('GET', 'POST'))
def game(pyint,skipTime):
    #return "This is the game version."
    # if request.method == 'POST':
    #     name = request.form['name']
    #
    #     # redirect
    #     return redirect(url_for('tutorial.scene1', id=name, pyint=0, skipTime=0))

    queryName=queries[pyint+skipTime]

    return render_template('EasyVersionHtml/easy.html',
    htmlint=pyint,
    SkipTime=skipTime,
    queryName=queryName,
    )
