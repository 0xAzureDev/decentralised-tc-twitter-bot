from datetime import datetime, timedelta


def __suffix(d: str) -> str:
    return 'th' if 11 <= d <= 13 else {1: 'st', 2: 'nd', 3: 'rd'}.get(d % 10, 'th')


def __custom_strftime(format: str, t) -> str:
    return t.strftime(format).replace('{S}', str(t.day) + __suffix(t.day))


def get_expiration_date() -> str:
    """
    Get expiration date
    -------------------

    Generates an expiration date 12 hours from now.
    """

    now = datetime.utcnow()
    expiration_date = now + timedelta(hours=12)

    expiration_link = f'https://time.is/{expiration_date.strftime("%H%M_%d_%b_%Y")}_in_UTC'
    expiration_string = __custom_strftime(
        '{S} %b, %Y @ %H:%M %p UTC',
        expiration_date
    )

    return [f'[{expiration_string}]({expiration_link})', expiration_date]


def is_expired(expiration_date) -> bool:
    """
    Is Expired
    ----------

    Check if the expiration date has passed.

    :param expiration_date: The expiration date to check against
    """

    return expiration_date <= datetime.utcnow()
