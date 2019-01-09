from flask_wtf import Form
from constant import events
from wtforms import StringField, DateTimeField, SelectField, SubmitField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import DateField


class CribForm(Form):
    first_name = StringField("Ім\'я", validators=[DataRequired()])
    last_name = StringField("Прізвище", validators=[DataRequired()])
    middle_name = StringField("По батькові", validators=[DataRequired()])
    date_birthday = DateField("Дата народження", validators=[DataRequired()], format='%Y-%m-%d')
    document = StringField("Документ", validators=[DataRequired()])
    reg_place = StringField("Зареєстрований", validators=[DataRequired()])
    date_time_event = DateTimeField("Дата(час) розгляду", validators=[DataRequired()])
    place_event = StringField("Місце розгляду", validators=[DataRequired()])
    vehicle = StringField("Транспортний засіб", validators=[DataRequired()])
    incident = SelectField("Порушення ПДР", validators=[DataRequired()],
                           choices=[("", "Порушення"), *[(events[event], event) for event in events.keys()]])
    witness = StringField("ПІБ свідка", validators=[DataRequired()])
    fine = StringField("Cтягнення", validators=[DataRequired()])
    submit = SubmitField("Переглянути")
