import logging
from flask import Flask, render_template, redirect, url_for, request, Blueprint
from .forms import gen_dist_form, gen_email_form, gen_bmi_form, gen_retire_form, gen_tip_form

from .distance import calc_distance
from .retirement import calc_retirement
from .email import verify_email
from .bmi import calc_bmi
from .tip import split_tip

main_blueprint = Blueprint('main', __name__)


@main_blueprint.route('/')
def index():
    return render_template('index.jinja2')


@main_blueprint.route('/bmi', methods=['GET', 'POST'])
def bmi():
    bmi_form = gen_bmi_form(request.form)
    if request.method == 'POST':

        try:
            bmi = calc_bmi(bmi_form.f.data, bmi_form.i.data, bmi_form.p.data)
        except Exception:
            bmi = -1

        return render_template('bmi.jinja2', form=bmi_form, bmi=bmi, post=1)
    else:
        return render_template('bmi.jinja2', form=bmi_form, distance=0, post=0)


@main_blueprint.route('/distance', methods=['GET', 'POST'])
def distance():
    dist_form = gen_dist_form(request.form)
    if request.method == 'POST':
        distance = calc_distance(dist_form.x1.data, dist_form.y1.data, dist_form.x2.data, dist_form.y2.data)
        return render_template('distance.jinja2', form=dist_form, distance=distance, post=1)
    else:
        return render_template('distance.jinja2', form=dist_form, distance=0, post=0)


@main_blueprint.route('/email', methods=['GET', 'POST'])
def email():
    email_form = gen_email_form(request.form)
    if request.method == 'POST':
        email = verify_email(email_form.email_input.data)
        return render_template('email.jinja2', form=email_form, email=email, post=True)
    else:
        return render_template('email.jinja2', form=email_form, email="", post=0)


@main_blueprint.route('/retirement', methods=['GET', 'POST'])
def retirement():
    retire_form = gen_retire_form(request.form)
    if request.method == 'POST':
        age = calc_retirement(retire_form.age.data, retire_form.salary.data, retire_form.percent.data, retire_form.goal.data)
        return render_template('retirement.jinja2', form=retire_form, age=age, post=1)
    else:
        return render_template('retirement.jinja2', form=retire_form, age=0, post=0)


@main_blueprint.route('/tip', methods=['GET', 'POST'])
def tip():
    tip_form = gen_tip_form(request.form)
    if request.method == 'POST':
        bills = split_tip(tip_form.bill.data, tip_form.guests.data)

        checks = list()
        if bills != False:
            guest = 1
            for amount in bills:
                temp_dict = dict({'guest': guest, 'amount': amount})
                checks.append(temp_dict)
                guest += 1

        return render_template('tip.jinja2', form=tip_form, bills=checks, post=1)
    else:
        return render_template('tip.jinja2', form=tip_form, bills=0, post=0)
