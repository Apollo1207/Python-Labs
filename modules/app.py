from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import ModelSchema
from flask_marshmallow import Marshmallow
from marshmallow import fields
import pymysql

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://Apollo:1207@127.0.0.1:3306/db"
db = SQLAlchemy(app)


class SportBuild(db.Model):
    __tablename__ = "SportBuilds"
    id = db.Column(db.Integer, primary_key=True)
    number_of_seats = db.Column(db.Integer)
    year_of_foundation = db.Column(db.Integer)
    location = db.Column(db.String(30))
    scale_of_field = db.Column(db.Integer)
    name_of_sport = db.Column(db.String(30))

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self


db.create_all()


class SportBuildSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = SportBuild
        sql_session = db.session

    id = fields.Integer(dump_only=True)
    number_of_seats = fields.Integer(required=True)
    year_of_foundation = fields.Integer(required=True)
    location = fields.String(required=True)
    scale_of_field = fields.Integer(required=True)
    name_of_sport = fields.String(required=True)


@app.route('/sportBuilds', methods=['GET'])
def get_all_sport_builds():
    get_sport_builds = SportBuild.query.all()
    sport_build_schema = SportBuildSchema(many=True)
    sport_builds = sport_build_schema.dump(get_sport_builds)
    return make_response(jsonify({"sportBuild": sport_builds}))


@app.route('/sportBuilds/<id>', methods=['GET'])
def get_sport_build_by_id(id):
    get_sport_build = SportBuild.query.get(id)
    sport_build_schema = SportBuildSchema()
    sport_builds = sport_build_schema.dump(get_sport_build)
    return make_response(jsonify({"sportBuild": sport_builds}))


@app.route('/sportBuilds', methods=['POST'])
def create_sport_build():
    data = request.get_json()
    sport_build_schema = SportBuildSchema()
    sport_build = sport_build_schema.load(data)
    sport_builds = sport_build_schema.dump(sport_build.create())
    return make_response(jsonify({"sportBuild": sport_builds}), 200)


@app.route('/sportBuilds/<id>', methods=['PUT'])
def update_sport_build_by_id(id):
    data = request.get_json()
    get_sport_build = SportBuild.query.get(id)
    if data.get('number_of_seats'):
        get_sport_build.number_of_seats = data['number_of_seats']
    if data.get('year_of_foundation'):
        get_sport_build.year_of_foundation = data['year_of_foundation']
    if data.get('location'):
        get_sport_build.location = data['location']
    if data.get('scale_of_field'):
        get_sport_build.scale_of_field = data['scale_of_field']
    if data.get('name_of_sport'):
        get_sport_build.name_of_sport = data['name_of_sport']

    db.session.add(get_sport_build)
    db.session.commit()
    sport_build_schema = SportBuildSchema(only=["id", "number_of_seats", "year_of_foundation", "location",
                                                "scale_of_field", "name_of_sport"])
    sport_builds = sport_build_schema.dump(get_sport_build)
    return make_response(jsonify({"sportBuild": sport_builds}))


@app.route('/sportBuilds/<id>', methods=['DELETE'])
def delete_sport_build_by_id(id):
    get_sport_build = SportBuild.query.get(id)
    db.session.delete(get_sport_build)
    db.session.commit()
    return make_response("", 204)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="80")
