import time
import string
import random

class ProgectHelper:

    def __init__(self, app):
        self.app = app

    def count_progect(self):
        wd = self.app.wd
        return len(wd.find_elements_by_css_selector("td.center"))

    def open_manage_projects_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage Projects").click()

    def random_string(prefix):
        symbol = string.ascii_letters + string.digits
        return random.choice(symbol)

    def add_progect(self):
        wd = self.app.wd
        wd.find_element_by_name("name").send_keys(self.random_string())
        wd.find_element_by_xpath("//input[@value='Add Category']").click()
        time.sleep(1)

    def del_progect(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.find_element_by_xpath("//input[@value='Delete Category']").click()
        time.sleep(6)


