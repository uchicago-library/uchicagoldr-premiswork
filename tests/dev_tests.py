import unittest
import xml.etree.ElementTree as ET
import xml.dom.minidom

from pypremis.premisrecord import *

class Test(unittest.TestCase):
#    def testObject(self):
#        format = Format()
#        objectCharacteristics = ObjectCharacteristics(format)
#        identifier = ObjectIdentifier('number','1')
#        second_id = ObjectIdentifier('letter','a')
#        print()
#        print(second_id._get_fields())
#        print(second_id.get_objectIdentifierValue())
#        print(second_id.get_objectIdentifierType())
#        test = Object(identifier, 'test_category', objectCharacteristics)
#        test.add_objectIdentifier(second_id.toXML())
#
#        rough_str = ET.tostring(test.toXML())
#        parsed = xml.dom.minidom.parseString(rough_str)
#        print(parsed.toprettyxml())

    def testObject(self):
        pass

    def testEvent(self):
        #Layer 2
        eventOutcomeDetail = EventOutcomeDetail()
        self.assertEqual(eventOutcomeDetail.get_name(), 'eventOutcomeDetail')

        eventOutcomeDetail.set_eventOutcomeDetailNote('event_outcome_detail_note')
        self.assertEqual(eventOutcomeDetail.get_eventOutcomeDetailNote(), 'event_outcome_detail_note')
        eventOutcomeDetail.set_eventOutcomeDetailExtension('event_outcome_detail_extension')
        self.assertEqual(eventOutcomeDetail.get_eventOutcomeDetailExtension(), ['event_outcome_detail_extension'])
        eventOutcomeDetail.add_eventOutcomeDetailExtension('event_outcome_detail_extension_2')
        self.assertEqual(eventOutcomeDetail.get_eventOutcomeDetailExtension(), ['event_outcome_detail_extension', 'event_outcome_detail_extension_2'])
        self.assertEqual(eventOutcomeDetail.get_eventOutcomeDetailExtension(1), 'event_outcome_detail_extension_2')
        eventOutcomeDetail_2 = EventOutcomeDetail()

        #Layer 1
        eventIdentifier = EventIdentifier('event_identifier_type', 'event_identifier_value')
        self.assertEqual(eventIdentifier.get_name(), 'eventIdentifier')

        self.assertEqual(eventIdentifier.get_eventIdentifierType(), 'event_identifier_type')
        self.assertEqual(eventIdentifier.get_eventIdentifierValue(), 'event_identifier_value')

        eventDetailInformation = EventDetailInformation()
        self.assertEqual(eventDetailInformation.get_name(), 'eventDetailInformation')

        eventDetailInformation.set_eventDetail('event_detail')
        self.assertEqual(eventDetailInformation.get_eventDetail(), 'event_detail')
        eventDetailInformation.set_eventDetailExtension('event_detail_extension')
        self.assertEqual(eventDetailInformation.get_eventDetailExtension(), ['event_detail_extension'])
        eventDetailInformation.add_eventDetailExtension('event_detail_extension_2')
        self.assertEqual(eventDetailInformation.get_eventDetailExtension(), ['event_detail_extension', 'event_detail_extension_2'])
        self.assertEqual(eventDetailInformation.get_eventDetailExtension(1), 'event_detail_extension_2')
        eventDetailInformation_2 = EventDetailInformation()

        eventOutcomeInformation = EventOutcomeInformation()
        self.assertEqual(eventOutcomeInformation.get_name(), 'eventOutcomeInformation')

        eventOutcomeInformation.set_eventOutcome('event_outcome')
        self.assertEqual(eventOutcomeInformation.get_eventOutcome(), 'event_outcome')
        eventOutcomeInformation.set_eventOutcomeDetail(eventOutcomeDetail)
        self.assertEqual(eventOutcomeInformation.get_eventOutcomeDetail(), [eventOutcomeDetail])
        eventOutcomeInformation.add_eventOutcomeDetail(eventOutcomeDetail_2)
        self.assertEqual(eventOutcomeInformation.get_eventOutcomeDetail(), [eventOutcomeDetail, eventOutcomeDetail_2])
        self.assertEqual(eventOutcomeInformation.get_eventOutcomeDetail(1), eventOutcomeDetail_2)
        eventOutcomeInformation_2 = EventOutcomeInformation()

        linkingAgentIdentifier = LinkingAgentIdentifier('linking_agent_identifier_type', 'linking_agent_identifier_value')
        self.assertEqual(linkingAgentIdentifier.get_name(), 'linkingAgentIdentifier')

        self.assertEqual(linkingAgentIdentifier.get_linkingAgentIdentifierType(), 'linking_agent_identifier_type')
        self.assertEqual(linkingAgentIdentifier.get_linkingAgentIdentifierValue(), 'linking_agent_identifier_value')
        linkingAgentIdentifier.set_linkingAgentRole('linking_agent_role')
        self.assertEqual(linkingAgentIdentifier.get_linkingAgentRole(), ['linking_agent_role'])
        linkingAgentIdentifier.add_linkingAgentRole('linking_agent_role_2')
        self.assertEqual(linkingAgentIdentifier.get_linkingAgentRole(), ['linking_agent_role', 'linking_agent_role_2'])
        self.assertEqual(linkingAgentIdentifier.get_linkingAgentRole(1), 'linking_agent_role_2')
        linkingAgentIdentifier_2 = LinkingAgentIdentifier('linking_agent_identifier_type_2', 'linking_agent_identifier_value_2')

        linkingObjectIdentifier = LinkingObjectIdentifier('linking_object_identifier_type', 'linking_object_identifier_value')
        self.assertEqual(linkingObjectIdentifier.get_name(), 'linkingObjectIdentifier')

        self.assertEqual(linkingObjectIdentifier.get_linkingObjectIdentifierType(), 'linking_object_identifier_type')
        self.assertEqual(linkingObjectIdentifier.get_linkingObjectIdentifierValue(), 'linking_object_identifier_value')
        linkingObjectIdentifier.set_linkingObjectRole('linking_object_role')
        self.assertEqual(linkingObjectIdentifier.get_linkingObjectRole(), ['linking_object_role'])
        linkingObjectIdentifier.add_linkingObjectRole('linking_object_role_2')
        self.assertEqual(linkingObjectIdentifier.get_linkingObjectRole(), ['linking_object_role', 'linking_object_role_2'])
        self.assertEqual(linkingObjectIdentifier.get_linkingObjectRole(1), 'linking_object_role_2')
        linkingObjectIdentifier_2 = LinkingObjectIdentifier('linking_object_identifier_type_2', 'linking_object_identifier_value_2')

        #Layer 0
        event = Event('event_type', eventIdentifier, 'event_date_time')
        self.assertEqual(event.get_name(), 'event')

        event.set_eventIdentifier(eventIdentifier)
        self.assertEqual(event.get_eventIdentifier(), eventIdentifier)
        self.assertEqual(event.get_eventType(), 'event_type')
        self.assertEqual(event.get_eventDateTime(), 'event_date_time')
        event.set_eventDetailInformation(eventDetailInformation)
        self.assertEqual(event.get_eventDetailInformation(), [eventDetailInformation])
        event.add_eventDetailInformation(eventDetailInformation_2)
        self.assertEqual(event.get_eventDetailInformation(), [eventDetailInformation, eventDetailInformation_2])
        self.assertEqual(event.get_eventDetailInformation(1), eventDetailInformation_2)
        event.set_eventOutcomeInformation(eventOutcomeInformation)
        self.assertEqual(event.get_eventOutcomeInformation(), [eventOutcomeInformation])
        event.add_eventOutcomeInformation(eventOutcomeInformation_2)
        self.assertEqual(event.get_eventOutcomeInformation(), [eventOutcomeInformation, eventOutcomeInformation_2])
        self.assertEqual(event.get_eventOutcomeInformation(1), eventOutcomeInformation_2)
        event.set_linkingAgentIdentifier(linkingAgentIdentifier)
        self.assertEqual(event.get_linkingAgentIdentifier(), [linkingAgentIdentifier])
        event.add_linkingAgentIdentifier(linkingAgentIdentifier_2)
        self.assertEqual(event.get_linkingAgentIdentifier(), [linkingAgentIdentifier, linkingAgentIdentifier_2])
        self.assertEqual(event.get_linkingAgentIdentifier(1), linkingAgentIdentifier_2)
        event.set_linkingObjectIdentifier(linkingObjectIdentifier)
        self.assertEqual(event.get_linkingObjectIdentifier(), [linkingObjectIdentifier])
        event.add_linkingObjectIdentifier(linkingObjectIdentifier_2)
        self.assertEqual(event.get_linkingObjectIdentifier(), [linkingObjectIdentifier, linkingObjectIdentifier_2])
        self.assertEqual(event.get_linkingObjectIdentifier(1), linkingObjectIdentifier_2)




    def testAgent(self):
        # Layer 1
        agentIdentifier = AgentIdentifier('agent_identifier_type', 'agent_identifier_value')
        self.assertEqual(agentIdentifier.get_name(), 'agentIdentifier')

        self.assertEqual(agentIdentifier.get_agentIdentifierType(), 'agent_identifier_type')
        self.assertEqual(agentIdentifier.get_agentIdentifierValue(), 'agent_identifier_value')
        agentIdentifier_2 = AgentIdentifier('agent_identifier_type_2', 'agent_identifier_value_2')

        linkingEventIdentifier = LinkingEventIdentifier('linking_event_identifier_type', 'linking_event_identifier_value')
        self.assertEqual(linkingEventIdentifier.get_name(), 'linkingEventIdentifier')

        self.assertEqual(linkingEventIdentifier.get_linkingEventIdentifierType(), 'linking_event_identifier_type')
        self.assertEqual(linkingEventIdentifier.get_linkingEventIdentifierValue(), 'linking_event_identifier_value')
        linkingEventIdentifier_2 = LinkingEventIdentifier('linking_event_identifier_type_2', 'linking_event_identifier_value_2')

        linkingRightsStatementIdentifier = LinkingRightsStatementIdentifier('linking_rights_statement_identifier_type', 'linking_rights_statement_identifier_value')
        self.assertEqual(linkingRightsStatementIdentifier.get_name(), 'linkingRightsStatementIdentifier')

        self.assertEqual(linkingRightsStatementIdentifier.get_linkingRightsStatementIdentifierType(), 'linking_rights_statement_identifier_type')
        self.assertEqual(linkingRightsStatementIdentifier.get_linkingRightsStatementIdentifierValue(), 'linking_rights_statement_identifier_value')
        linkingRightsStatementIdentifier_2 = LinkingRightsStatementIdentifier('linking_rights_statement_identifier_type_2', 'linking_rights_statement_identifier_value_2')

        linkingEnvironmentIdentifier = LinkingEnvironmentIdentifier('linking_environment_identifier_type', 'linking_environment_identifier_value')
        self.assertEqual(linkingEnvironmentIdentifier.get_name(), 'linkingEnvironmentIdentifier')

        self.assertEqual(linkingEnvironmentIdentifier.get_linkingEnvironmentIdentifierType(), 'linking_environment_identifier_type')
        self.assertEqual(linkingEnvironmentIdentifier.get_linkingEnvironmentIdentifierValue(), 'linking_environment_identifier_value')
        linkingEnvironmentIdentifier.set_linkingEnvironmentRole('linking_environment_role_1')
        self.assertEqual(linkingEnvironmentIdentifier.get_linkingEnvironmentRole(), ['linking_environment_role_1'])
        linkingEnvironmentIdentifier.add_linkingEnvironmentRole('linking_environment_role_2')
        self.assertEqual(linkingEnvironmentIdentifier.get_linkingEnvironmentRole(), ['linking_environment_role_1', 'linking_environment_role_2'])
        self.assertEqual(linkingEnvironmentIdentifier.get_linkingEnvironmentRole(1), 'linking_environment_role_2')
        linkingEnvironmentIdentifier_2 = LinkingEnvironmentIdentifier('linking_environment_identifier_type_2', 'linking_environment_identifier_value_2')

        #Layer 0
        agent = Agent(agentIdentifier)
        self.assertEqual(agent.get_name(), 'agent')

        self.assertEqual(agent.get_agentIdentifier(), [agentIdentifier])
        agent.add_agentIdentifier(agentIdentifier_2)
        self.assertEqual(agent.get_agentIdentifier(), [agentIdentifier, agentIdentifier_2])
        self.assertEqual(agent.get_agentIdentifier(1), agentIdentifier_2)

        agent.set_agentName('agent_name')
        self.assertEqual(agent.get_agentName(), ['agent_name'])
        agent.add_agentName('agent_name_2')
        self.assertEqual(agent.get_agentName(), ['agent_name', 'agent_name_2'])
        self.assertEqual(agent.get_agentName(1), 'agent_name_2')

        agent.set_agentType('agent_type')
        self.assertEqual(agent.get_agentType(),'agent_type')

        agent.set_agentVersion('agent_version')
        self.assertEqual(agent.get_agentVersion(), 'agent_version')

        agent.set_agentNote('agent_note')
        self.assertEqual(agent.get_agentNote(), ['agent_note'])
        agent.add_agentNote('agent_note_2')
        self.assertEqual(agent.get_agentNote(), ['agent_note', 'agent_note_2'])
        self.assertEqual(agent.get_agentNote(1), 'agent_note_2')

        agent.set_agentExtension('agent_extension')
        self.assertEqual(agent.get_agentExtension(), ['agent_extension'])
        agent.add_agentExtension('agent_extension_2')
        self.assertEqual(agent.get_agentExtension(), ['agent_extension', 'agent_extension_2'])
        self.assertEqual(agent.get_agentExtension(1), 'agent_extension_2')

        agent.set_linkingEventIdentifier(linkingEventIdentifier)
        self.assertEqual(agent.get_linkingEventIdentifier(), [linkingEventIdentifier])
        agent.add_linkingEventIdentifier(linkingEventIdentifier_2)
        self.assertEqual(agent.get_linkingEventIdentifier(), [linkingEventIdentifier, linkingEventIdentifier_2])
        self.assertEqual(agent.get_linkingEventIdentifier(1), linkingEventIdentifier_2)

        agent.set_linkingRightsStatementIdentifier(linkingRightsStatementIdentifier)
        self.assertEqual(agent.get_linkingRightsStatementIdentifier(), [linkingRightsStatementIdentifier])
        agent.add_linkingRightsStatementIdentifier(linkingRightsStatementIdentifier_2)
        self.assertEqual(agent.get_linkingRightsStatementIdentifier(), [linkingRightsStatementIdentifier, linkingRightsStatementIdentifier_2])
        self.assertEqual(agent.get_linkingRightsStatementIdentifier(1), linkingRightsStatementIdentifier_2)

        agent.set_linkingEnvironmentIdentifier(linkingEnvironmentIdentifier)
        self.assertEqual(agent.get_linkingEnvironmentIdentifier(), [linkingEnvironmentIdentifier])
        agent.add_linkingEnvironmentIdentifier(linkingEnvironmentIdentifier_2)
        self.assertEqual(agent.get_linkingEnvironmentIdentifier(), [linkingEnvironmentIdentifier, linkingEnvironmentIdentifier_2])
        self.assertEqual(agent.get_linkingEnvironmentIdentifier(1), linkingEnvironmentIdentifier_2)

    def testRights(self):
        pass


if __name__ == '__main__':
    unittest.main()
