from flask import Blueprint, request, render_template, redirect, url_for, flash
from popcorn_app import app

main = Blueprint("main", __name__)


@main.route('/')
def home():
    return render_template('home.html')
