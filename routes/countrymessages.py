from flask import Blueprint, render_template, redirect, url_for
from utils.db import db

countrymessages = Blueprint("countrymessages", __name__, url_prefix="/messages")

@countrymessages.route("/")
def home():
    return render_template("landing-page-pais-template/countrymessages/home")