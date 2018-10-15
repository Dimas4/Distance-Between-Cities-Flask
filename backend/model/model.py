from app.create_app import db


class DistanceModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city_1 = db.Column(db.String(100))
    city_2 = db.Column(db.String(100))
    distance = db.Column(db.Integer)
    __table_args__ = db.UniqueConstraint('city_1', 'city_2', name='_city_1_city_2'),

    def __repr__(self):
        return f"Book({self.city_1} and {self.city_2} = {self.distance})"
