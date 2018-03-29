# -*- coding: utf-8 -*-

"""
Object type for user

"""

from collections import namedtuple
from .wrapper import namedtuple_with_defaults
from ..constants import ENDPOINTS

User = namedtuple_with_defaults(
    namedtuple('User',
               [
                   'areaCode',
                   'avatarImage',
                   'backgroundImage',
                   'bio',
                   'briefIntro',
                   'city',
                   'country',
                   'following',
                   'gender',
                   'id',
                   'initUsername',
                   'isBetaUser',
                   'isLoginUser',
                   'isVerified',
                   'mobilePhoneNumber',
                   'preferences',
                   'province',
                   'profileImageUrl',
                   'ref',
                   'screenName',
                   'statsCount',
                   'updatedAt',
                   'userId',
                   'username',
                   'usernameSet',
                   'verifyMessage',
                   'weiboUid',
                   'weiboUserInfo',
               ])
)


class Myself:
    def __init__(self, jike_session):
        self.jike_session = jike_session
        self.user, self.stats_count = self.fetch()

    def __repr__(self):
        return f'User({self.user.screenName})'

    def fetch(self):
        res = self.jike_session.get(ENDPOINTS['my_profile'])
        if res.ok:
            result = res.json()
        res.raise_for_status()
        return User(**result['user']), result['statsCount']
