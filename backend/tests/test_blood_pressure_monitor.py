import pytest
from event_bus import EventBus
from blood_pressure_monitor import BloodPressureMonitor

def test_blood_pressure_monitor():
    event_bus = EventBus()
    bp_monitor = BloodPressureMonitor()
    

    def mock_callback(event):
        assert event['data']['heart_rate'] > 100 
    
    abnormal_event = {
        "type": "abnormal_heart_rate",
        "data": {"heart_rate": 110}
    }
    
    bp_monitor.handle_abnormal_heart_rate(abnormal_event)
