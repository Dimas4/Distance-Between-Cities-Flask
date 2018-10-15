from backend.generate_json_response import generate_response
from backend.model.model import DistanceModel
from backend.get_distance import get_distance
from app.create_app import config


class Service:
    def post(self, point_1, point_2):
        if point_1 and point_2:
            distance = DistanceModel.check_points(point_1, point_2)

            if not distance:
                distance = get_distance(point_1, point_2, config['api']['url'], config['api']['token'])
                DistanceModel.create_object(city_1=point_1, city_2=point_2,
                                            distance=distance)

            if distance:
                return generate_response({'answer': distance})
            else:
                return generate_response({'error': 'Incorrect Point 1 or Point 2'})
        else:
            return generate_response({'error': 'Point 1 or Point 2 does not exist!'})
