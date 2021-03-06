import time
import string
import random
from model.progect import Progect

class ProgectHelper:

    def __init__(self, app):
        self.app = app

    def count_progect(self):
        wd = self.app.wd
        return len(wd.find_elements_by_css_selector("td.center"))

    def get_project_list(self):
        wd = self.app.wd
        self.open_manage_projects_page()
        self.project = []
        for element in wd.find_elements_by_xpath("//td/a[contains(@href,'manage_proj_edit_page.php?project_id=')]"):
            text = element.text
            id = element.get_attribute("href").replace(self.app.base_url +'manage_proj_edit_page.php?project_id=', '')
            self.project.append(Progect(name=text, id=id))
        return self.project

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

    def add_progect(self, random_name):
        wd = self.app.wd
        self.open_manage_projects_page()
        wd.find_element_by_css_selector("input[value='Create New Project']").click()
        self.fill_project_form(random_name)
        wd.find_element_by_css_selector("input[value='Add Project']").click()
        time.sleep(3)

    def fill_project_form(self, project):
        wd = self.app.wd
        self.change_field_value("name", project.name)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def del_progect(self, id):
        wd = self.app.wd
        self.open_manage_projects_page()
        self.select_progect_by_id(id)
        time.sleep(1)
        wd.find_element_by_css_selector("input[value='Delete Project']").click()
        wd.find_element_by_css_selector("input[value='Delete Project']").click()
        time.sleep(6)

    def select_progect_by_id(self, id):
        wd = self.app.wd
        wd.get(self.app.base_url + "manage_proj_edit_page.php?project_id=" + str(id))


