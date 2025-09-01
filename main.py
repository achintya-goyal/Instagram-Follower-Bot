import time

from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

ACCOUNT = "leomessi" # Change this to an account of your choice
USERNAME = "your username"
PASSWORD = "your password"


class InstaFollower:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(chrome_options)
        self.wait = WebDriverWait(self.driver, timeout=3)


    def login(self):
        url = "https://www.instagram.com/accounts/login/"
        self.driver.get(url)
        time.sleep(4.3)
        username = self.driver.find_element(By.NAME, value="username")
        password = self.driver.find_element(By.NAME, value="password")

        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)
        time.sleep(2.1)

        password.send_keys(Keys.ENTER)
        time.sleep(9.4)

    def follow(self):
        time.sleep(1.2)
        self.driver.get(f"https://www.instagram.com/{ACCOUNT}/")

        time.sleep(0.3)

        follower_click = self.driver.find_element(By.XPATH, "//a[contains(@href, '/followers/')]")
        follower_click.click()

        time.sleep(1.3)
        follow_buttons = self.driver.find_elements(By.XPATH, '//div[text()="Follow"]')

        for button in follow_buttons:
            try:
                button.click()
                time.sleep(1.2)
            except ElementClickInterceptedException:
                temp = self.driver.find_element(By.XPATH, '//div[text()="Follow"]')
                temp.click()
                time.sleep(3)


bot = InstaFollower()
bot.login()
bot.follow()