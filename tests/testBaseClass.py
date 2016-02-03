import unittest
import xml.etree.ElementTree as ET
import xml.dom.minidom

from pypremis.lib import PremisNode

class TestPremisNode(unittest.TestCase):
    def testMint(self):
        a = PremisNode('a')

    def testAllStrings(self):
        a = PremisNode('testRoot')
        a.set_field('tag1', '1')
        a.set_field('tag2', '2')
        a.set_field('tag3', '3')

        rough_str = ET.tostring(a.toXML())
        parsed = xml.dom.minidom.parseString(rough_str)
        print(parsed.toprettyxml())

    def testLists(self):
        a = PremisNode('testRoot')
        a.set_field('tag',['value1','value2','value3'])

        rough_str = ET.tostring(a.toXML())
        parsed = xml.dom.minidom.parseString(rough_str)
        print(parsed.toprettyxml())

    def testNested(self):
        a = PremisNode('testRoot')
        a.set_field('tag',['value1','value2','value3'])

        b = PremisNode('testNested')
        b.set_field('nestedtag',['nested1','nested2','nested3'])
        b.set_field('nesetdtag2','nestedvalue')

        a.set_field('nest',b)

        rough_str = ET.tostring(a.toXML())
        parsed = xml.dom.minidom.parseString(rough_str)
        print(parsed.toprettyxml())

    def testNestedList(self):
        a = PremisNode('testRoot')

        b = PremisNode('b')
        b.set_field('value','1')
        b.set_field('this','that')

        c = PremisNode('c')
        c.set_field('value','2')
        c.set_field('good','dog')

        a.set_field('nestedList',[b.toXML(), c.toXML()])

        rough_str = ET.tostring(a.toXML())
        parsed = xml.dom.minidom.parseString(rough_str)
        print(parsed.toprettyxml())



if __name__ == '__main__':
    unittest.main()
