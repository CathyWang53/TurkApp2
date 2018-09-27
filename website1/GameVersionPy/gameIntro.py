from flask import (
    Blueprint, render_template, request, url_for,redirect
)

bp = Blueprint('gameIntro', __name__, url_prefix='/gameIntro')

@bp.route('/', methods=('GET', 'POST'))
def intro():
    # if request.method == 'POST':
    #     name = request.form['name']
    #
    #     # redirect
    #     return redirect(url_for('tutorial.scene1', id=name, pyint=0, skipTime=0))

    return render_template('GameVersionHtml/gameIntro.html')
