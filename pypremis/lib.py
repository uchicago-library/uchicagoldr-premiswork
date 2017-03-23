import xml.etree.ElementTree as ET
from pypremis.factories import XMLNodeFactory, JSONNodeFactory
from pypremis.nodes import *
from json import loads, load


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
    @classmethod
    def from_xml_file(cls, fp):
        with open(fp) as f:
            return cls.from_xml_stream(f)

    @classmethod
    def from_json_file(cls, fp):
        with open(fp) as f:
            return cls.from_json_stream(f)

    @classmethod
    def from_xml_str(cls, s):
        return cls.from_etree(ET.ElementTree(ET.fromstring(s)))

    @classmethod
    def from_json_str(cls, s):
        return cls.from_dict(loads(s))

    @classmethod
    def from_xml_stream(cls, s):
        return cls.from_etree(ET.parse(s))

    @classmethod
    def from_json_stream(cls, s):
        return cls.from_dict(load(s))

    @classmethod
    def from_dict(cls, d):
        fac = JSONNodeFactory(d)
        return PremisRecord(
            objects=fac.find_objects(),
            events=fac.find_events(),
            rights=fac.find_rights(),
            agents=fac.find_agents()
        )

    @classmethod
    def from_etree(cls, tree):
        fac = XMLNodeFactory(tree)
        return PremisRecord(
            objects=fac.find_objects(),
            events=fac.find_events(),
            rights=fac.find_rights(),
            agents=fac.find_agents()
        )

    def __init__(self, objects=None, events=None, agents=None, rights=None):
        """
        Initializes a PremisRecord object from either a list of
        pre-existing nodes or an existing xml file on disk. Requires
        one or the other to be supplied on init.

        __KWArgs__

        * objects (list): a list to initially populate objects_list
        * events (list):  a list to initially populate events_list
        * agents (list):  a list to initially populate agents_list
        * rights (list):  a list to initially populate rights_list
        """
        self._event_list = []
        self._object_list = []
        self._agent_list = []
        self._rights_list = []

        ET.register_namespace('premis', "")
        ET.register_namespace('xsi', "")
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
        if not isinstance(event, Event):
            raise ValueError()
        self._event_list.append(event)

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
        return self._event_list

    def set_event_list(self, l):
        del self.event_list
        for x in l:
            self.add_event(x)

    def del_event_list(self):
        self._event_list = []

    def add_object(self, obj):
        """
        Adds an object node to the object list.

        __Args__

        1. obj (PremisNode): an Object PremisNode instance
        """
        if not isinstance(obj, Object):
            raise ValueError()
        self._object_list.append(obj)

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
        return self._object_list

    def set_object_list(self, l):
        del self.object_list
        for x in l:
            self.add_object(x)

    def del_object_list(self):
        self._object_list = []

    def add_agent(self, agent):
        """
        Adds an agent node to the agent list.

        __Args__

        1. agent (PremisNode): an Agent PremisNode instance
        """
        if not isinstance(agent, Agent):
            raise ValueError()
        self._agent_list.append(agent)

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
        return self._agent_list

    def set_agent_list(self, l):
        del self.agent_list
        for x in l:
            self.add_agent(l)

    def del_agent_list(self):
        self._agent_list = []

    def add_rights(self, rights):
        """
        Adds a rights node to the rights list.

        __Args__

        1. rights (PremisNode): a Rights PremisNode instance
        """
        if not isinstance(rights, Rights):
            raise ValueError()
        self._rights_list.append(rights)

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
        return self._rights_list

    def set_rights_list(self, l):
        del self.rights_list
        for x in l:
            self.add_rights(x)

    def del_rights_list(self):
        self._rights_list = []

    def to_etree(self):
        tree = ET.ElementTree(element=ET.Element('premis:premis'))
        root = tree.getroot()
        root.set('xmlns:premis', "http://www.loc.gov/premis/v3")
        root.set('xmlns:xsi', "http://www.w3.org/2001/XMLSchema-instance")
        root.set('version', "3.0")
        for entry in self:
            root.append(entry.toXML())
        return tree

    def to_json(self):
        r = {}
        for x in self.get_object_list():
            if not r.get('object'):
                r['object'] = []
            r['object'].append(x.toJSON())
        for x in self.get_agent_list():
            if not r.get('agent'):
                r['agent'] = []
            r['agent'].append(x.toJSON())
        for x in self.get_rights_list():
            if not r.get('rights'):
                r['rights'] = []
            r['rights'].append(x.toJSON())
        for x in self.get_event_list():
            if not r.get('event'):
                r['event'] = []
            r['event'].append(x.toJSON())
        return r

    object_list = property(get_object_list, set_object_list, del_object_list)
    event_list = property(get_event_list, set_event_list, del_event_list)
    agent_list = property(get_agent_list, set_agent_list, del_agent_list)
    rights_list = property(get_rights_list, set_rights_list, del_rights_list)
