from app.create_app import db


class DistanceModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city_1 = db.Column(db.String(100))
    city_2 = db.Column(db.String(100))
    distance = db.Column(db.Integer)
    __table_args__ = db.UniqueConstraint('city_1', 'city_2', name='_city_1_city_2'),

    @classmethod
    def check_points(cls, point_1, point_2):
        distance = db.session.query(cls).filter_by(city_1=point_1, city_2=point_2).first()
        if not distance:
            distance = db.session.query(cls).filter_by(city_1=point_2, city_2=point_1).first()
        return distance.distance if distance else None

    @classmethod
    def create_object(cls, city_1, city_2, distance):
        distance_object = cls(city_1=city_1, city_2=city_2, distance=distance)
        db.session.add(distance_object)
        db.session.commit()

    def __repr__(self):
        return f"Distance({self.city_1} and {self.city_2} = {self.distance})"
