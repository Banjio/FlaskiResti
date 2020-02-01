from dotenv import load_dotenv
load_dotenv()
from flask import request, jsonify, abort
from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy

# local import
from instance.config import app_config

# init sql-alchemy

db = SQLAlchemy()

def create_app(config_name):
    from app.models import BucketList
    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    @app.route('/bucketlists/', methods=['POST', 'GET'])
    def bucketlists():
        if request.method == 'POST':
            name = str(request.data.get('name', ''))
            if name:
                bucketlist = BucketList(name=name)
                bucketlist.save()
                response = jsonify({
                    'id': bucketlist.id,
                    'name': bucketlist.name,
                    'date_created': bucketlist.date_created,
                    'date_modified': bucketlist.date_modified
                })
                response.status_code = 201
                return response
        else:
            # GET
            bucketlists = BucketList.get_all()
            results = list(map(lambda bucket: dict(id=bucket.id, name=bucket.name, date_created=bucket.date_created,
                                                   date_modified=bucket.date_modified), bucketlists))
            response = jsonify(results)
            response.status_code = 200
            return response

    @app.route('/bucketlists/<int:id>', methods=['GET','PUT', 'DELETE'])
    def bucketlist_manipulation(id, **kwargs):
        #retrieve a bucketlis using it's ID
        bucketlist = BucketList.query.filter_by(id=id).first()
        if not bucketlist:
            # Raise HTTP Exception with a 404 not found status code
            abort(404)

        if request.method == 'DELETE':
            bucketlist.delete()
            return {"message": f"bucketlist {bucketlist.id} deleted succesfully"}

        elif request.method == 'PUT':
            name = str(request.data.get('name', ''))
            bucketlist.name = name
            bucketlist.save()
            response = jsonify({
                'id': bucketlist.id,
                'name': bucketlist.name,
                'date_created': bucketlist.date_created,
                'date_modified': bucketlist.date_modified
            })
            response.status_code = 200
            return response
        else:
            response = jsonify({
                'id': bucketlist.id,
                'name': bucketlist.name,
                'date_created': bucketlist.date_created,
                'date_modified': bucketlist.date_modified
            })
            response.status_code = 200
            return response

    return app

