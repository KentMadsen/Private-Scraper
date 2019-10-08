from selenium import webdriver
import time

global_firefox_path = './drivers/geckodriver.exe'


class Crawler:
    global global_firefox_path

    """ """

    def __init__(self):
        self.title = None
        self.url = None
        self.delay_factor = 5

        self.browser = None

    def set_url(self, VARIABLE_VALUE):
        self.url = VARIABLE_VALUE

    def get_url(self):
        return self.url

    def initialise(self):
        self.browser = webdriver.Firefox(executable_path=global_firefox_path)
        return None

    def get(self):
        self.browser.get(self.get_url())

        time.sleep(self.delay_factor)

        self.title = self.browser.title

    def close(self):
        self.browser.close()

        return None
