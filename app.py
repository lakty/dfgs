from flask import Flask, render_template, request, jsonify, redirect, url_for
from config import Config
from constant import events, fine
import datetime

import forms

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/', methods=['GET', 'POST'])
def crib_form():
    data_form = forms.CribForm(request.form)
    data_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if request.method == 'POST' and data_form.validate():
        return redirect(url_for("crib"))
    return render_template("crib_form/index.html", data_form=data_form, data_time=data_time)


@app.route('/crib')
def crib():
    return render_template("crib/index.html")


@app.route('/fine/<incident>')
def func_fine(incident):
    _fine = fine[incident]
    print(_fine)
    fineObj = _fine

    return jsonify({'value': fineObj})


if __name__ == '__main__':
    app.run()
