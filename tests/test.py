from pypremis.factories import JSONNodeFactory
from pypremis.lib import PremisRecord
from json import load
from json import dump


object_rec = PremisRecord(frompath="testobject1.xml")
object_j = object_rec.to_json()
object_fac = JSONNodeFactory(object_j)
object_output = object_fac.find_objects()
with open("testobject1.json", 'w') as f:
    dump(PremisRecord(objects=object_output).to_json(), f, indent=4)
with open("testobject1.json") as f:
    new = load(f)

with open("1.txt", 'w') as f:
    f.write(str(JSONNodeFactory(new).find_objects()))
with open("2.txt", 'w') as f:
    f.write(str((object_rec.objects_list)))


event_rec = PremisRecord(frompath="testevent1.xml")
event_j = event_rec.to_json()
event_fac = JSONNodeFactory(event_j)
event_output = event_fac.find_events()
with open("testevent1.json", 'w') as f:
    dump(PremisRecord(events=event_output).to_json(), f, indent=4)

agent_rec = PremisRecord(frompath="testagent1.xml")
agent_j = agent_rec.to_json()
agent_fac = JSONNodeFactory(agent_j)
agent_output = agent_fac.find_agents()
with open("testagent1.json", 'w') as f:
    dump(PremisRecord(agents=agent_output).to_json(), f, indent=4)

rights_rec = PremisRecord(frompath="testrights1.xml")
rights_j = rights_rec.to_json()
rights_fac = JSONNodeFactory(rights_j)
rights_output = rights_fac.find_rights()
with open("testrights1.json", 'w') as f:
    dump(PremisRecord(rights=rights_output).to_json(), f, indent=4)
