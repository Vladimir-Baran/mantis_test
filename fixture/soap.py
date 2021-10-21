from suds.client import Client
from suds import WebFault
from model.progect import Progect

class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client(self.app.base_url + "api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_project_list_soup(self):
        client = Client(self.app.base_url + "api/soap/mantisconnect.php?wsdl")
        try:
            user_accessible = client.service.mc_projects_get_user_accessible(self.app.config['webadmin']['username'],
                                                                             self.app.config['webadmin']['password'])
            projects_soap_list = []
            for project in user_accessible:
                name = project["name"]
                id = project["id"]
                projects_soap_list.append(Progect(name=name, id=int(id)))
            return projects_soap_list
        except WebFault:
            return False