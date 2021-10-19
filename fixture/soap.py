from suds.client import Client
from suds import WebFault
from model.progect import Progect

class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client("http://localhost:8080/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_project_list(self, username, password):
        client = Client("http://localhost:8080/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        try:
            user_accessible = client.service.mc_projects_get_user_accessible(username, password)
            projects_soap_list = []
            for project in user_accessible:
                name = project["name"]
                id = project["id"]
                projects_soap_list.append(Progect(name=name, id=int(id)))
            return projects_soap_list
        except WebFault:
            return False