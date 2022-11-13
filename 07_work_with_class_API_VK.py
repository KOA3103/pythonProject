from pydantic import BaseModel
import requests
from urllib.parse import urlencode
from my_token import TOKEN_VK

"""Работа с классами на примере API VK"""

class DisplayTypes(BaseModel):
    page: str = "page"
    popup: str = "popup"


class ScopeTypes(BaseModel):
    FRIENDS: str = "friends"
    WALL: str = "wall"

    def scope_list(self):
        return [self.FRIENDS, self.WALL]

    @property
    def scope(self):
        return ", ".join(self.scope_list())

APP_ID = 0000000

class VKClient:
     BASE_URL: str = "https://api.vk.com/method/"
     URL_AUTH: str = "https://oauth.vk.com/authorize"
     URL_REDIRECT: str = "https://oauth.vk.com/blank.html"
     METHOD_GET_FRIENDS: str = "friends.get"
     PROTOCOL_VERSION: str = "5.131"

     def __init__(self, token: str=None, user_id: str="1"):
         self.token = token
         self.user_id = user_id

     def get_token(self):
         param = {
             "client_id": APP_ID,
             "redirect_uri": self.URL_REDIRECT,
             "display": DisplayTypes().page,
             "scope": 'friends, status, wall, groups, stats, offline',
             "response_type""token"
         }
         print("Нажать => ", '?'.join((self.URL_AUTH, urlencode(param))))
