from flask import Blueprint,render_template,request,flash,jsonify
from flask_login import login_required,current_user
from . import db
from .models import User
import json
views=Blueprint('views',__name__)
@views.route('/',methods=["GET","POST"])
def home():
    return render_template('Main.html',user=current_user)
@views.route('/workouts')
def workout():
    return render_template('workout.html',user=current_user)
@views.route('/leftchest')
def leftchest():
    return render_template('leftchest.html', user=current_user)
@views.route('/chestBODY')
def chestBODY():
    return render_template('chestBODY.html',user=current_user)
@views.route('/chestSTR')
def chestSTR():
    return render_template('chestSTR.html' ,user=current_user)
@views.route('/shoulder')
def shoulder():
    return render_template('shoulder.html',user=current_user)
@views.route('/bicep')
def Bicep():
    return render_template('biceps.html',user=current_user)
@views.route('/forearm')
def forearm():
    return render_template('forearm.html',user=current_user)
@views.route('/abs')
def abs():
    return render_template('abs.html',user=current_user)
@views.route('/quads')
def quads():
    return render_template('quads.html',user=current_user)
@views.route('/calves')
def calves():
    return render_template('calves.html',user=current_user)
@views.route('/upperback')
def upperback():
    return render_template('upperback.html',user=current_user)
@views.route('/middleback')
def middleback():
    return render_template('middleback.html',user=current_user)
@views.route('/triceps')
def triceps():
    return render_template('triceps.html',user=current_user)
@views.route('/hamstring')
def hamstring():
    return render_template('hamstring.html',user=current_user)
@views.route('/pricing')
def pricing():
    return render_template('pricing.html',user=current_user)
