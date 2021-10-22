# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from app.base.forms import CreateAccountForm
from app.home import blueprint
from flask import jsonify, render_template, redirect, request, url_for, flash
from flask_login import login_required, current_user
from app import login_manager
from app.home.data_push import push
from app.home.forms import CreateUser
from jinja2 import TemplateNotFound

@blueprint.route('/index')
@login_required
def index():


    return render_template('index.html', title='Dashboard')

@blueprint.route('/create_user', methods=['GET', 'POST'])
@login_required
def create_user():
    form = CreateUser()
    if form.validate_on_submit():
        entry = [str(form.username.data), str(form.email.data), str(form.first_name.data), str(form.last_name.data)]
        push(entry)
        flash('User created successfully!')
        return redirect(url_for('home_blueprint.create_user'))

    else:
        return render_template('create_user.html', title='Create User', form=form)

@blueprint.route('/<template>')
def route_template(template):

    try:

        if not template.endswith( '.html' ):
            template += '.html'

        return render_template( template )

    except TemplateNotFound:
        return render_template('page-404.html'), 404
    
    except:
        return render_template('page-500.html'), 500
