from health_monitor import monitor_health
from event_bus import EventBus

def test_monitor_health():
    event_bus = EventBus()
    
    def callback(event):
        assert event['data']['heart_rate'] == 110
    
    event_bus.subscribe('abnormal_heart_rate', callback)
    
    monitor_health({'heart_rate': 110})
