


def test_login_mantis(app):
    assert app.session.is_logged_in_as("administrator")