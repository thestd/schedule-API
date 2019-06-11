from bs4 import BeautifulSoup


__all__ = ["parse_schedule", "parse_faculties", ]


def _parse_raw_lesson(raw_lesson):
    # Todo: provide docstring
    info = raw_lesson.find_all('td')
    lesson_number = info[0].contents[0]

    time_bounds = "".join(str(item) for item in info[1].contents)\
        .replace('<br/>', ' - ')
    lesson_info = "".join(str(item) for item in info[2].contents)\
        .replace('<br/>', ' / ').replace(u'\xa0', u' ')

    parsed_lesson = {
            'number': lesson_number,
            'time_bounds': time_bounds,
            'info': lesson_info
    }

    return parsed_lesson


def _check_lesson_is_empty(parsed_lesson):
    # Todo: provide docstring
    return not parsed_lesson['info'].strip()


def _parse_raw_lessons(raw_lessons):
    # Todo: provide docstring
    parsed_lessons_list = []
    for raw_lesson in raw_lessons:
        parsed_lesson = _parse_raw_lesson(raw_lesson)
        if not _check_lesson_is_empty(parsed_lesson):
            parsed_lessons_list.append(parsed_lesson)

    return parsed_lessons_list


def _parse_raw_day(fragment):
    # Todo: provide docstring
    header = fragment.find_next('h4').contents
    day_schedule = fragment.find_next('table')
    raw_lessons = day_schedule.find_all('tr')

    date = header[0]
    day = header[1].contents[0]
    parsed_lessons_list = _parse_raw_lessons(raw_lessons)

    return date, day, parsed_lessons_list


def _parse_raw_days(raw_days_list):
    # Todo: provide docstring
    schedule = []
    for raw_day in raw_days_list:
        date, day, parsed_lessons_list = _parse_raw_day(raw_day)
        schedule_item = {
            'date': date,
            'day': day,
            'items': parsed_lessons_list

        }
        schedule.append(schedule_item)

    return schedule


def parse_schedule(body):
    # Todo: provide docstring
    soup = BeautifulSoup(body, 'lxml')
    raw_days_list = soup.find_all('div', class_='col-md-6')[1:]
    schedule = _parse_raw_days(raw_days_list)

    return schedule


def _parse_options_list(options):
    # Todo: provide docstring
    faculties_list = []
    for option in options:
        faculties_list.append({
            'name': option.text,
            'code': int(option['value'])
        })

    return faculties_list


def parse_faculties(body):
    # Todo: provide docstring
    soup = BeautifulSoup(body, 'lxml')
    form_field = soup.find('select', id='faculty')
    options = form_field.find_all('option')[1:]
    faculties_list = _parse_options_list(options)

    return faculties_list


