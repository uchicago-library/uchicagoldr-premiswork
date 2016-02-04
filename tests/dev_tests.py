import unittest
import xml.etree.ElementTree as ET
import xml.dom.minidom

from pypremis.premisrecord import *

class Test(unittest.TestCase):
    def testObject(self):
        format = Format()
        objectCharacteristics = ObjectCharacteristics(format)
        identifier = ObjectIdentifier('number','1')
        second_id = ObjectIdentifier('letter','a')
        print()
        print(second_id._get_fields())
        print(second_id.get_objectIdentifierValue())
        print(second_id.get_objectIdentifierType())
        test = Object(identifier, 'test_category', objectCharacteristics)
        test.add_objectIdentifier(second_id.toXML())

        rough_str = ET.tostring(test.toXML())
        parsed = xml.dom.minidom.parseString(rough_str)
        print(parsed.toprettyxml())


if __name__ == '__main__':
    unittest.main()
