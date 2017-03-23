from pypremis.factories import JSONNodeFactory
from pypremis.lib import PremisRecord
from pypremis.nodes import *
from json import load
from json import dump, dumps

# Minimal record
#objectIdentifier1 = ObjectIdentifier("type1", "value1")
#objectIdentifier2 = ObjectIdentifier("type2", "value2")
#formatDesignation1 = FormatDesignation("format_name1")
#format1 = Format(formatDesignation1)
#objectCharacteristics1 = ObjectCharacteristics(format1)
#obj = Object([objectIdentifier1, objectIdentifier2], "file", objectCharacteristics1)
#object_rec = PremisRecord(objects=[obj])

object_rec = PremisRecord.from_xml_file("testobject1.xml")
object_rec2 = PremisRecord.from_dict(object_rec.to_json())
print(object_rec.to_json() == object_rec2.to_json())
object_rec2.write_to_file("comp_object1.xml")

event_rec = PremisRecord.from_xml_file("testevent1.xml")
event_rec2 = PremisRecord.from_dict(event_rec.to_json())
print(event_rec.to_json() == event_rec2.to_json())

agent_rec = PremisRecord.from_xml_file("testagent1.xml")
agent_rec2 = PremisRecord.from_dict(agent_rec.to_json())
print(agent_rec.to_json() == agent_rec2.to_json())

rights_rec = PremisRecord.from_xml_file("testrights1.xml")
rights_rec2 = PremisRecord.from_dict(rights_rec.to_json())
print(rights_rec.to_json() == rights_rec2.to_json())

