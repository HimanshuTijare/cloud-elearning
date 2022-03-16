from flask import Flask, render_template, request,session,redirect,flash,url_for,send_file
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
import app
import re



import os




app = Flask(__name__,template_folder='templates')

ENV = 'prod'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@localhost/e-learningwebapp'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://cxrthnnzpdurpo:6b4dd798078a00d1dcbd785bf73ba7c83673bb49f57c2935e2facf318d547bd3@ec2-18-210-191-5.compute-1.amazonaws.com:5432/df06lhn4p4l26b'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Register(db.Model):
    __tablename__="register"
    id = db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50),nullable =False)
    uname=db.Column(db.String(50),nullable =False)
    email=db.Column(db.String(50),nullable =False)
    password=db.Column(db.String(50),nullable =False)
    cpassword=db.Column(db.String(50),nullable =False)

def __init__(self, name, uname, email, password, cpassword):
        self.name = name
        self.uname = uname
        self.email = email
        self.password = password
        self.cpassword = cpassword



@app.route("/")
def Home():
    return render_template('index.html')

@app.route("/about")
def About():
    return render_template('about.html')

@app.route("/album")
def Album():
    return render_template('album.html')



@app.route("/register", methods=['POST'])
def register():
    if(request.method=='POST'):
        name = request.form['name']
        uname = request.form['uname']
        mobile = request.form['mobile']
        email= request.form['email']
        password= request.form['password']
        cpassword= request.form['cpassword']

        user=register.query.filter_by(email=email).first()
        if user:
            flash('Account already exist!Please login','success')
            return redirect(url_for('register'))
        if not(len(name)) >3:
            flash('length of name is invalid','error')
            return redirect(url_for('register')) 
        if (len(mobile))<10:
            flash('invalid mobile number','error')
            return redirect(url_for('register')) 
        if (len(password))<8:
            flash('length of password should be greater than 7','error')
            return redirect(url_for('register'))
        else:
             flash('You have registtered succesfully','success')
        entry = Register(name=name,uname=uname,email=email,password=password,cpassword=cpassword)
        db.session.add(register)
        db.session.commit()
    return render_template('register.html')

@app.route("/login",methods=['GET','POST'])
def login():
    return render_template('login.html')

@app.route("/contact",  methods=['GET','POST'])
def contact():
   
    return render_template('contact.html')

@app.route("/web",methods=['GET','POST'])
def web_development():
    return render_template('web.html')

@app.route("/andriod",methods=['GET','POST'])
def andriod_development():
    return render_template('andriod.html')

@app.route("/art",methods=['GET','POST'])
def Art():
    return render_template('art.html')

@app.route("/photography",methods=['GET','POST'])
def Photography():
    return render_template('photography.html')

@app.route("/uxdesign",methods=['GET','POST'])
def Uxdesign():
    return render_template('uxdesign.html')

@app.route("/graphic",methods=['GET','POST'])
def Graphic_design():
    return render_template('graphic.html')

@app.route("/marketing",methods=['GET','POST'])
def Digital_marketing():
    return render_template('marketing.html')

@app.route("/linux",methods=['GET','POST'])
def Linux_development():
    return render_template('linux.html')

@app.route("/web_development")
def download_file():
    p="website_development_tutorial.pdf"
    return send_file(p,as_attachment=True)

@app.route("/andriod_development")
def andriod_download_file():
    c="android_tutorial.pdf"
    return send_file(c,as_attachment=True)

@app.route("/art_craft")
def art_download_file():
    d="art_and_design-_a_comprehensive_guide_for_creative_artists.pdf"
    return send_file(d,as_attachment=True)

@app.route("/photo")
def photo_download_file():
    m="photography.pdf"
    return send_file(m,as_attachment=True)

@app.route("/ux")
def ux_download_file():
    k="ux design.pdf"
    return send_file(k,as_attachment=True)

@app.route("/graphics")
def graphics_download_file():
    n="Graphic Design.pdf"
    return send_file(n,as_attachment=True)

@app.route("/digital")
def digital_download_file():
    s="Digital Marketing.pdf"
    return send_file(s,as_attachment=True)

@app.route("/linux_development")
def linux_download_file():
    a="Linux development.pdf"
    return send_file(a,as_attachment=True)

@app.route("/adminlogin",methods=['GET','POST'])
def adminlogin():
    if(request.method=='POST'):
        email=request.form.get('email')
        password=request.form.get('password')
        if email=='admin@gmail.com' and password=='123456':
            return render_template('admindash.html') 
    return render_template('adminlogin.html')



@app.route("/logout", methods = ['GET','POST'])
def logout():
    session.pop('email')
    return redirect(url_for('Home')) 


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

if __name__ == '__main__':
    app.run()