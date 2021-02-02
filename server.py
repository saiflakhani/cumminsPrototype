"""
Main module of the server file
"""

# 3rd party moudles
from flask import render_template, Flask
import connexion
import db
import mqtt_messaging
from flask_cors import CORS, cross_origin
from config import FLASK_HOST, FLASK_PORT
import logging
from art import tprint

# Create the application instance
app = Flask(__name__, template_folder="./frontend", static_folder="./frontend")
app2 = connexion.App(__name__, specification_dir="./")
app2.app = Flask(__name__, template_folder="./frontend", static_folder="./frontend", static_url_path="/")
cors = CORS(app2.app)



# Read the swagger.yml file to configure the endpoints
app2.add_api("swagger.yml")
# api_doc(app2.app, config_path='swagger.yml', url_prefix='/api/ui_new', title='API doc')
# app2.app.after_request(set_cors_headers_on_response)

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

# create a URL route in our application for "/"
@app2.route("/")
@cross_origin()
def home():
    """
    This function just responds to the browser URL
    localhost:5000/

    :return:        the rendered template "home.html"
    
    """
    return render_template('home.html')

## FOR CORS
def set_cors_headers_on_response(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'X-Requested-With'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS'
    return response


if __name__ == "__main__":
    tprint("CUMMINS", font="starwars")
    print("Creating all tables...")
    db.create_all_tables()
    print("Initialising MQTT...")
    mqtt_messaging.init_mqtt()
    app2.run(host=FLASK_HOST, port=FLASK_PORT, debug=False)
