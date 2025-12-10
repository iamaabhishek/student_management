from flask import Flask, render_template , request ,redirect
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)

# sql connection
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Student_Management.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class StuMa(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    NAME = db.Column(db.String(100), nullable=False)
    EMAIL = db.Column(db.String(120),  nullable=False)
    COURSE = db.Column(db.String(100), nullable=False)

    def __repr__(self) -> str:          # This function show result in console
        return f"{self.ID} - {self.NAME} - {self.EMAIL} - {self.COURSE}"


# home page for student management
@app.route("/",methods=['GET','POST'])
def addStudent():
    if request.method == 'POST': # Getting data from form
        name = request.form['studentName']
        email = request.form['exampleInputEmail']
        course = request.form['course']    
    # (Insert data for testing purpose)
        student = StuMa(NAME=name,EMAIL=email,COURSE=course)
        db.session.add(student)
        db.session.commit()
         
    allStudent = StuMa.query.all()
    return render_template('index.html',allStudent = allStudent)



@app.route("/showStudent")
def showStudent():
    allStudent = StuMa.query.all()
    print(allStudent)
    return "<p>Hello you are in product </p>"


@app.route("/delete/<int:ID>")
def deleteStudent(ID):
    Student = StuMa.query.filter_by(ID=ID).first()
    db.session.delete(Student)
    db.session.commit()
    return redirect("/")
   

@app.route("/update/<int:ID>", methods=['GET', 'POST'])
def updateStudent(ID):
    student = StuMa.query.get_or_404(ID)

    if request.method == "POST":
        student.NAME = request.form['studentName']
        student.EMAIL = request.form['exampleInputEmail']
        student.COURSE = request.form['course']

        db.session.commit()
        return redirect("/")

    return render_template('update.html', Student=student)




if __name__ == "__main__":
    app.run(debug=True,port=3000)













