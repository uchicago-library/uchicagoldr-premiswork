from pypremis.factories import JSONNodeFactory
from pypremis.lib import PremisRecord
from pypremis.nodes import *
from json import load
from json import dump, dumps

objectIdentifier1 = ObjectIdentifier("type1", "value1")
objectIdentifier2 = ObjectIdentifier("type2", "value2")
formatDesignation1 = FormatDesignation("format_name1")
format1 = Format(formatDesignation1)
objectCharacteristics1 = ObjectCharacteristics(format1)
obj = Object([objectIdentifier1, objectIdentifier2], "file", objectCharacteristics1)
object_rec = PremisRecord(objects=[obj])

#object_rec = PremisRecord.from_xml_file("pretty_testobject1.xml")
with open("1.testing", 'w') as f:
    dump(object_rec.to_json(), f, indent=4)
with open("2.testing", 'w') as f:
    dump(object_rec.to_json(), f, indent=4)
object_rec2 = PremisRecord.from_json_file("1.testing")
print(dumps(object_rec.objects_list[0].toJSON(), indent=2))
print(dumps(object_rec2.objects_list[0].toJSON(), indent=2))
with open("3.testing", 'w') as f:
    dump(object_rec2.to_json(), f, indent=4)



#object_j = object_rec.to_json()
#object_fac = JSONNodeFactory(object_j)
#object_output = object_fac.find_objects()
#j1 = object_rec.to_json()
#object_rec2 = PremisRecord.from_dict(j1)
#object_rec3 = PremisRecord.from_dict(j1)
#print(object_rec == object_rec2)
#with open("1.testing", 'w') as f:
#    dump(object_rec.to_json(), f, indent=4)
#with open("1.testing") as f:
#    print(load(f) == object_rec.to_json())

#event_rec = PremisRecord.from_xml_file("testevent1.xml")
#event_j = event_rec.to_json()
#event_fac = JSONNodeFactory(event_j)
#event_output = event_fac.find_events()
#with open("testevent1.json", 'w') as f:
#    dump(PremisRecord(events=event_output).to_json(), f, indent=4)
#
#agent_rec = PremisRecord.from_xml_file("testagent1.xml")
#agent_j = agent_rec.to_json()
#agent_fac = JSONNodeFactory(agent_j)
#agent_output = agent_fac.find_agents()
#with open("testagent1.json", 'w') as f:
#    dump(PremisRecord(agents=agent_output).to_json(), f, indent=4)
#
#rights_rec = PremisRecord.from_xml_file("testrights1.xml")
#rights_j = rights_rec.to_json()
#rights_fac = JSONNodeFactory(rights_j)
#rights_output = rights_fac.find_rights()
#with open("testrights1.json", 'w') as f:
#    dump(PremisRecord(rights=rights_output).to_json(), f, indent=4)
