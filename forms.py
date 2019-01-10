from flask_wtf import FlaskForm
from constant import events
from wtforms import StringField, DateTimeField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length
from wtforms.fields.html5 import DateField


class CribForm(FlaskForm):
    first_name = StringField("Ім\'я", validators=[DataRequired()])
    last_name = StringField("Прізвище", validators=[DataRequired()])
    middle_name = StringField("По батькові", validators=[DataRequired()])
    date_birthday = DateField("Дата народження")
    document = StringField("Документ", validators=[DataRequired()])
    reg_place = StringField("Зареєстрований", validators=[DataRequired()])
    date_time_event = DateTimeField("Дата(час) розгляду", validators=[DataRequired()])
    place_event = StringField("Місце розгляду", validators=[DataRequired()])
    vehicle = StringField("Транспортний засіб", validators=[DataRequired()])
    incident = SelectField("Порушення ПДР", validators=[DataRequired()],
                           choices=[("", "Порушення"), *[(events[event], event) for event in events.keys()]])
    witness = StringField("ПІБ свідка", validators=[DataRequired()])
    fine = StringField("Cтягнення", validators=[DataRequired()])
    police_bio = StringField("ПІБ", validators=[DataRequired()])
    police_rang = StringField("Спеціальне звання", validators=[DataRequired()])
    police_position = StringField("Посада", validators=[DataRequired()])
    submit = SubmitField("Переглянути")
