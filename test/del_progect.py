import random
import string


def test_del_progect(app):
    app.session.login("administrator", "root")
    app.progect.open_manage_projects_page()
    if int(app.progect.count_progect()) == 2:
        app.progect.add_progect()
    old_progect = app.progect.count_progect()
    app.progect.del_progect()
    new_progect = app.progect.count_progect()
    assert old_progect - 1 == new_progect


