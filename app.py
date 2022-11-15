from flask import Flask, render_template, jsonify, request
from flask_pymongo import PyMongo
from datetime import datetime

mongo = PyMongo()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
# app.config[ 'MONGO_URI'] = 'mongodb+srv://lcusergps:A2kSols123@lcgpscluster.4oddxrt.mongodb.net/lcgpstracking?retryWrites=true'
app.config['MONGO_URI'] = 'mongodb+srv://flaskuser:A2kSols123@cluster0.vzyqo.mongodb.net/map_data?retryWrites=true'
mongo.init_app(app)


@app.route('/gps_tracking', methods=['POST'])
def index():
    try:
        time_now = datetime.now().time()
        time_now = time_now.strftime("%I:%M %p")
        finalgpscluster = mongo.db.finalgpscluster
        reservation_id = request.form.get('reservation_id')
        latitude = request.form.get("latitude")
        longitutde = request.form.get("longitude")
        if reservation_id and latitude and longitutde:
            finalgpscluster.insert_one({'reservation_id': reservation_id, 'latitude': latitude, 'longitude': longitutde,
                                        'time': time_now})
            return jsonify(
                {'reservation_id': reservation_id, 'latitude': latitude, 'longitude': longitutde, 'time': time_now})
        else:
            return "Please enter Both  Reservation_id , latitude , longitude"
    except Exception as e:
        print("error==", e)
        return "Something went wrong", 400


@app.route('/gps_tracking1', methods=['GET'])
def get_data():
    try:
        finalgpscluster = mongo.db.finalgpscluster
        data = finalgpscluster.find({'reservation_id': '27'})
        print("data is---", data)
        list_obj = list(data)
        data_obj = list_obj[len(list_obj) - 1]
        print("list=====", list_obj)
        print("list=====", data_obj)

        finalgpscluster = mongo.db.finalgpscluster
        return "Please enter Both  Reservation_id , latitude , longitude"
    except Exception as e:
        print("error==", e)
        return "Something went wrong", 400


if __name__ == '__main__':
    app.run(debug=True)
