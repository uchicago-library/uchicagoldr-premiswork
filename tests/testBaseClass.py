import unittest
import xml.etree.ElementTree as ET
import xml.dom.minidom

from pypremis.lib import PremisNode

class TestPremisNode(unittest.TestCase):
    def testMint(self):
        a = PremisNode('a')

    def testAllStrings(self):
        a = PremisNode('testRoot')
        a._set_field('tag1', '1')
        a._set_field('tag2', '2')
        a._set_field('tag3', '3')

        rough_str = ET.tostring(a.toXML())
        parsed = xml.dom.minidom.parseString(rough_str)
        print(parsed.toprettyxml())

    def testLists(self):
        a = PremisNode('testRoot')
        a._set_field('tag',['value1','value2','value3'])

        rough_str = ET.tostring(a.toXML())
        parsed = xml.dom.minidom.parseString(rough_str)
        print(parsed.toprettyxml())

    def testNested(self):
        a = PremisNode('testRoot')
        a._set_field('tag',['value1','value2','value3'])

        b = PremisNode('testNested')
        b._set_field('nestedtag',['nested1','nested2','nested3'])
        b._set_field('nesetdtag2','nestedvalue')

        a._set_field('nest',b)

        rough_str = ET.tostring(a.toXML())
        parsed = xml.dom.minidom.parseString(rough_str)
        print(parsed.toprettyxml())

    def testNestedList(self):
        a = PremisNode('testRoot')

        b = PremisNode('b')
        b._set_field('value','1')
        b._set_field('this','that')

        c = PremisNode('c')
        c._set_field('value','2')
        c._set_field('good','dog')

        a._set_field('nestedList',[b.toXML(), c.toXML()])

        rough_str = ET.tostring(a.toXML())
        parsed = xml.dom.minidom.parseString(rough_str)
        print(parsed.toprettyxml())



if __name__ == '__main__':
    unittest.main()
