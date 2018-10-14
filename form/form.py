from wtforms import Form, StringField, SubmitField


class SearchForm(Form):
    point_1 = StringField('point_1')
    point_2 = StringField('point_2')

    submit = SubmitField('Search')
