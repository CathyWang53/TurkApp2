from flask import (
    Blueprint, render_template, request, url_for,redirect
)
from random import choice

pyint=0
skipTime=0

bp = Blueprint('game', __name__, url_prefix='/game/<int:pyint>/<int:skipTime>')
queries = [["A great movie for Friday night.","What movies do you think fit for Firday night?",
"Can you recommend some movies for Friday night?"],
["Find me some movies similar to Titanic.","What would you recommend to a fan of Titanic?",
"Movies like Titanic.","Films similar to Titanic"],
["Show me a movie with Harrison Ford", "Movies starred by Harrison Ford","show me all movies starring Harrison Ford"],
["The Shawshank Redemption","I'd like to watch The Shawshank Redemption"],
["Show me love stories with a happy ending"],
["Comedy","Funny movies","Something funny","I'd like to watch a commedy"],
["Popular movies", "Movies that many people like"],
["Can you find me a funny romantic movie made in the 2000s?"],
["Best movies right now"]
]


@bp.route('/', methods=('GET', 'POST'))
def game(pyint,skipTime):
    #return "This is the game version."
    # if request.method == 'POST':
    #     name = request.form['name']
    #
    #     # redirect
    #     return redirect(url_for('tutorial.scene1', id=name, pyint=0, skipTime=0))

    queryName=choice(queries[pyint+skipTime])

    return render_template('GameVersionHtml/game.html',
    htmlint=pyint,
    SkipTime=skipTime,
    queryName=queryName
    )
