from flask import Flask, render_template, request, jsonify, redirect, url_for
from config import Config
from constant import events
import datetime
import forms

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/', methods=['GET', 'POST'])
def crib_form():
    data_form = forms.CribForm(request.form)
    data_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    if request.method == 'POST' and data_form.is_submitted():
        input_data = {
            "first_name": data_form.first_name.data,
            "last_name": data_form.last_name.data,
            "middle_name": data_form.middle_name.data,
            "date_birthday": data_form.date_birthday.data,
            "document": data_form.document.data,
            "reg_place": data_form.reg_place.data,
            "date_time_event": data_form.date_time_event.data,
            "place_event": data_form.place_event.data,
            "vehicle": data_form.vehicle.data,
            "incident_pdd": [key for (key, value) in events.items() if value == data_form.incident.data],
            "incident": data_form.incident.data,
            "witness": data_form.witness.data,
            "fine": data_form.fine.data,
            "police_bio": data_form.police_bio.data,
            "police_rang": data_form.police_rang.data,
            "police_position": data_form.police_position.data
        }
        print(input_data['police_position'])
        return render_template("crib/index.html", input_data=input_data)

    return render_template("crib_form/index.html", data_form=data_form, data_time=data_time)


@app.route('/crib')
def crib():
    input_data = {
        "first_name": "first_name",
        "last_name": "last_name",
        "middle_name": "middle_name",
        "date_birthday": "date_birthday",
        "document": "document",
        "reg_place": "reg_place",
        "date_time_event": "date_time_event",
        "place_event": "place_event",
        "vehicle": "vehicle",
        "incident_pdd": "incident_pdd",
        "incident": "incident",
        "witness": "witness",
        "fine": "fine",
        "police_bio": "police_bio",
        "police_rang": "police_rang",
        "police_position": "police_position"
    }
    return render_template("crib/index.html", input_data=input_data)


if __name__ == '__main__':
    app.run()
