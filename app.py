from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
 

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:manas123@localhost/height_collector"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
db.init_app(app)


class Data(db.Model):
    __tablename__ = "data"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20), nullable = False)
    email_ = db.Column(db.String(120), unique = True, nullable  = False)
    height_ = db.Column(db.Integer, nullable = False)

    def __init__(self, name, email_, height_):
        self.name = name
        self.email_ = email_
        self.height_ = height_
        

    

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/Home", methods = ["POST"])
def Home():
    if request.method == "POST":
        return index()


@app.route("/success", methods =["POST"])
def successPage():
    if request.method=="POST":
        name_ = request.form["user_name"]
        email = request.form["email_name"]
        height = request.form["height_name"]
        
#send_email(email, height)
        if db.session.query(Data).filter(Data.email_== email).count() == 0:
            data = Data(name_, email, height)
            db.session.add(data)
            db.session.commit()
            average_height = db.session.query(func.avg(Data.height_)).scalar()
            average_height = round(average_height, 1)
            userName =  db.session.query(Data.name).all()
            mail = db.session.query(Data.email_).all()
            heit = db.session.query(Data.height_).all()
            # for i in heit:
            #     print(i)
            # print(average_height)
            return render_template("success.html", heights=height, avg = average_height,mail= mail,heit= heit, userName = userName)
        return render_template("index.html",
        text = "Seems like we've got something from the Email Address already!")

if __name__ == "__main__":
    app.run(debug=True, port=5000)