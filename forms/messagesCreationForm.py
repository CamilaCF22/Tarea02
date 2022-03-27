from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import InputRequired, Length, ValidationError


class messagesCreationForm(FlaskForm):
    nombre = StringField(
        validators=[
            InputRequired(),
            Length(min=3, max=20),
        ],
        render_kw={"placeholder": "nombre"},
    )

    apellido = StringField(
        validators=[
            InputRequired(),
            Length(min=3, max=20),
        ],
        render_kw={"placeholder": "apellido"},
    )
    
    correo = StringField(
        validators=[
            InputRequired(),
            Length(min=3, max=20),
        ],
        render_kw={"placeholder": "correo"},
    )
    
    mensaje = StringField(
        validators=[
            InputRequired(),
            Length(min=3, max=500),
        ],
        render_kw={"placeholder": "mensaje"},
    )

    submit = SubmitField("Send")