from model.progect import Progect

def test_add_project(app):
    app.progect.open_manage_projects_page()
    random_name = app.progect.random_name()
    old_count_progect = app.progect.count_progect()
    old_list_progect = app.progect.get_progect_list()
    app.progect.add_progect(random_name)
    new_count_progect = app.progect.count_progect()
    new_list_progect = app.progect.get_progect_list()
    assert old_count_progect +1 == new_count_progect
    old_list_progect.append(str(random_name))
    assert sorted(old_list_progect) == sorted(new_list_progect)