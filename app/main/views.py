from flask import render_template, request, redirect, url_for, session
from . import main


@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
