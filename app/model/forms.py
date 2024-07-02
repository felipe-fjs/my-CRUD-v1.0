from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length

class LogForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('pass', validators=[DataRequired()])


class ColabForm(FlaskForm):
    nome = StringField('nome', validators=[DataRequired(), Length(min=3)])
    matricula = StringField('matricula', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])