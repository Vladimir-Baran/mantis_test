import time
import string
import random
from model.progect import Progect
import itertools

class ProgectHelper:

    def __init__(self, app):
        self.app = app

    def count_progect(self):
        wd = self.app.wd
        return len(wd.find_elements_by_css_selector("td.center"))

    def get_progect_list_tr1(self):
        wd = self.app.wd
        self.open_manage_projects_page()
        tr = wd.find_elements_by_css_selector("tr.row-1")
        list_progect_1 = []
        for element in tr:
            cells = element.find_elements_by_tag_name("td")
            name = cells[0].text
            list_progect_1.append(name)
        return list_progect_1

    def get_progect_list_tr2(self):
        wd = self.app.wd
        self.open_manage_projects_page()
        tr = wd.find_elements_by_css_selector("tr.row-2")
        list_progect_2 = []
        for element in tr:
            cells = element.find_elements_by_tag_name("td")
            name = cells[0].text
            list_progect_2.append(name)
        return list_progect_2

    def get_progect_list(self):
        wd = self.app.wd
        return "\n".join(map(str, itertools.chain.from_iterable(zip(self.get_progect_list_tr1(), self.get_progect_list_tr2()))))

    def open_manage_projects_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()

    def random_string(self, prefix, maxlen):
        symbol = string.ascii_letters + string.digits
        return prefix + "".join([random.choice(symbol) for i in range(random.randrange(maxlen))])

    def random_name(self):
        wd = self.app.wd
        rand = self.random_string("asd", 10)
        return rand

    def add_progect(self, ):
        wd = self.app.wd
        wd.find_element_by_name("name").send_keys(self.random_name())
        wd.find_element_by_xpath("//input[@value='Add Category']").click()
        time.sleep(1)

    def del_progect(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.find_element_by_xpath("//input[@value='Delete Category']").click()
        time.sleep(6)

    def get_progect_row_1(self):
        wd = self.app.wd
        self.open_manage_projects_page()
        entry =wd.find_elements_by_name("row-1")

