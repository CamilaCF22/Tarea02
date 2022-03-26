from flask import Blueprint, render_template, redirect, url_for
from utils.db import db

country = Blueprint("country", __name__)

@country.route("/")
def home():
    return render_template("landing-page-pais-template/country/home.html")
