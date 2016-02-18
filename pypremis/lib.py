import xml.etree.ElementTree as ET

from pypremis.factories import XMLNodeFactory 
from pypremis.nodes import *


class PremisRecord(object):
    def __init__(self,
                 objects=None, events=None, agents=None, rights=None,
                 frompath=None):

        if (frompath and (objects or events or agents or rights)):
            raise ValueError("Must supply either a valid file or at least "
                             "one array of valid PREMIS objects.")

        self.events_list = []
        self.objects_list = []
        self.agents_list = []
        self.rights_list = []
        self.filepath = None

        if frompath:
            self.filepath = frompath
            self.populate_from_file(XMLNodeFactory)
        else:
            if objects:
                for x in objects:
                    self.add_object(x)
            if events:
                for x in events:
                    self.add_event(x)
            if agents:
                for x in agents:
                    self.add_agent(x)
            if rights:
                for x in rights:
                    self.add_rights(x)

    def __iter__(self):
        for x in self.get_object_list() + self.get_event_list() + \
                self.get_rights_list() + self.get_agent_list():
            yield x

    def __eq__(self, other):
        if not isinstance(other, PremisRecord):
            return False
        for x in self:
            if x not in other:
                return False
        for x in other:
            if x not in self:
                return False
        return True

    def add_event(self, event):
        self.events_list.append(event)

    def get_event(self, eventID):
        pass

    def get_event_list(self):
        return self.events_list

    def add_object(self, obj):
        self.objects_list.append(obj)

    def get_object(self, objID):
        pass

    def get_object_list(self):
        return self.objects_list

    def add_agent(self, agent):
        self.agents_list.append(agent)

    def get_agent(self, agentID):
        pass

    def get_agent_list(self):
        return self.agents_list

    def add_rights(self, rights):
        self.rights_list.append(rights)

    def get_rights(self, rightsID):
        pass

    def get_rights_list(self):
        return self.rights_list

    def set_filepath(self, filepath):
        self.filepath = filepath

    def get_filepath(self):
        return self.filepath

    def validate(self):
        pass

    def populate_from_file(self, factory, filepath=None):
        if filepath is None:
            filepath = self.get_filepath()
        factory = factory(filepath)
        for event in factory.find_events():
            self.add_event(event)
        for agent in factory.find_agents():
            self.add_agent(agent)
        for rights in factory.find_rights():
            self.add_rights(rights)
        for obj in factory.find_objects():
            self.add_object(obj)


    def write_to_file(self, targetpath):
        tree = ET.ElementTree(element=ET.Element('premis:premis'))
        root = tree.getroot()
        root.set('xmlns:premis',"http://www.loc.gov/premis/v3")
        root.set('xmlns:xsi', "http://www.w3.org/2001/XMLSchema-instance")
        root.set('version',"3.0")
        for entry in self:
            root.append(entry.toXML())
        tree.write(targetpath, xml_declaration = True, encoding = 'utf-8', method = 'xml')
