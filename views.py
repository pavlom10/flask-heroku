from flask import request, jsonify
from flask.views import MethodView
from sqlalchemy import exc

from app import app, db
from models import Advertisement
import errors


class AdvertisementView(MethodView):

    def get(self, advertisement_id):
        print(advertisement_id)
        advertisement = Advertisement.query.get(advertisement_id)
        return jsonify(advertisement.to_dict())

    def post(self):
        advertisement = Advertisement(**request.json)
        db.session.add(advertisement)
        try:
            db.session.commit()
            return jsonify(advertisement.to_dict())
        except exc.IntegrityError:
            raise errors.BadLuck

    def patch(self, advertisement_id):
        advertisement = Advertisement.query.get(advertisement_id)
        advertisement.update(**request.json)
        try:
            db.session.commit()
            return jsonify(advertisement.to_dict())
        except exc.IntegrityError:
            raise errors.BadLuck

    def delete(self, advertisement_id):
        advertisement = Advertisement.query.get(advertisement_id)
        try:
            db.session.delete(advertisement)
            db.session.commit()
            return jsonify(advertisement.to_dict())
        except exc.IntegrityError:
            raise errors.BadLuck


app.add_url_rule(
    '/api/v1/<int:advertisement_id>',
    view_func=AdvertisementView.as_view('advertisement_get'),
    methods=['GET', ]
)
app.add_url_rule(
    '/api/v1',
    view_func=AdvertisementView.as_view('advertisement_post'),
    methods=['POST', ]
)
app.add_url_rule(
    '/api/v1/<int:advertisement_id>',
    view_func=AdvertisementView.as_view('advertisement_patch'),
    methods=['PATCH', ]
)
app.add_url_rule(
    '/api/v1/<int:advertisement_id>',
    view_func=AdvertisementView.as_view('advertisement_delete'),
    methods=['DELETE', ]
)


def nothing():
    pass
