from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)

# sql connection
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Student_Management.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Todo(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    NAME = db.Column(db.String(100), nullable=False)
    EMAIL = db.Column(db.String(120), unique=True, nullable=False)
    COURSE = db.Column(db.String(100), nullable=False)




# home page for student management
@app.route("/")
def hello_world():
    return render_template('index.html')



@app.route("/products")
def products():
    return "<p>Hello you are in product </p>"



if __name__ == "__main__":
    app.run(debug=True,port=3000)













