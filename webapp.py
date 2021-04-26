import os
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session

app = Flask(__name__)

app.secret_key=os.environ["SECRET_KEY"];

@app.route('/')
def renderMain():
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
    session["quest1"]=request.form['order']
    return render_template('question2.html')

@app.route('/question3',methods=['GET','POST'])
def renderQ3():
    session["quest2"]=request.form['job']
    return render_template('question3.html')

@app.route('/response',methods=['GET','POST'])
def renderResponse():
    session["quest3"]=request.form['event']
    session["score"] = 0
    
    if session["quest1"] == "DCP":
        session["response1"] = "correctly"
        session["score"] = session["score"] + 1
    else:
        session["response1"] = "incorrectly"
    if session["quest2"] == "phar":
        session["response2"] = "correctly"
        session["score"] = session["score"] + 1
    else:
        session["response2"] = "incorrectly"
    if session["quest3"] == "ww2":
        session["response3"] = "correctly"
        session["score"] = session["score"] + 1
    else:
        session["response3"] = "incorrectly"
    return render_template('response.html')
    
if __name__=="__main__":
    app.run(debug=False)
