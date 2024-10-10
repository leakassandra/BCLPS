from flask import Flask, render_template, request, redirect, url_for, Response
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# set up flask app
app = Flask(__name__)

# set up the database (SQLite)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///submissions.db' # file that will store the submissions
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # disabled for performance
db = SQLAlchemy(app) # initialize

# define database model (structure of the database where user-submitted data will be stored)
class Submission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    link = db.Column(db.String(300), nullable=False)
    description = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

# create database
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    link = request.form['link']
    description = request.form['description']

    # Store data in the database
    new_submission = Submission(username=username, link=link, description=description)
    db.session.add(new_submission)
    db.session.commit()

    return redirect(url_for('index'))

@app.route('/feed')
def atom_feed():
    # Retrieve all submissions from the database
    submissions = Submission.query.order_by(Submission.timestamp.desc()).all()

    # Create the ATOM feed structure
    feed = f"""<?xml version="1.0" encoding="utf-8"?>
    <feed xmlns="http://www.w3.org/2005/Atom">
        <title>Links Feed</title>
        <link href="/feed" />
        <updated>{datetime.utcnow().isoformat()}Z</updated>
        <author><name>URL Submission App</name></author>"""

    for submission in submissions:
        feed += f"""
        <entry>
            <title>{submission.username}</title>
            <link href="{submission.link}" />
            <updated>{submission.timestamp.isoformat()}Z</updated>
            <summary>{submission.description}</summary>
        </entry>"""
    
    feed += "</feed>"
    
    # Return the ATOM feed as XML
    return Response(feed, mimetype='application/atom+xml')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)