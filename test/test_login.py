


def test_login_mantis(app):
    app.session.login("administrator", "root")
    assert app.session.is_logged_in_as("administrator")