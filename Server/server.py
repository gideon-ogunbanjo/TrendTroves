from flask import Flask, request, jsonify
import util
app = Flask(__name__)

@app.route('/get_location_name')
def get_location_name():
    response = jsonify({
        'locations' : util.get_location_names()
    })
    return 'Hi'


if __name__ == "__main__":
    print("Starting Python Flask Server for Predictions")
    app.run(debug=True)