import datetime
from nose.tools import *

from pypiwik import User
from tests import PywikTestCase


class UserTestCase(PywikTestCase):

    def test_basic_creation(self):
        user = User(
            login='testuser',
            email='test@example.org',
        )

        assert_equal('testuser', user.login)
        assert_equal('test@example.org', user.email)

    def test_from_api_dict(self):
        user_dict = {
            'login': 'admin',
            'password': '01e6b375cab45dd3f9ae15a417aee257',
            'alias': 'Test User 0',
            'email': 'admin@example.org',
            'token_auth': '6a110eba31b4424558fb00c2a76f7380',
            'superuser_access': '1',
            'date_registered': '2014-09-30 17:39:38'
        }
        user = User(**user_dict)

        assert_equal(user_dict['login'], user.login)
        assert_equal(user_dict['alias'], user.alias)
        assert_equal(user_dict['email'], user.email)
        assert_equal(user_dict['token_auth'], user.token_auth)
        assert_equal(True, user.is_superuser)
        assert_equal(
            datetime.datetime.strptime(
                user_dict['date_registered'],
                '%Y-%m-%d %H:%M:%S'
            ),
            user.date_registered,
        )
