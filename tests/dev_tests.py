import unittest
import xml.etree.ElementTree as ET
import xml.dom.minidom

from pypremis.premisrecord import *

class Test(unittest.TestCase):
    def testObject(self):
        identifier = ObjectIdentifier('number','1')
        test = PremisObject(identifier.toXML(), 'test_category')

        rough_str = ET.tostring(test.toXML())
        parsed = xml.dom.minidom.parseString(rough_str)
        print(parsed.toprettyxml())


if __name__ == '__main__':
    unittest.main()
