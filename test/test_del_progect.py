import random
import string
from model.progect import Progect

username = "administrator"
password = "root"

def test_del_progect(app):
    app.progect.open_manage_projects_page()
    if len(app.progect.get_project_list()) == 0:
        app.progect.add_progect()
    old_list_progect = app.soap.get_project_list(username, password)
    progect = random.choice(len(old_list_progect))
    app.progect.del_progect(progect.id)
    new_list_progect = app.soap.get_project_list(username, password)
    assert len(old_list_progect) - 1 == len(new_list_progect)
    old_list_progect.remote(progect)
    assert sorted(old_list_progect, key=Progect.id_or_max) == sorted(new_list_progect, key=Progect.id_or_max)


