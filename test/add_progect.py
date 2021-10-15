

def test_add_project(app):
    app.session.login("administrator", "root")
    app.progect.open_manage_projects_page()
    old_count_progect = app.progect.count_progect()
    app.progect.add_progect()
    new_count_progect = app.progect.count_progect()
    assert old_count_progect +1 == new_count_progect