def monitor_health(data):
    heart_rate = data['heart_rate']
    if heart_rate > 100:   
        event = {
            "type": "abnormal_heart_rate",
            "data": data
        }
        event_bus.publish(event)
