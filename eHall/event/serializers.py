from datetime import datetime
import decimal
import json

# Source: jgbarah http://stackoverflow.com/a/22238613/ (modified)
class EventSerializer(json.JSONEncoder):
    def __init__(self, **kwargs):
        super(EventSerializer, self).__init__(**kwargs)
        
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        if isinstance(obj, decimal.Decimal):
            return float(obj)
        return json.JSONEncoder.default(self, obj)
    