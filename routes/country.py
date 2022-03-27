from flask import Blueprint, render_template, redirect, url_for
from utils.db import db

country = Blueprint("country", __name__)

@country.route("/")
def home():
    return render_template("landing-page-pais-template/country/home.html")

@country.route("/create", methods=["GET", "POST"])
def create():
    form = messagesCreationForm()
    if form.validate_on_submit():
        nombre = form.nombre.data
        apellido = form.apellido.data
        correo = form.correo.data
        mensaje = form.mensaje.data
        newMessage = Message(nombre, apellido, correo, mensaje)
        db.session.add(newMessage)
        db.session.commit()
        return redirect(url_for("country.home"))
    return render_template("countrymessages/create.html", form=form)
