from requests import Session
from bot.customtypes import WrongPassword
from os import getenv
from json import loads
from dotenv import load_dotenv
load_dotenv()


class User:
    URL = "https://mafia.gg/api/user-session"
    headers = {
        "Host": "mafia.gg",
        "Origin": "https://mafia.gg",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    }
    def __init__(self):
        with Session() as s:
            cookie = s.post(self.URL, json={'login': getenv('MAFIA_GG_USERNAME'), 'password': getenv('MAFIA_GG_PASSWORD')}, headers=self.headers)
            print(cookie)
        if cookie.status_code == 401:
            raise WrongPassword("You provided incorrect password")
        self.response = loads(cookie.text)
        self.cookie = cookie.cookies.get_dict()