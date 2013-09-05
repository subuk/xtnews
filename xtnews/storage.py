
import datetime
import pytz
import dateutil.parser

def now():
    return datetime.datetime.now(dateutil.tz.tzutc()).isoformat()

_DATA = [{
    'id': 1,
    'subject': 'First message',
    'text': "No body",
    'date_created': now()
},{
    'id': 2,
    'subject': 'Second message',
    'text': "No body",
    'date_created': now()
},{
    'id': 3,
    'subject': 'Breaking news!',
    'text': "No body",
    'date_created': now()
}]

class ValidationError(Exception):
    def __init__(self, item, errors):
        self.item = item
        self.errors = errors

def _validate(item):
    errors = {}

    if 'date_created' not in item:
        item['date_created'] = now()

    if not isinstance(item, datetime.datetime):
        try:
            item['date_created'] = dateutil.parser.parse(item['date_created']).astimezone(dateutil.tz.tzutc())
        except Exception, e:
            errors['date_created'] = repr(e)

    if not item['subject']:
        errors['subject'] = "This field is required"
    if not item['text']:
        errors['text'] = "This field is required"
    if errors:
        raise ValidationError(item, errors)

    return item

def all():
    return _DATA.__iter__()

def get(object_id):
    return _DATA[object_id + 1]

def add(object_id, obj):
    global _DATA
    obj['id'] = None
    _DATA.append(_validate(obj))
    obj['id'] = len(_DATA) - 1
    return obj

def delete(object_id):
    global _DATA
    del _DATA[object_id]

def update(object_id, obj):
    global _DATA
    _DATA[object_id] = _validate(obj)
