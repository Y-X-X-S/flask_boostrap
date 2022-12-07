from flask import render_template
from app.messages import bp
from app.models.message import Message

@bp.route('/')
def index():
    messages = Message.query.all()
    return render_template('index.html', messages = messages)
    
@bp.route('/create', methods = ('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        if not title:
            flash('El título es obligatorio')
        elif not content:
            flash('El contenido es obligatorio')
        else:
            messages.append({'title': title, 'content':content})
            return redirect(url_for('index'))
    return render_template('create.html')
