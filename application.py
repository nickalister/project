from flask import request, session, redirect, url_for, g, abort, render_template, flash, make_response, Flask
from flask.ext import excel
from passlib.hash import sha256_crypt
import datetime

#import flask app
app = Flask(__name__)
app.config.from_object('config')


@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
  error = ""
  if request.method == "POST":
    if request.form['username'] !='' and request.form['password'] !='':
      pass
    error = "Wrong username or password"
    return render_template('login.html', error=error)
  return render_template('login.html')



if __name__ == '__main__':
  app.run(debug=True, port=5055)
