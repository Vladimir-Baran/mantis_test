from model.progect import Progect
import random
import string

username = "administrator"
password = "root"


def test_add_project(app):
    old_list_progect = app.soap.get_project_list(username, password)
    app.progect.open_manage_projects_page()
    random_name = app.progect.random_name()
    app.progect.add_progect(random_name)
    new_list_progect = app.soap.get_project_list(username, password)
    assert len(old_list_progect) +1 == len(new_list_progect)
    old_list_progect.append(str(random_name))
    assert sorted(old_list_progect, key=Progect.id_or_max) == sorted(new_list_progect, key=Progect.id_or_max)