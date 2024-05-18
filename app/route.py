from flask import render_template, request, redirect, url_for, send_from_directory, session
from app import app


@app.route('/')
def index():
    return render_template('index.html')

