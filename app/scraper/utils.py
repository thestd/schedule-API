from app import options


__all__ = ["prepare_post_data", ]


def prepare_post_data(**kwargs):
    """
    Returns:
        dict: dict, prepared to use as body in POST request.

    """
    group = kwargs.get('group', '')
    faculty = kwargs.get('faculty', '')
    teacher = kwargs.get('teacher', '')
    sdate = kwargs.get('date_from', '')
    edate = kwargs.get('date_to', '')

    post_data = {
        'faculty': faculty,
        'teacher': teacher.encode(options.BASE_ENCODING),
        'group': group.encode(options.BASE_ENCODING),
        'sdate': sdate.encode(options.BASE_ENCODING),
        'edate': edate.encode(options.BASE_ENCODING),
        'n': 700
    }

    return post_data
