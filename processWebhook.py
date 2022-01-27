import flask
import os
from flask import send_from_directory, render_template, request
from flask.helpers import url_for
from werkzeug.utils import redirect
#import graph
#import sound


app = flask.Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/favicon.png')

@app.route('/')
@app.route('/home')
@app.route('/button_element.php',methods = ['POST'])


#below trying to resolve how to develop website to post projects
@app.route('/')
@app.route('/home')
def home():
    if request.method == 'POST':
        print('at frontage')
    return render_template('frontpage.html')
""""
#below is an example on how to take user data with post/get, the below script can also activate sound
@app.route('/welcome.php',methods = ['POST'])
def submit():
    if request.method == 'POST':
        print('---------inside welcome php')
        #sound.play_sound() #would start sound.py
        user_name = request.form['name']
        return redirect(url_for("welcome",usr=user_name))

#test route for practising navigation

@app.route('/graph')
def test():
        graph_img = graph()
        return render_template(graph_img)


@app.route('/<usr>')
def welcome(usr):
    return f"<p> {usr} </p>"
"""
if __name__ == "__main__":
    app.secret_key = 'ItIsASecret'
    app.debug = True
    app.run()