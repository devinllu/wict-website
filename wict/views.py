from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():     
  return render_template("home.html") 

@views.route('/execs')
def execs():
  return render_template("execs.html")

@views.route('/merch')
def merch():
  return render_template("merch.html")

@views.route('/design')
def design():
  return render_template("design.html")
