from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time


class Bot:
    start_url = "https://www.instagram.com/"

    def __init__(self, path: str, username: str):  # TODO: add more browser
        """
        :param path: absolut path to a webdriver
        :param username: a valid instagram username
        """

        self.username = username
        self.driver = webdriver.Chrome(path)

    def login(self, password: str):
        self.driver.get(self.start_url)
        time.sleep(5)
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

    def logout(self):
        menu = self.driver.find_element_by_xpath('//span[@class="_2dbep qNELH"]')
        menu.click()
        time.sleep(1)
        logout = self.driver.find_element_by_xpath('//div[@class="-qQT3"]')
        logout.click()

    def pm(self):
        pass

    def like(self):
        pass

    def commend(self):
        pass
