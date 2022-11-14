from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        content = toml.loads(content)
        name = content['tool']['poetry']['name']
        desc = content['tool']['poetry']['description']
        deps = content['tool']['poetry']['dependencies']
        depsDev = content['tool']['poetry']['dev-dependencies']

        return Project(name, desc, deps, depsDev)
