from selenium import webdriver
from fixture.session import SessionHelper
from fixture.progect import ProgectHelper
from fixture.james import JamesHelper
from fixture.signup import SignupHelper
from fixture.mail import MailHelper



class Application:

    def __init__(self, browser, config):
        if browser == "firefox":
            self.wd = webdriver.Firefox(firefox_binary=r'C:/Program Files/Mozilla Firefox/firefox.exe')
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        # self.wd.implicitly_wait(1)
        self.james = JamesHelper(self)
        self.progect = ProgectHelper(self)
        self.session = SessionHelper(self)
        self.config = config
        self.mail = MailHelper(self)
        self.signup = SignupHelper(self)
        self.base_url = config['web']['baseUrl']

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()