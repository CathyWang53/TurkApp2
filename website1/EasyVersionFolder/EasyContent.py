from flask import (
    Blueprint, render_template, request, url_for,redirect
)
from random import choice

pyint=0
skipTime=0

bp = Blueprint('easy', __name__, url_prefix='/easy/<int:pyint>')
queries = [["comedy"],
["Brad Pitt"],
["France"],
["2010s","➕","Superhero"],
["explosion"],
["popular"],
["Titanic"],
["interesting characters"],
["Best","➕",">2000"]
]
helps = [""]


@bp.route('/', methods=('GET', 'POST'))
def game(pyint):
    #return "This is the game version."
    # if request.method == 'POST':
    #     name = request.form['name']
    #
    #     # redirect
    #     return redirect(url_for('tutorial.scene1', id=name, pyint=0, skipTime=0))

    queryName=queries[pyint]

    return render_template('EasyVersionFolder/easy.html',
    htmlint=pyint,
    SkipTime=skipTime,
    queryName=queryName
    )
