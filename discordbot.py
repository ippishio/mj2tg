# Module with DiscordBot class
# that is used to interact with Discord user client.
# There is some shitty lines, like constant time.sleep(), but i think
# it doesn't matter now

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time


class DiscordBot:
    def __init__(self, email, password, debug=False):
        self.email = email
        self.password = password
        authenticated = os.path.isdir("./selenium/")
        op = webdriver.ChromeOptions()
        if not debug:
            op.add_argument('--headless')  # turns on webdriver gui
        op.add_argument("user-data-dir=selenium")
        self.driver = webdriver.Chrome(
            ChromeDriverManager().install(), options=op)
        self.server = None
        self.channel = None
        self.textbox = None
        if not authenticated:
            self.login()

    def closeBrowser(self):
        self.driver.close()

    def login(self, redirect=False):
        driver = self.driver
        if not redirect:
            driver.get("https://discord.com/login")
        else:
            print("redirected")
            driver.find_element(By.CSS_SELECTOR, "[type=button]").click()
        try:
            email = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "[name=email]"))  # wait until loaded
            )
            password = driver.find_element(By.CSS_SELECTOR, "[name=password]")
            email.send_keys(self.email)
            password.send_keys(self.password)
            driver.find_element(By.CSS_SELECTOR, "[type=submit]").click()
            print("successful login")
        except:
            print("timeout")
        if not redirect:
            WebDriverWait(driver, 30).until(
                lambda driver: driver.current_url == "https://discord.com/app")  # wait for login

    def sendMessage(self, server: int, channel: int, message: str):
        driver = self.driver
        if (server != self.server or channel != self.channel):  # if server/channel changed
            driver.get("https://discord.com/channels/" +
                       str(server)+"/"+str(channel))
            self.server = server
            self.channel = channel
            try:
                time.sleep(1)
                print(driver.current_url)
                # time.sleep(600)
                if (driver.current_url.__contains__("?redirect_to=%2F")):
                    self.login(redirect=True)
                self.textbox = WebDriverWait(driver, 30).until(
                    EC.presence_of_element_located(
                        (By.XPATH, '//div[@role="textbox"]'))  # wait until loaded
                )
            except TimeoutError as e:
                print("timeout", e)
        if message.startswith("/imagine"):
            self.textbox.send_keys("/imagine")
            time.sleep(1)
            self.textbox.send_keys(Keys.SPACE)
            self.textbox.send_keys(message.replace("/imagine ", ""))
            self.textbox.send_keys(Keys.ENTER)
        else:
            self.textbox.send_keys(message)
            self.textbox.send_keys(Keys.ENTER)
            if message.startswith('/'):
                time.sleep(1)
                self.textbox.send_keys(Keys.ENTER)
                self.textbox.send_keys(Keys.ENTER)
                self.textbox.send_keys(Keys.ENTER)
