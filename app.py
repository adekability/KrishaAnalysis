""" app - main module """
from flask import Flask, request
from services.mapworker import MapWorker

app = Flask(__name__)


@app.route("/map", methods=['GET'])
def get_map():
    """ get_map - main function"""
    longitude = float(request.args.get("lon"))
    latitude = float(request.args.get("lat"))
    return MapWorker(longitude=longitude,
                     latitude=latitude).fetch_map_by_coordinates()


if __name__ == "__main__":
    app.run()
