from flask import Flask, jsonify, request
from event_bus import EventBus
from models import db, HealthWearable  
from config import Config
from database import init_db
import logging


logging.basicConfig(filename='logs/app.log', level=logging.INFO)

app = Flask(__name__)
app.config.from_object(Config)

event_bus = EventBus()

@app.route('/wearables', methods=['POST'])
def register_wearable():
    data = request.json
    wearable = HealthWearable(**data)
    db.session.add(wearable)
    db.session.commit()
    return jsonify({"message": "Wearable registered!"}), 201

@app.route('/events', methods=['POST'])
def publish_event():
    event = request.json
    event_bus.publish(event)
    logging.info(f"Event published: {event}")
    return jsonify({"message": "Event published!"}), 200

@app.route('/health_check', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":
    init_db(app)
    app.run(host='0.0.0.0', port=5000)
