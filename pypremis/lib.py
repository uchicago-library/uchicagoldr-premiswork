import xml.etree.ElementTree as ET
from pypremis.factories import XMLNodeFactory
from pypremis.nodes import *


"""
### Classes for general use in pypremis ###

1. **PremisRecord** is a containing class meant to hold a list of sorted nodes
and facilitate writing them to reading and writing serializations.
"""


class PremisRecord(object):
    """
    A class for holding PremisNode objects. Facilitates reading and writing
    to disk

    __Attributes__

    1. objects_list is a list of instances of object nodes
    2. events_list is a list of instances of event nodes
    3. agents_list is a list of instances of agent nodes
    4. rights_list is a list of instances of rights nodes
    5. filepath is a string which correlates to the location on disk
    of a premis.xml file.
    """
    def __init__(self,
                 objects=None, events=None, agents=None, rights=None,
                 frompath=None):
        """
        Initializes a PremisRecord object from either a list of
        pre-existing nodes or an existing xml file on disk. Requires
        one or the other to be supplied on init.

        __KWArgs__

        * objects (list): a list to initially populate objects_list
        * events (list):  a list to initially populate events_list
        * agents (list):  a list to initially populate agents_list
        * rights (list):  a list to initially populate rights_list
        * frompath (list): a string meant to set the location of an originating
        xml file
        """

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
        """
        Yields each contained node.

        __Returns__

        * (generator): a generator of each node in the record
        """
        for x in self.get_object_list() + self.get_event_list() + \
                self.get_rights_list() + self.get_agent_list():
            yield x

    def __eq__(self, other):
        """
        Computes equality between two PremisRecord objects.

        __Args__

        1. other: an object to compute equality with.

        __Returns__

        * (bool): A boolean denoting equality
        """
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
        """
        Adds an event node to the event list.

        __Args__

        1. event (PremisNode): an Event PremisNode instance.
        """
        self.events_list.append(event)

    def get_event(self, eventID):
        """
        Returns the event node with the corresponding eventID.

        __Args__

        1. eventID (str): A string which corresponds to one of the
        eventIdentifierValue's specified in an Event PremisNode instance.

        __Returns__

        * (PremisNode or None): an event PremisNode, or None
        """
        pass

    def get_event_list(self):
        """
        Returns a list containing each associated event node.

        __Returns__

        * (list): the self.events_list attribute
        """
        return self.events_list

    def add_object(self, obj):
        """
        Adds an object node to the object list.

        __Args__

        1. obj (PremisNode): an Object PremisNode instance
        """
        self.objects_list.append(obj)

    def get_object(self, objID):
        """
        Returns the object node with the corresponding objectID

        __Args__

        1. objID (str): A string which corresponds with one of the
        objectIdentifierValue's specified in an Object PremisNode instance

        __Returns__

        * (PremisNode or None): an object PremisNode, or None
        """
        pass

    def get_object_list(self):
        """
        Returns a list containing each object node.

        __Returns__

        * (list): the self.objects_list attribute
        """
        return self.objects_list

    def add_agent(self, agent):
        """
        Adds an agent node to the agent list.

        __Args__

        1. agent (PremisNode): an Agent PremisNode instance
        """
        self.agents_list.append(agent)

    def get_agent(self, agentID):
        """
        Returns the agent node with the corresponding agentID.

        __Args__

        1. agentID (str): A string which corresponds with one of the
        agentIdentifierValue's specified in an Agent PremisNode instance

        __Returns__

        * (PremisNode or None): an event PremisNode, or None
        """
        pass

    def get_agent_list(self):
        """
        Returns a list containing each agent node.

        __Returns__

        * (list): the self.agents_list attribute
        """
        return self.agents_list

    def add_rights(self, rights):
        """
        Adds a rights node to the rights list.

        __Args__

        1. rights (PremisNode): a Rights PremisNode instance
        """
        self.rights_list.append(rights)

    def get_rights(self, rightsID):
        """
        Returns the rights node with the corresponding rightsID

        __Args__

        1. rightsID (str): A string which corresponds with one of the
        rightsIdentifierValue's specified in a Rights PremisNode instance.

        __Returns__

        * (PremisNode or None): a rights PremisNode, or None
        """
        pass

    def get_rights_list(self):
        """
        Returns a list containing each rights node.

        __Returns__

        * (list): the self.rights_list attribute
        """
        return self.rights_list

    def set_filepath(self, filepath):
        """
        Sets the filepath attribute.

        __Args__

        1. filepath (str): A string corresponding to a filepath on disk that specifies
        the location of a pre-existing premis xml record
        """
        self.filepath = filepath

    def get_filepath(self):
        """
        Returns the filepath attribute.

        __Returns__

        * (str): the self.filepath attribute
        """
        return self.filepath

    def validate(self):
        """
        Validates the contained record against the PREMIS specification.

        __Returns__

        * (bool): A bool denoting validity
        """
        pass

    def populate_from_file(self, factory, filepath=None):
        """
        Populates the object, event, agent, and rights lists from an existing
        premis xml file

        __Args__

        1. factory (cls): A factory class which implements .find_events(),
        .find_agents(), .find_rights, and .find_objects(), which return
        iterators consisting of Event, Agent, Rights, and Object PremisNode
        instances respectively.

        __KWArgs__

        * filepath (str): A string which specifies the location of a serialization
        supported by the given factory class. If not provided the instances
        filepath attribute is assumed.
        """
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
        # This fixes a weird bug where the premis xmlns was being written twice
        # in the attributes of the root tag when calling .write_to_file() in
        # cases where extension nodes contain children that are PremisNodes
        ET.register_namespace('premis', "")
        ET.register_namespace('xsi', "")

    def write_to_file(self, targetpath):
        """
        Writes the contained premis data structure out to disk as the
        specified path as an xml document.

        __Args__

        1. targetpath (str): a str corresponding to the intended location on disk
        to write the premis xml file to.
        """
        tree = ET.ElementTree(element=ET.Element('premis:premis'))
        root = tree.getroot()
        root.set('xmlns:premis', "http://www.loc.gov/premis/v3")
        root.set('xmlns:xsi', "http://www.w3.org/2001/XMLSchema-instance")
        root.set('version', "3.0")
        for entry in self:
            root.append(entry.toXML())
        tree.write(targetpath,
                   xml_declaration=True,
                   encoding='unicode',
                   method='xml')
