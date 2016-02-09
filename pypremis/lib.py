import xml.etree.ElementTree as ET


class PremisRecord(object):
    def __init__(self,
                 objs=None, events=None, agents=None, rights=None,
                 filepath=None):

        if not filepath and not (objs or events or agents or rights) or \
                filepath and (objs or events or agents or rights):
            raise ValueError("Must supply either a valid file or at least "
                             "one array of valid PREMIS objects.")

        self.events = []
        self.objects = []
        self.agents = []
        self.rights = []
        self.filepath = None

        if filepath:
            self.filepath = filepath
        else:
            pass


    def __iter__(self):
        for x in self.events + self.objects + self.entites + self.rights:
            return x

    def add_event(self, event):
        self.events.append(event)

    def get_event(self, eventID):
        pass

    def get_event_list(self):
        return self.events

    def add_object(self, obj):
        self.objects.append(obj)
        pass

    def get_object(self, objID):
        pass

    def get_object_list(self):
        return self.objects

    def add_agent(self, agent):
        self.agents.append(agent)
        pass

    def get_agent(self, agentID):
        pass

    def get_agent_list(self):
        return self.entities

    def add_rights(self, rights):
        self.rights.append(rights)

    def get_rights(self, rightsID):
        pass

    def get_rights_list(self):
        return self.rights

    def set_filepath(self, filepath):
        self.filepath = filepath

    def get_filepath(self):
        return self.filepath

    def validate(self):
        pass

    def populate_from_file(self):
        ET.register_namespace('premis', 'http://www.loc.gov/premis/v3')
        tree = ET.parse(self.filepath)
        root = tree.get_root()
        factory = NodeFactory(root)
        for event in factory.find_events():
            self.add_event(event)
        for agent in factory.find_agents():
            self.add_agent(agent)
        for rights in factory.find_rights():
            self.add_rights(rights)
        for obj in factory._find_objects():
            self.add_object(obj)


    def write_to_file(self, targetpath):
        ET.register_namespace('premis', 'http://www.loc.gov/premis/v3')
        tree = ET.ElementTree(element=self.root)
        for entry in self:
            root.append(entry.toXML())
        tree.write(targetpath)


class PremisNode(object):
    def __init__(self, nodeName):
        self._set_fields({})
        self._set_name(nodeName)

    def __repr__(self):
        return ET.tostring(self.toXML()).decode('utf-8')

    def __eq__(self, other):
        return isinstance(other, PremisNode) and \
            self.name == other.name and \
            self.fields == other.fields

    def toXML(self):
        root = ET.Element("premis:"+self.name)
        for key in self.fields:
            newNodes = []
            value = self.fields[key]
            if isinstance(value, str):
                newNode = ET.Element("premis:"+key)
                newNode.text = value
                newNodes.append(newNode)
            elif isinstance(value, list):
                for entry in value:
                    if isinstance(entry, PremisNode):
                        entry = entry.toXML()
                    if isinstance(entry, str):
                        newNode = ET.Element("premis:"+key)
                        newNode.text = entry
                        newNodes.append(newNode)
                    else:
                        raise ValueError
            elif isinstance(value, PremisNode):
                newNode = value.toXML()
                newNodes.append(newNode)
            else:
                raise ValueError
            for entry in newNodes:
                root.append(entry)
        return root

    def _set_fields(self, fields):
        if not isinstance(fields, dict):
            raise TypeError
        self.fields = fields

    def _get_fields(self):
        return self.fields

    def _set_name(self, name):
        if not isinstance(name, str):
            raise TypeError
        self.name = name

    def get_name(self):
        return self.name

    def _set_field(self, key, value):
        if not isinstance(key, str):
            raise TypeError
        valueType = (isinstance(value, str) or isinstance(value, PremisNode) or
                     isinstance(value, ET.Element) or isinstance(value, list))
        if not valueType:
            raise TypeError
        self.fields[key] = value

    def _get_field(self, key):
        return self.fields[key]

    def _add_to_field(self, key, value):
        if key not in self.fields:
            self.fields[key] = []
        if not isinstance(self.fields[key], list):
            raise KeyError
        valueType = (isinstance(value, str) or isinstance(value, PremisNode) or
                     isinstance(value, ET.Element) or isinstance(value, list))
        if not valueType:
            raise TypeError
        self.fields[key].append(value)

    def _get_from_field_by_index(self, key, index):
        return self.fields[key][index]

    def _listify(self, x):
        if not isinstance(x, list):
            return [x]
        else:
            return x

    def _list_getter(self, key, index):
        if index is None:
            return self.fields[key]
        else:
            return self.fields[key][index]

    def _type_check(self, x, type_it_should_be):
        if not isinstance(x, type_it_should_be):
            raise TypeError
