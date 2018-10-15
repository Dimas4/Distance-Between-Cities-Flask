
from flask import render_template, request
from service.service import Service
from flask_classy import FlaskView
from form.form import SearchForm


service = Service()


class View(FlaskView):
    def index(self):
        form = SearchForm(request.form)
        return render_template('start.html', form=form)

    def post(self):
        requets_dict = request.form.to_dict()
        return service.post(requets_dict['point_1'], requets_dict['point_2'])
