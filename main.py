from flask import Flask, request, redirect, render_template, url_for
import cgi
app = Flask(__name__)
app.config['DEBUG'] = True
error = ""


def userName():
    global error
    username = cgi.escape(request.form['username'])
    if len(username) >= 20 and len(username) <= 3:
        error = "This is not a valid username,! {0}/n".format(username)

    passWord()
    Verify()
   

def passWord():
    global error
    password = cgi.escape(request.form['password'])
    if len(password) >= 20 and len(password) <= 3:
        error += " is not a valid password! {0}/n".format(password)
    

    

def Verify():
    global error
    verify = cgi.escape(request.form['verify'])
    password = cgi.escape(request.form['password'])
    if verify  != password:
        error += "does not match password"

@app.route("/verify", methods=['POST'])
def verify():
    global error
    userName()
    if error == "":
        return render_template("add-confirmation.html")
    return redirect(url_for("index"))
@app.route("/")
def index():
    global error
    return render_template('edit.html', error=error)

app.run()