import requests
import json


def get_distance(point_1, point_2, url, key):
    data = {
          "locations": [
            point_1,
            point_2
          ],
        }
    data = requests.post(url.format(key),
                         data=json.dumps(data))
    data = data.json()

    if data.get('distance'):
        return max(data.get('distance'))
