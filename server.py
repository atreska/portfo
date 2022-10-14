from email import header
import re
from unicodedata import name
from flask import Flask, render_template
import os
import csv
from flask import send_from_directory
from flask import request, redirect


app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def pages(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('/Users/adamtreska/Downloads/project_files/database.txt', 'a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        database.write(
            f'email: {email}\nsubject: {subject}\nmessage: {message}\n\n')


def write_to_csv(data):
    with open('/Users/adamtreska/Downloads/project_files/database.csv', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])
        # future Challenge: write headers if file doesn't exist, and not if it does.


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thanks.html')
        except:
            return 'Something went wrong try again!'
    else:
        return 'There was an error with this request.'
