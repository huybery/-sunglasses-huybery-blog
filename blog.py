from flask import Flask
from flask import redirect,session,url_for, flash
from flask import render_template
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from datetime import datetime
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from flask.ext.sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'huybers string'
bootstrap = Bootstrap(app)
moment = Moment(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64),unique=True)

    def __repr__(self):
        return '<Role %r>' % self.name

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)

    def __repr__(self):
        return '<User %r' % self.username

@app.route('/', methods=['GET','POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not  None and old_name != form.name.data:
            flash('Look like you have changed your name!')
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('hello.html',name = session.get('name'),form = form ,current_time = datetime.utcnow())

@app.route('/usr/<name>')
def user(name):
    return render_template('usr.html',usr=name)

@app.route('/baidu')
def baidu():
    return redirect('http://www.baidu.com')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html'),404

class NameForm(Form):
    name = StringField('what is your name?',validators=[Required()])
    submit = SubmitField('Submit')


if __name__ == '__main__':
    app.run(debug=True)

