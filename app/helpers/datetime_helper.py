import datetime


def current_datetime() -> datetime.datetime:
    """
    Returns:
        datetime.datetime: the current date and time.
    """
    return datetime.datetime.now()


def current_datetime_as_string() -> str:
    """
    Returns:
        str: the current date and time in the format 'YYYY-MM-DD HH:MM:SS'.
    """
    return current_datetime().strftime("%Y-%m-%d %H:%M:%S")
