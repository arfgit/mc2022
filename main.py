from crypt import methods
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

#connect to database
app.config['SQLALCHEMY_DATABASE_URL']='postgres:///postgres:newpassword@localhost/postgres'
db = SQLAlchemy(app)

class Data(db.Model):
    __tablename__ = "data"
    id=db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique = True)
    username = db.Column(db.String(120))

    def __init__(self,email, username):
        self.email = email
        self.username = username



@app.route("/")
def hello():
    return render_template("checkout.html")

#get information from your form in checkout.html, when the submit button isclicked
@app.route('/', methods=['POST'])
def thankyou():
    #the methods that handle request are called views, in flask import
    #form is a dictionary like attribute that holds the form data
    if request.method == "POST":
        email = request.form["email"]
        username = request.form["username"]
        print(request.form)
    data = Data(email,username)
    db.session.add(data)
    db.session.commit()
    return render_template("thankyou.html")



if __name__ == "__main__":
    app.debug = True
    app.run()

