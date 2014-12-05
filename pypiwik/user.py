import datetime


class User(object):

    def __init__(self, login=None, email=None, **kwargs):
        self.login = login
        self.email = email
        self.alias = kwargs.get('alias')
        self.token_auth = kwargs.get('token_auth')

        # If supplied by a user, expect it to be a bool
        self.is_superuser = kwargs.get('is_superuser')
        if self.is_superuser is None:
            # If coming from the API, this is a string "0" or "1"
            self.is_superuser = bool(int(kwargs.get('superuser_access', '0')))

        self.date_registered = kwargs.get('date_registered')
        if (
            self.date_registered is not None
            and not isinstance(self.date_registered, datetime.datetime)
        ):
            self.date_registered = datetime.datetime.strptime(
                self.date_registered,
                '%Y-%m-%d %H:%M:%S',
            )

    def __eq__(self, other):
        return self.login == other.login