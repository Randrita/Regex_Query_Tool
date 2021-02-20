from flask import Flask, render_template, request, flash ,session
from database import users, db_init, db
import re
import csv
from werkzeug.utils import secure_filename
from csrlc import replace_csv
import os
import pytesseract
from io import TextIOWrapper

app = Flask(__name__)
app.secret_key="1258suy"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db_init(app)
@app.route('/')
def index():
   return render_template('index.html')

@app.route('/typein.html',methods=['GET','POST'])
def typein():
   #if request.method=='POST':
   
      #txt=request.form['text']
      
   #else:
   return render_template('typein.html')

 
   return render_template('typein.html')

@app.route('/xlsx.html')
def xlsx():
   return render_template('xlsx.html')

@app.route('/csv.html')
def csv():
   return render_template('csv.html')
@app.route('/typein-find.html',methods=['GET','POST'])
def find():
   if request.method=='POST':
      check=request.form['find']
      txt=request.form['text']
      
      #a = users( txt, check,"")
      x=re.search(check, txt)
      #print(x.span())
      #db.session.add(a)
      #db.session.commit()
      
      if x:
         flash(f"Word is found at the position {x.span()}")
         #print('Y')
         #return render_template('typein-find.html')
      else:
         flash("Word is not found")

         #return render_template('typein-find.html')

   return render_template("typein-find.html")

@app.route('/typein-replace.html',methods=['GET','POST'])
def replace():
   if request.method=='POST':
      check1=request.form['find']
      txt1=request.form['text']
      rlc=request.form['replace']
      new_string = re.sub(check1,rlc,txt1)
      flash(new_string)

   return render_template("typein-replace.html")

@app.route('/typein-number.html',methods=['GET','POST'])
def number():
   if request.method=='POST':
      txt1=request.form['text']
      pattern = '\d+'
      result = re.findall(pattern, txt1) 
      flash(result)
      

   return render_template("typein-number.html")

@app.route('/typein-https.html',methods=['GET','POST'])
def https():
   if request.method=='POST':
      txt1=request.form['text']
      obj1 = re.findall('(\w+)://',txt1) 
      flash(f'Protocol:{obj1}') 
      obj2 = re.findall('://([\w\-\.]+)',txt1) 
      flash(f'Host:{obj2}')
   return render_template("typein-https.html")

@app.route('/typein-ip.html',methods=['GET','POST'])
def ip():
   if request.method=='POST':
      txt1=request.form['text']
      regex = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$'''
      if(re.search(regex, txt1)): 
         flash("Valid Ip address")  
      else:
         flash("Invalid Ip address")
   return render_template("typein-ip.html")

@app.route('/typein-mail.html',methods=['GET','POST'])
def mail():
   if request.method=='POST':
      txt1=request.form['text']
      regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
      if(re.search(regex,txt1)):
         flash("Valid Email")  
      else:
         flash("Invalid Email")
   return render_template("typein-mail.html")

@app.route('/typein-quotedword.html',methods=['GET','POST'])
def quotedword():
   if request.method=='POST':
      txt1=request.form['text']
      flash(re.findall(r'"(.*?)"', txt1))
   return render_template("typein-quotedword.html")
#for csv
@app.route('/csv-find.html',methods=['GET','POST'])

def cv_find():
   import csv
   
   if request.method=='POST':
      ls=[]
      find=request.form['find']
      text=request.files['actual-btn']
      #filename=text.split(".")
      text = TextIOWrapper(text, encoding='utf-8')
      

     


      
      cv_reader1= csv.reader(text)
      for line in cv_reader1:
         for word in line:
            a=word.split(';')
            ls=ls+a
      for item in ls:
         if item in find:
            flash('Found')
            break
      else:
         flash('Not Found')
      

   
   return render_template("csv-find.html")
@app.route('/csv-replace.html',methods=['GET','POST'])
def csv_replace():
   import csv
   if request.method=='POST':
      org_wrd=request.form['Replace']
      rlc_wrd=request.form['nwwrd']
      txt= request.files['actual-btn']
      txt = TextIOWrapper(txt, encoding='utf-8')
      csv_reader=csv.reader(txt)
     
      text = ''.join([str(i) for i in csv_reader])  
      
      text = text.replace('{}'.format(org_wrd),'{}'.format(rlc_wrd)) 
      x = open("output.csv","w")
      x.writelines(text)
      x.close()
      
      
      
     

   
   return render_template("csv-replace.html",op="output.csv")



if __name__ == '__main__':
   app.run(debug=True,port=80)