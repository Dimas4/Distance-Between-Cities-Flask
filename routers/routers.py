from backend.generate_json_response import generate_response
from backend.model.model import DistanceModel
from backend.get_distance import get_distance
from flask import render_template, request
from form.form import SearchForm
from app.create_app import db
from run import app, config


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    db.create_all()
    form = SearchForm(request.form)
    if request.method == 'POST' and form.validate():
        point_1 = form.point_1.data
        point_2 = form.point_2.data

        if point_1 and point_2:
            distance = db.session.query(DistanceModel).filter_by(city_1=point_1, city_2=point_2).first()
            if not distance:
                distance = db.session.query(DistanceModel).filter_by(city_1=point_2, city_2=point_1).first()

            if not distance:
                distance = get_distance(point_1, point_2, config['url'], config['token'])
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

    return render_template('start.html', form=form)
