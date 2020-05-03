from flask import Flask, request, jsonify, make_response, abort
from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import ModelSchema
from flask_marshmallow import Marshmallow
from marshmallow import fields
import pymysql

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://Apollo:1207@127.0.0.1:3306/mydb"
db = SQLAlchemy(app)


class FootballField(db.Model):
    __tablename__ = "FootballFields"
    id = db.Column(db.Integer, primary_key=True)
    number_of_seats = db.Column(db.Integer, unique=False)
    year_of_foundation = db.Column(db.Integer, unique=False)
    location = db.Column(db.String(30), unique=False)
    scale_of_field = db.Column(db.Integer, unique=False)
    name_of_sport = db.Column(db.String(30), unique=False)
    roof_type = db.Column(db.String(30), unique=False)
    color_of_field = db.Column(db.String(30), unique=False)
    count_of_vip_places = db.Column(db.Integer, unique=False)

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self


db.create_all()


class FootballFieldSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = FootballField
        sql_session = db.session

    id = fields.Integer(dump_only=True)
    number_of_seats = fields.Integer(required=True)
    year_of_foundation = fields.Integer(required=True)
    location = fields.String(required=True)
    scale_of_field = fields.Integer(required=True)
    name_of_sport = fields.String(required=True)
    roof_type = fields.String(required=True)
    color_of_field = fields.String(required=True)
    count_of_vip_places = fields.Integer(required=True)


football_field_schema = FootballFieldSchema()
football_fields_schema = FootballFieldSchema(many=True)


@app.route("/footballFields", methods=["GET"])
def get_all_football_fields():
    get_football_fields = FootballField.query.all()
    if not get_football_fields:
        abort(404)
    football_fields = football_fields_schema.dump(get_football_fields)
    return make_response(jsonify({"footballField": football_fields}), 200)


@app.route("/footballField/<id>", methods=["GET"])
def get_football_field_by_id(id):
    get_football_field = FootballField.query.get(id)
    if not get_football_field:
        abort(404)
    football_fields = football_field_schema.dump(get_football_field)
    return make_response(jsonify({"footballField": football_fields}), 200)


@app.route("/footballField", methods=["POST"])
def create_football_field():
    data = request.get_json()
    football_field = football_field_schema.load(data)
    football_fields = football_field_schema.dump(football_field.create())
    return make_response(jsonify({"footballField": football_fields}), 200)


@app.route("/footballField/<id>", methods=["PUT"])
def update_sport_build_by_id(id):
    data = request.get_json()
    get_football_field = FootballField.query.get(id)
    if data.get("number_of_seats"):
        get_football_field.number_of_seats = data["number_of_seats"]
    if data.get("year_of_foundation"):
        get_football_field.year_of_foundation = data["year_of_foundation"]
    if data.get("location"):
        get_football_field.location = data["location"]
    if data.get("scale_of_field"):
        get_football_field.scale_of_field = data["scale_of_field"]
    if data.get("name_of_sport"):
        get_football_field.name_of_sport = data["name_of_sport"]
    if data.get("roof_type"):
        get_football_field.roof_type = data["roof_type"]
    if data.get("color_of_field"):
        get_football_field.color_of_field = data["color_of_field"]
    if data.get("count_of_vip_places"):
        get_football_field.count_of_vip_places = data["count_of_vip_places"]

    db.session.add(get_football_field)
    db.session.commit()
    football_fields = football_field_schema.dump(get_football_field)
    return make_response(jsonify({"footballField": football_fields}), 200)


@app.route("/footballField/<id>", methods=["DELETE"])
def delete_football_field_by_id(id):
    get_football_field = FootballField.query.get(id)
    if not get_football_field:
        abort(404)
    db.session.delete(get_football_field)
    db.session.commit()
    return make_response("", 200)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="80")
