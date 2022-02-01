from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Profiles(db.Model):
    profile_id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    about = db.Column(db.Text, nullable=False)
    photo = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<Profile %r>' % self.profile_id


@app.route("/")
def index():
    profiles = Profiles.query.all()
    return render_template('index.html', profiles=profiles)


if __name__ == '__main__':
    app.run(debug=True)
