import pytest
from event_bus import EventBus

def test_event_bus():
    event_bus = EventBus()
    
    def callback(event):
        assert event['data'] == 'test_data'
    
    event_bus.subscribe('test_event', callback)
    event_bus.publish({'type': 'test_event', 'data': 'test_data'})
