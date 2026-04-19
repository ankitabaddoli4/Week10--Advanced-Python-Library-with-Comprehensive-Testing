import json

def to_json(data):
    return json.dumps(data)


def from_json(data: str):
    return json.loads(data)