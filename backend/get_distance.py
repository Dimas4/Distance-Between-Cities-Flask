import requests
import json

from pprint import pprint


def get_distance(point_1, point_2, url, key):
    data = {
          "locations": [
            point_1,
            point_2
          ],
          "options": {
            "allToAll": True
          }
        }
    data = requests.post(url.format(key),
                         data=json.dumps(data)).json()

    if data.get('distance'):
        return max(data.get('distance')[0])
