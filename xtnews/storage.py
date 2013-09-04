
import pytz
import datetime

_DATA = [{
    'id': 1,
    'subject': 'First message',
    'text': "No body",
    'date_created': datetime.datetime.now(pytz.UTC).isoformat()
},{
    'id': 2,
    'subject': 'Second message',
    'text': "No body",
    'date_created': datetime.datetime.now(pytz.UTC).isoformat()
},{
    'id': 3,
    'subject': 'Breaking news!',
    'text': "No body",
    'date_created': datetime.datetime.now(pytz.UTC).isoformat()
}]

def all():
    return _DATA.__iter__()

def get(object_id):
    return _DATA[object_id + 1]

def add(obj):
    global _DATA
    _DATA.append(obj)
    obj['id'] = len(_DATA) - 1

def delete(object_id):
    global _DATA
    del _DATA[object_id]

def update(object_id, obj):
    global _DATA
    _DATA[object_id] = obj
