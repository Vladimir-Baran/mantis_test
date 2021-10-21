from model.progect import Progect
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters+string.digits + string.punctuation + " "*10
    return prefix + "".join((random.choice(symbols) for i in range(random.randrange(maxlen))))


def test_add_project(app):
    old_list_progect = app.soap.get_project_list_soup()
    app.progect.open_manage_projects_page()
    random_name = Progect(name=random_string("asr", 10))
    app.progect.add_progect(random_name)
    new_list_progect = app.soap.get_project_list_soup()
    assert len(old_list_progect) +1 == len(new_list_progect)
    old_list_progect.append(random_name)
    assert sorted(old_list_progect, key=Progect.id_or_max) == sorted(new_list_progect, key=Progect.id_or_max)