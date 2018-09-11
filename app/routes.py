from app import app
from flask import render_template, url_for, redirect

@app.route('/')
@app.route('/index')
def index():
    list = ['Hippo', 'Lion', 'Tiger', 'Cat', 'Monkey']
    d = {
        'Hippo': 'Mean',
        'Lion': 'Lazy',
        'Tiger': 'Magnificent',
        'Cat': 'just cats',
    }
    return render_template('index.html', list=list, d=d)

@app.route('/info')
def site_info():
    copy_right = 'Site Created By XXXXXX'
    d = {
        'Jan': 31,
        'Feb': 28,
        'Mar': 31,
        'Apr': 30,
        'May': 31,
        'June': 30,
        'July': 31,
        'Aug': 31
    }
    seasons = ['Spring', 'Summer', 'Fall', 'Winter']
    return render_template('info.html', copy_right=copy_right, d=d, seasons=seasons)

@app.route('/location')
def place():
    names = ['Shanghai', 'New York', 'London', 'Rio']
    d = {
        'Shanghai': 'Asia',
        'New York': 'North America',
        'London': 'Europe',
        'Rio': 'South America'
    }
    return render_template('place.html', names=names, d=d)

@app.route('/redirecting')
def my_redirect():
    return redirect(url_for('index'))
