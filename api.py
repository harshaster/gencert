from flask import Flask, jsonify, render_template,request, send_file
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from pdfwrite import create_cert


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['DEBUG']=False
db=SQLAlchemy(app)

class reg(db.Model):
    __tablename__ = 'participants'
    name = db.Column(db.Text)
    phone = db.Column(db.Text)
    mail = db.Column(db.Text, primary_key=True)

    def __repr__(self) -> str:
        return '<Person %r>' % self.name


@app.route('/c', methods=['GET'])
def click():
    print(f"{datetime.now()}\t Clicked")
    return jsonify({
        'message': 'I am glad you are this curious.'
    })

@app.route('/',methods=["GET", "POST"])
def home():
    if request.method == 'GET':
        return render_template('index.html',notfound=False)
    elif request.method == 'POST':

        mail=request.form['email'].strip()

        
        print(f"{datetime.now()}\t{mail}")

        std = reg.query.filter_by(mail=mail).first()
        if std:
            try:
                filename = create_cert(std.name)
                print(filename)
            except:
                return render_template('index.html',error=True)
            print(f"Approved")
            return send_file(filename)
        else:
            return render_template('index.html',notfound=True)


if __name__=="__main__":
    app.run()
