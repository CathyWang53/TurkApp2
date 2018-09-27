from flask import (
    Blueprint, render_template, request, url_for,redirect
)

bp = Blueprint('easyIntro', __name__, url_prefix='/easyIntro')

@bp.route('/', methods=('GET', 'POST'))
def intro():
    # if request.method == 'POST':
    #     name = request.form['name']
    #
    #     # redirect
    #     return redirect(url_for('tutorial.scene1', id=name, pyint=0, skipTime=0))

    return render_template('EasyVersionHtml/easyIntro.html')
