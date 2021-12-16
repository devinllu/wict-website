from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def index():     
  return render_template("home.html") 

@views.route('/execs')
def execs():
  return render_template("execs.html")

@views.route('/contacts')
def contacts():
  return render_template("contacts.html")
