from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time


class Bot:
    start_url = "https://www.instagram.com/"

    def __init__(self, path: str, username: str):  # TODO: add more browser support
        """
        :param path: absolut path to a webdriver
        :param username: a valid instagram username
        """

        self.username = username
        self.driver = webdriver.Chrome(path)

    def login(self, password: str) -> bool:
        """
        :param password: put in a valid instagram password in plaintext
        :return: bool
        """
        self.driver.get(self.start_url)
        time.sleep(5)
        try:
            user_field = self.driver.find_element_by_xpath('//input[@name="username"]')
            user_field.send_keys(self.username)
            passwd_field = self.driver.find_element_by_xpath('//input[@name="password"]')
            passwd_field.send_keys(password)
            submit_field = self.driver.find_element_by_xpath('//button[@type="submit"]')
            time.sleep(1)
            submit_field.send_keys(Keys.ENTER)
            time.sleep(5)
            if self.driver.find_element_by_xpath('//section[@class="ABCxa"]'):
                nn = self.driver.find_element_by_xpath('//div[@class="cmbtv"]/button')
                nn.send_keys(Keys.ENTER)
                time.sleep(3)
            if self.driver.find_element_by_xpath('//div[@class="_1XyCr"]'):
                nn = self.driver.find_element_by_xpath('//div[@class="mt3GC"]/button[2]')
                nn.send_keys(Keys.ENTER)
                time.sleep(1)
            return True
        except:
            return False

    def logout(self) -> bool:
        """
        :return: bool
        """
        menu = self.driver.find_element_by_xpath('//span[@class="_2dbep qNELH"]')
        menu.click()
        time.sleep(1)
        logout = self.driver.find_element_by_xpath('//div[@class="-qQT3"]')
        logout.click()
        return True

    def pm(self, msg: str, user_url=None, username=None) -> bool:
        """
        :param msg: the message itself
        :param user_url: profile url of the target
        :param username: targets username (experimental) !!!!
        :return: bool
        """
        msg = str(msg)
        if username:
            url = f"{self.start_url}{username}/"
        if user_url:
            url = user_url
        try:
            self.driver.get(url)
            time.sleep(4)
            sm = self.driver.find_element_by_xpath('//div[@class="_862NM"]//button')
            sm.click()
            time.sleep(4)
            tf = self.driver.find_element_by_xpath('//div[@class="X3a-9"]//textarea')
            tf.send_keys(msg)
            time.sleep(1)
            tf.send_keys(Keys.ENTER)
            return True
        except:
            return False

    def like(self) -> bool:
        pass

    def commend(self) -> bool:
        pass
