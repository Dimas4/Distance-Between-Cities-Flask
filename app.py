import yaml

from flask import Flask, render_template, request, jsonify
from backend.get_distance import get_distance
from form.form import SearchForm


app = Flask(__name__)

with open('config.yaml', 'r') as file:
    config = yaml.load(file)['api']


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    form = SearchForm(request.form)
    if request.method == 'POST' and form.validate():
        point_1 = form.point_1.data
        point_2 = form.point_2.data

        if point_1 and point_2:
            distance = get_distance(point_1, point_2, config['url'], config['token'])
            if distance:
                return jsonify({'answer': distance})
            else:
                return jsonify({'error': 'Incorrect Point 1 or Point 2'})
        else:
            return jsonify({'error': 'Point 1 or Point 2 does not exist!'})

    return render_template('start.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
