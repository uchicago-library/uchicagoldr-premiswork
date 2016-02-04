import xml.etree.ElementTree as ET


class PremisNode(object):
    def __init__(self, nodeName):
        self._set_fields({})
        self._set_name(nodeName)

    def __repr__(self):
        return ET.tostring(self.toXML())

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
                for entry in value:
                    if isinstance(entry, PremisNode):
                        entry = entry.toXML()
                    if isinstance(entry, str):
                        newNode = ET.Element(key)
                        newNode.text = entry
                        newNodes.append(newNode)
                    elif isinstance(entry, ET.Element):
                        newNodes.append(entry)
                    else:
                        raise ValueError
            elif isinstance(value, PremisNode):
                newNode = value.toXML()
                newNodes.append(newNode)
            elif isinstance(value, ET.Element):
                newNodes.append(value)
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

    def _get_name(self):
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
