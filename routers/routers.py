from backend.generate_json_response import generate_response
from backend.model.model import DistanceModel
from backend.get_distance import get_distance
from flask import render_template, request
from app.create_app import db, config
from flask_classy import FlaskView
from form.form import SearchForm


class View(FlaskView):
    def index(self):
        form = SearchForm(request.form)
        return render_template('start.html', form=form)

    def post(self):
        requets_dict = request.form.to_dict()
        point_1 = requets_dict['point_1']
        point_2 = requets_dict['point_2']

        if point_1 and point_2:
            distance = db.session.query(DistanceModel).filter_by(city_1=point_1, city_2=point_2).first()
            if not distance:
                distance = db.session.query(DistanceModel).filter_by(city_1=point_2, city_2=point_1).first()

            if not distance:
                print('Api')
                distance = get_distance(point_1, point_2, config['api']['url'], config['api']['token'])
                distance_object = DistanceModel(city_1=point_1, city_2=point_2,
                                                distance=distance)
                db.session.add(distance_object)
                db.session.commit()
            else:
                distance = distance.distance

            if distance:
                return generate_response({'answer': distance})
            else:
                return generate_response({'error': 'Incorrect Point 1 or Point 2'})
        else:
            return generate_response({'error': 'Point 1 or Point 2 does not exist!'})
