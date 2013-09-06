
import datetime
import pytz
import dateutil.parser

def now():
    return datetime.datetime.now(dateutil.tz.tzutc()).isoformat()

_DATA = [{
    'id': 1,
    'subject': 'Obama pushes for support on Syria',
    'text': "US President Obama uses his final day at the G20 summit to push for support for a military strike on Syria, but global leaders remain deeply divided.",
    'date_created': now()
},{
    'id': 2,
    'subject': 'Dutch liable for Srebrenica deaths',
    'text': "The Dutch supreme court rules that the Netherlands is liable for the deaths of three Bosnian Muslim men killed during the 1995 Srebrenica massacre.",
    'date_created': now()
},{
    'id': 3,
    'subject': "US and UK 'crack online encryption'",
    'text': "US and UK intelligence agencies reportedly crack technology used to encrypt internet services such as online banking, medical records and email.",
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
