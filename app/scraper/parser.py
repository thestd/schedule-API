from bs4 import BeautifulSoup


__all__ = ["parse_schedule", "parse_faculties", ]


def _parse_raw_lesson(raw_lesson):
    """

    Args:
        raw_lesson: 'BeautifulSoup' objects contains lesson info
    Returns:
        dict: info about lesson
        {
            'number': str,
            'time_bounds': str,
            'info': str
        }
    """
    info = raw_lesson.find_all('td')
    lesson_number = info[0].get_text()
    time_bounds = "".join(str(item) for item in info[1].contents)\
        .replace('<br/>', ' - ')
    lesson_info = info[2].get_text()

    return {
            'number': lesson_number,
            'time_bounds': time_bounds,
            'info': lesson_info
    }


def _check_lesson_is_empty(parsed_lesson):
    """
    Checking lesson for being empty

    Args:
        parsed_lesson (dict): Parsed lesson

    Return:
        bool: True if parsed_lesson['info'] have any content except whitespaces, else False
    """
    return not parsed_lesson['info'].strip()


def _parse_raw_lessons(raw_lessons):
    """

    Args:
         raw_lessons (list): list of the 'BeautifulSoup'

    Returns:
        list[dict]: list of the parsed lessons

    """
    parsed_lessons_list = []
    for raw_lesson in raw_lessons:
        parsed_lesson = _parse_raw_lesson(raw_lesson)
        if not _check_lesson_is_empty(parsed_lesson):
            parsed_lessons_list.append(parsed_lesson)

    return parsed_lessons_list


def _parse_raw_day(fragment):
    """
    Taking all the info we need from the object

    Args:
        fragment: 'BeautifulSoup' objects contains day info ('div' with class 'col-md-6')

    Returns:
        tuple: (str, str, list): Tuple contains date, day and list of the lessons

    """
    header = fragment.find_next('h4').contents
    day_schedule = fragment.find_next('table')
    raw_lessons = day_schedule.find_all('tr')

    date = header[0]
    day = header[1].contents[0]
    parsed_lessons_list = _parse_raw_lessons(raw_lessons)

    return date, day, parsed_lessons_list


def _parse_raw_days(raw_days_list):
    """

    Args:
        raw_days_list (list): list of the 'BeautifulSoup' objects ('div' with class 'col-md-6')

    Returns:
        list[dict]:


        [
          {
            'date': str,
            'day': str,
            'items': [
              {
                'number': str,
                'time_bounds': str,
                'info': str
              }
        ]

    """
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
    """
    Find all html parts with day schedule and pass them to _parse_raw_days() function

    Args:
        body (str): Request response body

    Returns:
        list[dict]: list of dicts


        [
          {
            'date': str,
            'day': str,
            'items': [
              {
                'number': str,
                'time_bounds': str,
                'info': str
              }
        ]


    """
    soup = BeautifulSoup(body, 'lxml')
    raw_days_list = soup.find_all('div', class_='col-md-6')[1:]
    schedule = _parse_raw_days(raw_days_list)

    return schedule


def _parse_options_list(options):
    """
    Args:
        options: list of the BeautifulSoup objects

    Returns:
        list[dict]: list of parsed info about faculties
    """
    faculties_list = []
    for option in options:
        faculties_list.append({
            'name': option.text,
            'code': int(option['value'])
        })

    return faculties_list


def parse_faculties(body):
    """
    Args:
        body (str): Request response body

    Returns:
        list[dict]: list of the faculties codes and names
    """
    soup = BeautifulSoup(body, 'lxml')
    form_field = soup.find('select', id='faculty')
    options = form_field.find_all('option')[1:]
    faculties_list = _parse_options_list(options)

    return faculties_list


