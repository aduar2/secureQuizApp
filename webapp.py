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
    session["result1"]=request.form['order']
    return render_template('question2.html')

@app.route('/question3',methods=['GET','POST'])
def renderQ3():
    session["result2"]=request.form['job']
    return render_template('question3.html')

@app.route('/response',methods=['GET','POST'])
def renderResponse():
    session["result3"]=request.form['event']
    return render_template('response.html')
    
if __name__=="__main__":
    app.run(debug=False)
