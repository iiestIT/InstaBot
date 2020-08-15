from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

from typing import List, Dict, Optional, Union, Any
from pydantic import BaseModel


class Bot(BaseModel):
    def __int__(self, driver: Any, username: str):
        self.driver = driver
        self.username = username
        self.start_url: str = "https://www.instagram.com/"

    def login(self, password: str):
        pass

    def logout(self):
        pass

    def pm(self):
        pass

    def like(self):
        pass

    def commend(self):
        pass
