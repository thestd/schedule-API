import json


__all__ = ["serialize_schedule", "serialize_list", ]


def serialize_schedule(group, schedule):
    # Todo: provide docstring
    to_serialize = {
        'group': group,
        'schedule': schedule
    }
    schedule_json = json.dumps(to_serialize, ensure_ascii=False)
    return schedule_json


def serialize_list(some_list):
    # Todo: provide docstring
    return json.dumps(some_list, ensure_ascii=False)
