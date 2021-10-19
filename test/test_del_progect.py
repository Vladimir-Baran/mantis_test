import random
import string
from model.progect import Progect

username = "administrator"
password = "root"

def random_string(prefix, maxlen):
    symbols = string.ascii_letters+string.digits + string.punctuation + " "*10
    return prefix + "".join((random.choice(symbols) for i in range(random.randrange(maxlen))))


def test_del_progect(app):
    app.progect.open_manage_projects_page()
    if len(app.progect.get_project_list()) == 0:
        app.progect.add_progect(Progect(name=random_string("qws", 10)))
    old_list_progect = app.soap.get_project_list_soup(username, password)
    progect = random.choice(old_list_progect)
    app.progect.del_progect(progect.id)
    new_list_progect = app.soap.get_project_list_soup(username, password)
    assert len(old_list_progect) - 1 == len(new_list_progect)
    old_list_progect.remove(progect)
    assert sorted(old_list_progect, key=Progect.id_or_max) == sorted(new_list_progect, key=Progect.id_or_max)

