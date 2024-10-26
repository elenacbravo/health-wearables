from event_bus import event_bus

class BloodPressureMonitor:
    def __init__(self):
        
        event_bus.subscribe('abnormal_heart_rate', self.handle_abnormal_heart_rate)
        self.type = "blood_pressure_monitor"
        self.status = "active"

    def handle_abnormal_heart_rate(self, event):
        print(f"Received abnormal heart rate event: {event}")
        self.take_reading()

    def take_reading(self):
        print(f"Taking blood pressure reading for {self.type}.")
        bp_reading = {
            "systolic": 120,
            "diastolic": 80
        }
        print(f"Blood Pressure Reading: {bp_reading['systolic']}/{bp_reading['diastolic']}")
