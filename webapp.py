import os
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session

app = Flask(__name__)

app.secret_key=os.environ["SECRET_KEY"];

@app.route('/')
def renderMain():
    session["secure1"] = True
    session["secure2"] = True
    session["secure3"] = True
    return render_template('home.html')

@app.route('/startOver')
def startOver():
    session.clear() #clears variable values and creates a new session
    return redirect(url_for('renderMain')) # url_for('renderMain') could be replaced with '/'

@app.route('/question1')
def renderQ1():
    return render_template('question1.html')

@app.route('/question2',methods=['GET','POST'])
def renderQ2():
    if session["secure1"] == True:
        session["quest1"]=request.form['order']
    session["secure1"] = False
    return render_template('question2.html')

@app.route('/question3',methods=['GET','POST'])
def renderQ3():
    if session["secure2"] == True:
        session["quest2"]=request.form['job']
    session["secure2"] = False
    return render_template('question3.html')

@app.route('/response',methods=['GET','POST'])
def renderResponse():
    if session["secure3"] == True:
        session["quest3"]=request.form['event']
    session["secure3"] = False
        
    session["score"] = 0
    
    if session["quest1"] == "DCP":
        session["result1"] = "correctly"
        session["score"] = session["score"] + 1
    else:
        session["result1"] = "incorrectly"
    if session["quest2"] == "phar":
        session["result2"] = "correctly"
        session["score"] = session["score"] + 1
    else:
        session["result2"] = "incorrectly"
    if session["quest3"] == "ww2":
        session["result3"] = "correctly"
        session["score"] = session["score"] + 1
    else:
        session["result3"] = "incorrectly"
    return render_template('response.html')
    
if __name__=="__main__":
    app.run(debug=False)
