from flask import Flask, render_template

#, flash, redirect, request, url_for, render_template, make_response
# from werkzeug.utils import secure_filename

# ALLOWED_EXTENSIONS = {'txt'}

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template("home.html")
