from bs4 import BeautifulSoup
import json


def parse_lesson_row(lesson):
    info = lesson.find_all('td')
    lesson_number = info[0].contents[0]

    time_bounds = "".join(str(item) for item in info[1].contents).replace('<br/>', ' - ')
    lesson_info = "".join(str(item) for item in info[2].contents).replace('<br/>', ' / ')\
                                                                 .replace(u'\xa0', u' ')

    parsed_lesson = {
            'number': lesson_number,
            'time_bounds': time_bounds,
            'info': lesson_info
    }

    return parsed_lesson


def parse_lessons(lessons):

    parsed_lessons = []

    for lesson_row in lessons:
        parsed_lesson = parse_lesson_row(lesson_row)
        parsed_lessons.append(parsed_lesson)

    return parsed_lessons


def parse_fragments(fragments):

    schedule = []

    for fragment in fragments:
        header = fragment.find_next('h4').contents
        date = header[0]
        day = header[1].contents[0]

        day_schedule = fragment.find_next('table')
        lessons = day_schedule.find_all('tr')
        parsed_lessons = parse_lessons(lessons)

        schedule_item = {
            'date': date,
            'day': day,
            'items': parsed_lessons

        }
        schedule.append(schedule_item)

    return schedule


def serialize_schedule(group, schedule):
    to_serialize = {
        'group': group,
        'schedule': schedule
    }
    schedule_json = json.dumps(to_serialize, ensure_ascii=False)
    return schedule_json


def parse_schedule(body):
    soup = BeautifulSoup(body, 'lxml')

    fragments_with_days = soup.find_all('div', class_='col-md-6')[1:]
    schedule = parse_fragments(fragments_with_days)

    return schedule




