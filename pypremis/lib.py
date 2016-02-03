import xml.etree.ElementTree as ET


class PremisNode(object):
    def __init__(self, nodeName):
        self.fields = {}
        self.name = nodeName

    def toXML(self):
        root = ET.Element(self.name)
        for key in self.fields:
            newNodes = []
            value = self.fields[key]
            if isinstance(value, str):
                newNode = ET.Element(key)
                newNode.text = value
                newNodes.append(newNode)
            elif isinstance(value, list):
                for entry in list:
                    newNode = ET.Element(key)
                    if isinstance(entry, str):
                        newNode.text = entry
                    elif isinstance(entry, ET.Element):
                        newNode.append(entry)
                    else:
                        raise ValueError
                    newNodes.append(newNode)
            elif isinstance(value, PremisNode):
                newNode = value.toXML()
                newNodes.append(newNode)
            else:
                raise ValueError
            for entry in newNodes:
                root.append(entry)
        return root

    def set_field(self, key, value):
        self.fields[key] = value

    def get_field(self, key):
        return self.fields[key]

    def add_to_field(self, key, value):
        if not isinstance(value, list):
            raise KeyError
        self.fields[key].append(value)
