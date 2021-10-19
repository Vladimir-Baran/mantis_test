import random
import string


def test_del_progect(app):
    app.progect.open_manage_projects_page()
    if int(app.progect.count_progect()) == 2:
        app.progect.add_progect()
    old_list_progect = app.progect.get_progect_list()
    app.progect.del_progect()
    new_list_progect = app.progect.get_progect_list()
    assert len(old_list_progect) - 1 == len(new_list_progect)
    old_list_progect[0:1] = []
    assert old_list_progect == new_list_progect


