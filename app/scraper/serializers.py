import json


def serialize_schedule(group, schedule):
    to_serialize = {
        'group': group,
        'schedule': schedule
    }
    schedule_json = json.dumps(to_serialize, ensure_ascii=False)
    return schedule_json


def serialize_faculties(faculties_list):
    return json.dumps(faculties_list, ensure_ascii=False)
