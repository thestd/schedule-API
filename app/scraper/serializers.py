import ujson as json


__all__ = ["serialize_schedule", "serialize_list", ]


def serialize_schedule(query, q_type, schedule):
    to_serialize = {
        q_type: query,
        'schedule': schedule
    }
    schedule_json = json.dumps(to_serialize, ensure_ascii=False)
    return schedule_json


def serialize_list(some_list):
    # Todo: provide docstring
    return json.dumps(some_list, ensure_ascii=False)
