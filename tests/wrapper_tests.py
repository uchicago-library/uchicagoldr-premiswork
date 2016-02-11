import unittest
import xml.etree.ElementTree as ET
import xml.dom.minidom

from pypremis.nodes import *
from pypremis.lib import PremisRecord


class Test(unittest.TestCase):
    def testObject(self):
        # Layer 3
        formatDesignation = FormatDesignation('format_name')
        self.assertEqual(formatDesignation.get_name(), 'formatDesignation')

        self.assertEqual(formatDesignation.get_formatName(), 'format_name')
        formatDesignation.set_formatVersion('format_version')
        self.assertEqual(formatDesignation.get_formatVersion(), 'format_version')

        formatRegistry = FormatRegistry('format_registry_name', 'format_registry_key')
        self.assertEqual(formatRegistry.get_name(), 'formatRegistry')

        self.assertEqual(formatRegistry.get_formatRegistryName(), 'format_registry_name')
        self.assertEqual(formatRegistry.get_formatRegistryKey(), 'format_registry_key')
        formatRegistry.set_formatRegistryRole('format_registry_role')
        self.assertEqual(formatRegistry.get_formatRegistryRole(), 'format_registry_role')

        # Layer 2
        fixity = Fixity('message_digest_algorithm', 'message_digest')
        self.assertEqual(fixity.get_name(), 'fixity')

        self.assertEqual(fixity.get_messageDigestAlgorithm(), 'message_digest_algorithm')
        self.assertEqual(fixity.get_messageDigest(), 'message_digest')
        fixity.set_messageDigestOriginator('message_digest_originator')
        self.assertEqual(fixity.get_messageDigestOriginator(), 'message_digest_originator')
        fixity_2 = Fixity('message_digest_algorithm_2', 'message_digest_2')

        format = Format()
        self.assertEqual(format.get_name(), 'format')

        format.set_formatDesignation(formatDesignation)
        self.assertEqual(format.get_formatDesignation(), formatDesignation)
        format.set_formatRegistry(formatRegistry)
        self.assertEqual(format.get_formatRegistry(), formatRegistry)
        format.set_formatNote('format_note')
        self.assertEqual(format.get_formatNote(), ['format_note'])
        format.add_formatNote('format_note_2')
        self.assertEqual(format.get_formatNote(), ['format_note', 'format_note_2'])
        self.assertEqual(format.get_formatNote(1), 'format_note_2')
        format_2 = Format()

        creatingApplication = CreatingApplication()
        self.assertEqual(creatingApplication.get_name(), 'creatingApplication')

        creatingApplication.set_creatingApplicationName('creating_application_name')
        self.assertEqual(creatingApplication.get_creatingApplicationName(), 'creating_application_name')
        creatingApplication.set_creatingApplicationVersion('creating_application_version')
        self.assertEqual(creatingApplication.get_creatingApplicationVersion(), 'creating_application_version')
        creatingApplication.set_dateCreatedByApplication('date_created_by_application')
        self.assertEqual(creatingApplication.get_dateCreatedByApplication(), 'date_created_by_application')
        creatingApplication.set_creatingApplicationExtension('creating_application_extension')
        self.assertEqual(creatingApplication.get_creatingApplicationExtension(), ['creating_application_extension'])
        creatingApplication.add_creatingApplicationExtension('creating_application_extension_2')
        self.assertEqual(creatingApplication.get_creatingApplicationExtension(), ['creating_application_extension', 'creating_application_extension_2'])
        self.assertEqual(creatingApplication.get_creatingApplicationExtension(1), 'creating_application_extension_2')
        creatingApplication_2 = CreatingApplication()

        inhibitors = Inhibitors('inhibitor_type')
        self.assertEqual(inhibitors.get_name(), 'inhibitors')

        self.assertEqual(inhibitors.get_inhibitorType(), 'inhibitor_type')
        inhibitors.set_inhibitorTarget('inhibitor_target')
        self.assertEqual(inhibitors.get_inhibitorTarget(), ['inhibitor_target'])
        inhibitors.add_inhibitorTarget('inhibitor_target_2')
        self.assertEqual(inhibitors.get_inhibitorTarget(), ['inhibitor_target', 'inhibitor_target_2'])
        self.assertEqual(inhibitors.get_inhibitorTarget(1), 'inhibitor_target_2')
        inhibitors.set_inhibitorKey('inhibitor_key')
        self.assertEqual(inhibitors.get_inhibitorKey(), 'inhibitor_key')
        inhibitors_2 = Inhibitors('inhibitor_type_2')

        contentLocation = ContentLocation('content_location_type', 'content_location_value')
        self.assertEqual(contentLocation.get_name(), 'contentLocation')

        self.assertEqual(contentLocation.get_contentLocationType(), 'content_location_type')
        self.assertEqual(contentLocation.get_contentLocationValue(), 'content_location_value')

        signature = Signature('signature_encoding', 'signature_method', 'signature_value', 'signature_validation_rules')
        self.assertEqual(signature.get_name(), 'signature')

        self.assertEqual(signature.get_signatureEncoding(), 'signature_encoding')
        self.assertEqual(signature.get_signatureMethod(), 'signature_method')
        self.assertEqual(signature.get_signatureValue(), 'signature_value')
        self.assertEqual(signature.get_signatureValidationRules(), 'signature_validation_rules')
        signature.set_signer('signer')
        self.assertEqual(signature.get_signer(), 'signer')
        signature.set_signatureProperties('signature_properties')
        self.assertEqual(signature.get_signatureProperties(), ['signature_properties'])
        signature.add_signatureProperties('signature_properties_2')
        self.assertEqual(signature.get_signatureProperties(), ['signature_properties', 'signature_properties_2'])
        self.assertEqual(signature.get_signatureProperties(1), 'signature_properties_2')
        signature.set_keyInformation('key_information')
        self.assertEqual(signature.get_keyInformation(), 'key_information')
        signature_2 = Signature('signature_encoding_2', 'signature_method_2', 'signature_value_2', 'signature_validation_rules_2')

        relatedObjectIdentifier = RelatedObjectIdentifier('related_object_identifier_type', 'related_object_identifier_value')
        self.assertEqual(relatedObjectIdentifier.get_name(), 'relatedObjectIdentifier')

        self.assertEqual(relatedObjectIdentifier.get_relatedObjectIdentifierType(), 'related_object_identifier_type')
        self.assertEqual(relatedObjectIdentifier.get_relatedObjectIdentifierValue(), 'related_object_identifier_value')
        relatedObjectIdentifier.set_relatedObjectSequence('related_object_sequence')
        self.assertEqual(relatedObjectIdentifier.get_relatedObjectSequence(), 'related_object_sequence')
        relatedObjectIdentifier_2 = RelatedObjectIdentifier('related_object_identiifer_type_2', 'related_object_identifier_value_2')

        relatedEventIdentifier = RelatedEventIdentifier('related_event_identifier_type', 'related_event_identifier_value')
        self.assertEqual(relatedEventIdentifier.get_name(), 'relatedEventIdentifier')

        self.assertEqual(relatedEventIdentifier.get_relatedEventIdentifierType(), 'related_event_identifier_type')
        self.assertEqual(relatedEventIdentifier.get_relatedEventIdentifierValue(), 'related_event_identifier_value')
        relatedEventIdentifier.set_relatedEventSequence('related_event_sequence')
        self.assertEqual(relatedEventIdentifier.get_relatedEventSequence(), 'related_event_sequence')
        relatedEventIdentifier_2 = RelatedEventIdentifier('related_event_identifier_type_2', 'related_event_identifier_value_2')

        # Layer 1
        objectIdentifier = ObjectIdentifier('object_identifier_type', 'object_identifier_value')
        self.assertEqual(objectIdentifier.get_name(), 'objectIdentifier')

        self.assertEqual(objectIdentifier.get_objectIdentifierType(), 'object_identifier_type')
        self.assertEqual(objectIdentifier.get_objectIdentifierValue(), 'object_identifier_value')

        preservationLevel = PreservationLevel('preservation_level_value')
        self.assertEqual(preservationLevel.get_name(), 'preservationLevel')

        self.assertEqual(preservationLevel.get_preservationLevelValue(), 'preservation_level_value')
        preservationLevel.set_preservationLevelType('preservation_level_type')
        self.assertEqual(preservationLevel.get_preservationLevelType(), 'preservation_level_type')
        preservationLevel.set_preservationLevelRole('preservation_level_role')
        self.assertEqual(preservationLevel.get_preservationLevelRole(), 'preservation_level_role')
        preservationLevel.set_preservationLevelRationale('preservation_level_rationale')
        self.assertEqual(preservationLevel.get_preservationLevelRationale(), ['preservation_level_rationale'])
        preservationLevel.add_preservationLevelRationale('preservation_level_rationale_2')
        self.assertEqual(preservationLevel.get_preservationLevelRationale(), ['preservation_level_rationale', 'preservation_level_rationale_2'])
        self.assertEqual(preservationLevel.get_preservationLevelRationale(1), 'preservation_level_rationale_2')
        preservationLevel.set_preservationLevelDateAssigned('preservation_level_date_assigned')
        self.assertEqual(preservationLevel.get_preservationLevelDateAssigned(), 'preservation_level_date_assigned')
        preservationLevel_2 = PreservationLevel('preservation_level_value_2')

        significantProperties = SignificantProperties()
        self.assertEqual(significantProperties.get_name(), 'significantProperties')

        significantProperties.set_significantPropertiesType('significant_properties_type')
        self.assertEqual(significantProperties.get_significantPropertiesType(), 'significant_properties_type')
        significantProperties.set_significantPropertiesValue('significant_properties_value')
        self.assertEqual(significantProperties.get_significantPropertiesValue(), 'significant_properties_value')
        significantProperties.set_significantPropertiesExtension('significant_properties_extension')
        self.assertEqual(significantProperties.get_significantPropertiesExtension(), ['significant_properties_extension'])
        significantProperties.add_significantPropertiesExtension('significant_properties_extension_2')
        self.assertEqual(significantProperties.get_significantPropertiesExtension(), ['significant_properties_extension', 'significant_properties_extension_2'])
        self.assertEqual(significantProperties.get_significantPropertiesExtension(1), 'significant_properties_extension_2')
        significantProperties_2 = SignificantProperties()

        objectCharacteristics = ObjectCharacteristics(format)
        self.assertEqual(objectCharacteristics.get_name(), 'objectCharacteristics')

        objectCharacteristics.set_compositionLevel('composition_level')
        self.assertEqual(objectCharacteristics.get_compositionLevel(), 'composition_level')
        objectCharacteristics.set_fixity(fixity)
        self.assertEqual(objectCharacteristics.get_fixity(), [fixity])
        objectCharacteristics.add_fixity(fixity_2)
        self.assertEqual(objectCharacteristics.get_fixity(), [fixity, fixity_2])
        self.assertEqual(objectCharacteristics.get_fixity(1), fixity_2)
        objectCharacteristics.set_size('size')
        self.assertEqual(objectCharacteristics.get_size(), 'size')
        objectCharacteristics.set_format(format)
        self.assertEqual(objectCharacteristics.get_format(), [format])
        objectCharacteristics.add_format(format_2)
        self.assertEqual(objectCharacteristics.get_format(), [format, format_2])
        self.assertEqual(objectCharacteristics.get_format(1), format_2)
        objectCharacteristics.set_creatingApplication(creatingApplication)
        self.assertEqual(objectCharacteristics.get_creatingApplication(), [creatingApplication])
        objectCharacteristics.add_creatingApplication(creatingApplication_2)
        self.assertEqual(objectCharacteristics.get_creatingApplication(), [creatingApplication, creatingApplication_2])
        self.assertEqual(objectCharacteristics.get_creatingApplication(1), creatingApplication_2)
        objectCharacteristics.set_inhibitors(inhibitors)
        self.assertEqual(objectCharacteristics.get_inhibitors(), [inhibitors])
        objectCharacteristics.add_inhibitors(inhibitors_2)
        self.assertEqual(objectCharacteristics.get_inhibitors(), [inhibitors, inhibitors_2])
        self.assertEqual(objectCharacteristics.get_inhibitors(1), inhibitors_2)
        objectCharacteristics.set_objectCharacteristicsExtension('object_characteristics_extension')
        self.assertEqual(objectCharacteristics.get_objectCharacteristicsExtension(), ['object_characteristics_extension'])
        objectCharacteristics.add_objectCharacteristicsExtension('object_characteristics_extension_2')
        self.assertEqual(objectCharacteristics.get_objectCharacteristicsExtension(), ['object_characteristics_extension', 'object_characteristics_extension_2'])
        self.assertEqual(objectCharacteristics.get_objectCharacteristicsExtension(1), 'object_characteristics_extension_2')
        objectCharacteristics_2 = ObjectCharacteristics(format_2)

        storage = Storage()
        self.assertEqual(storage.get_name(), 'storage')

        storage.set_contentLocation(contentLocation)
        self.assertEqual(storage.get_contentLocation(), contentLocation)
        storage.set_storageMedium('storage_medium')
        self.assertEqual(storage.get_storageMedium(), 'storage_medium')
        storage_2 = Storage()

        signatureInformation = SignatureInformation()
        self.assertEqual(signatureInformation.get_name(), 'signatureInformation')

        signatureInformation.set_signature(signature)
        self.assertEqual(signatureInformation.get_signature(), [signature])
        signatureInformation.add_signature(signature_2)
        self.assertEqual(signatureInformation.get_signature(), [signature, signature_2])
        self.assertEqual(signatureInformation.get_signature(1), signature_2)
        signatureInformation.set_signatureInformationExtension('signature_information_extension')
        self.assertEqual(signatureInformation.get_signatureInformationExtension(), ['signature_information_extension'])
        signatureInformation.add_signatureInformationExtension('signature_information_extension_2')
        self.assertEqual(signatureInformation.get_signatureInformationExtension(), ['signature_information_extension', 'signature_information_extension_2'])
        self.assertEqual(signatureInformation.get_signatureInformationExtension(1), 'signature_information_extension_2')
        signatureInformation_2 = SignatureInformation()

        environmentFunction = EnvironmentFunction('environment_function_type', 'environment_function_level')
        self.assertEqual(environmentFunction.get_name(), 'environmentFunction')

        self.assertEqual(environmentFunction.get_environmentFunctionType(), 'environment_function_type')
        self.assertEqual(environmentFunction.get_environmentFunctionLevel(), 'environment_function_level')
        environmentFunction_2 = EnvironmentFunction('environment_function_type_2', 'environment_function_level_2')

        environmentDesignation = EnvironmentDesignation('environment_name')
        self.assertEqual(environmentDesignation.get_name(), 'environmentDesignation')

        self.assertEqual(environmentDesignation.get_environmentName(), 'environment_name')
        environmentDesignation.set_environmentVersion('environment_version')
        self.assertEqual(environmentDesignation.get_environmentVersion(), 'environment_version')
        environmentDesignation.set_environmentOrigin('environment_origin')
        self.assertEqual(environmentDesignation.get_environmentOrigin(), 'environment_origin')
        environmentDesignation.set_environmentDesignationNote('environment_designation_note')
        self.assertEqual(environmentDesignation.get_environmentDesignationNote(), ['environment_designation_note'])
        environmentDesignation.add_environmentDesignationNote('environment_designation_note_2')
        self.assertEqual(environmentDesignation.get_environmentDesignationNote(), ['environment_designation_note', 'environment_designation_note_2'])
        self.assertEqual(environmentDesignation.get_environmentDesignationNote(1), 'environment_designation_note_2')
        environmentDesignation.set_environmentDesignationExtension('environment_designation_extension')
        self.assertEqual(environmentDesignation.get_environmentDesignationExtension(), ['environment_designation_extension'])
        environmentDesignation.add_environmentDesignationExtension('environment_designation_extension_2')
        self.assertEqual(environmentDesignation.get_environmentDesignationExtension(), ['environment_designation_extension', 'environment_designation_extension_2'])
        self.assertEqual(environmentDesignation.get_environmentDesignationExtension(1), 'environment_designation_extension_2')
        environmentDesignation_2 = EnvironmentDesignation('environment_name_2')

        environmentRegistry = EnvironmentRegistry('environment_registry_name', 'environment_registry_key')
        self.assertEqual(environmentRegistry.get_name(), 'environmentRegistry')

        self.assertEqual(environmentRegistry.get_environmentRegistryName(), 'environment_registry_name')
        self.assertEqual(environmentRegistry.get_environmentRegistryKey(), 'environment_registry_key')
        environmentRegistry.set_environmentRegistryRole('environment_registry_role')
        self.assertEqual(environmentRegistry.get_environmentRegistryRole(), 'environment_registry_role')
        environmentRegistry_2 = EnvironmentRegistry('environment_registry_name_2', 'environment_registry_key_2')

        relationship = Relationship('relationship_type', 'relationship_sub_type', relatedObjectIdentifier)
        self.assertEqual(relationship.get_name(), 'relationship')

        self.assertEqual(relationship.get_relationshipType(), 'relationship_type')
        self.assertEqual(relationship.get_relationshipSubType(), 'relationship_sub_type')
        self.assertEqual(relationship.get_relatedObjectIdentifier(), [relatedObjectIdentifier])
        relationship.add_relatedObjectIdentifier(relatedObjectIdentifier_2)
        self.assertEqual(relationship.get_relatedObjectIdentifier(), [relatedObjectIdentifier, relatedObjectIdentifier_2])
        self.assertEqual(relationship.get_relatedObjectIdentifier(1), relatedObjectIdentifier_2)
        relationship.set_relatedEventIdentifier(relatedEventIdentifier)
        self.assertEqual(relationship.get_relatedEventIdentifier(), [relatedEventIdentifier])
        relationship.add_relatedEventIdentifier(relatedEventIdentifier_2)
        self.assertEqual(relationship.get_relatedEventIdentifier(), [relatedEventIdentifier, relatedEventIdentifier_2])
        self.assertEqual(relationship.get_relatedEventIdentifier(1), relatedEventIdentifier_2)
        relationship.set_relatedEnvironmentPurpose('related_environment_purpose')
        self.assertEqual(relationship.get_relatedEnvironmentPurpose(), ['related_environment_purpose'])
        relationship.add_relatedEnvironmentPurpose('related_environment_purpose_2')
        self.assertEqual(relationship.get_relatedEnvironmentPurpose(), ['related_environment_purpose', 'related_environment_purpose_2'])
        self.assertEqual(relationship.get_relatedEnvironmentPurpose(1), 'related_environment_purpose_2')
        relationship.set_relatedEnvironmentCharacteristic('related_environment_characteristic')
        self.assertEqual(relationship.get_relatedEnvironmentCharacteristic(), 'related_environment_characteristic')
        relationship_2 = Relationship('relationship_type_2', 'relationship_sub_type_2', relatedObjectIdentifier_2)

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

        # Layer 0
        object = Object(objectIdentifier, 'file', objectCharacteristics)
        self.assertEqual(object.get_name(), 'object')

        self.assertEqual(object.get_objectIdentifier(), [objectIdentifier])
        self.assertEqual(object.get_objectCategory(), 'file')
        self.assertEqual(object.get_objectCharacteristics(), [objectCharacteristics])

        object.set_preservationLevel(preservationLevel)
        self.assertEqual(object.get_preservationLevel(), [preservationLevel])
        object.add_preservationLevel(preservationLevel_2)
        self.assertEqual(object.get_preservationLevel(), [preservationLevel, preservationLevel_2])
        self.assertEqual(object.get_preservationLevel(1), preservationLevel_2)

        object.set_significantProperties(significantProperties)
        self.assertEqual(object.get_significantProperties(), [significantProperties])
        object.add_significantProperties(significantProperties_2)
        self.assertEqual(object.get_significantProperties(), [significantProperties, significantProperties_2])
        self.assertEqual(object.get_significantProperties(1), significantProperties_2)

        object.set_objectCharacteristics(objectCharacteristics)
        self.assertEqual(object.get_objectCharacteristics(), [objectCharacteristics])
        object.add_objectCharacteristics(objectCharacteristics_2)
        self.assertEqual(object.get_objectCharacteristics(), [objectCharacteristics, objectCharacteristics_2])
        self.assertEqual(object.get_objectCharacteristics(1), objectCharacteristics_2)

        object.set_originalName('originalName')
        self.assertEqual(object.get_originalName(), 'originalName')

        object.set_storage(storage)
        self.assertEqual(object.get_storage(), [storage])
        object.add_storage(storage_2)
        self.assertEqual(object.get_storage(), [storage, storage_2])
        self.assertEqual(object.get_storage(1), storage_2)

        object.set_signatureInformation(signatureInformation)
        self.assertEqual(object.get_signatureInformation(), [signatureInformation])
        object.add_signatureInformation(signatureInformation_2)
        self.assertEqual(object.get_signatureInformation(), [signatureInformation, signatureInformation_2])
        self.assertEqual(object.get_signatureInformation(1), signatureInformation_2)

        object.set_environmentFunction(environmentFunction)
        self.assertEqual(object.get_environmentFunction(), [environmentFunction])
        object.add_environmentFunction(environmentFunction_2)
        self.assertEqual(object.get_environmentFunction(), [environmentFunction, environmentFunction_2])
        self.assertEqual(object.get_environmentFunction(1), environmentFunction_2)

        object.set_environmentDesignation(environmentDesignation)
        self.assertEqual(object.get_environmentDesignation(), [environmentDesignation])
        object.add_environmentDesignation(environmentDesignation_2)
        self.assertEqual(object.get_environmentDesignation(), [environmentDesignation, environmentDesignation_2])
        self.assertEqual(object.get_environmentDesignation(1), environmentDesignation_2)

        object.set_environmentRegistry(environmentRegistry)
        self.assertEqual(object.get_environmentRegistry(), [environmentRegistry])
        object.add_environmentRegistry(environmentRegistry_2)
        self.assertEqual(object.get_environmentRegistry(), [environmentRegistry, environmentRegistry_2])
        self.assertEqual(object.get_environmentRegistry(1), environmentRegistry_2)

        object.set_environmentExtension('environment_extension')
        self.assertEqual(object.get_environmentExtension(), ['environment_extension'])
        object.add_environmentExtension('environment_extension_2')
        self.assertEqual(object.get_environmentExtension(), ['environment_extension', 'environment_extension_2'])
        self.assertEqual(object.get_environmentExtension(1), 'environment_extension_2')

        object.set_relationship(relationship)
        self.assertEqual(object.get_relationship(), [relationship])
        object.add_relationship(relationship_2)
        self.assertEqual(object.get_relationship(), [relationship, relationship_2])
        self.assertEqual(object.get_relationship(1), relationship_2)

        object.set_linkingEventIdentifier(linkingEventIdentifier)
        self.assertEqual(object.get_linkingEventIdentifier(), [linkingEventIdentifier])
        object.add_linkingEventIdentifier(linkingEventIdentifier_2)
        self.assertEqual(object.get_linkingEventIdentifier(), [linkingEventIdentifier, linkingEventIdentifier_2])
        self.assertEqual(object.get_linkingEventIdentifier(1), linkingEventIdentifier_2)

        object.set_linkingRightsStatementIdentifier(linkingRightsStatementIdentifier)
        self.assertEqual(object.get_linkingRightsStatementIdentifier(), [linkingRightsStatementIdentifier])
        object.add_linkingRightsStatementIdentifier(linkingRightsStatementIdentifier_2)
        self.assertEqual(object.get_linkingRightsStatementIdentifier(), [linkingRightsStatementIdentifier, linkingRightsStatementIdentifier_2])
        self.assertEqual(object.get_linkingRightsStatementIdentifier(1), linkingRightsStatementIdentifier_2)

        record = PremisRecord(objects=[object])
        record.write_to_file('/Users/balsamo/Envs/ldr_dev/repos/uchicagoldr-premiswork/tests/testobject1.xml')

        record_2 = PremisRecord(filepath='/Users/balsamo/Envs/ldr_dev/repos/uchicagoldr-premiswork/tests/testobject1.xml')
        record_2.write_to_file('/Users/balsamo/Envs/ldr_dev/repos/uchicagoldr-premiswork/tests/testobject2.xml')
            
        self.assertEqual(record, record_2)

        record_2.get_object_list()[0].add_objectIdentifier(ObjectIdentifier('a','b'))

        self.assertFalse(record == record_2)



    def testEvent(self):
        # Layer 2
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

        # Layer 1
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

        # Layer 0
        event = Event(eventIdentifier, 'event_type', 'event_date_time')
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

        record = PremisRecord(events=[event])
        record.write_to_file('/Users/balsamo/Envs/ldr_dev/repos/uchicagoldr-premiswork/tests/testevent1.xml')

        record_2 = PremisRecord(filepath='/Users/balsamo/Envs/ldr_dev/repos/uchicagoldr-premiswork/tests/testevent1.xml')
        record_2.write_to_file('/Users/balsamo/Envs/ldr_dev/repos/uchicagoldr-premiswork/tests/testevent2.xml')

        self.assertEqual(record, record_2)

        record.get_event_list()[0].set_eventIdentifier(EventIdentifier('x','y'))
        self.assertFalse(record == record_2)

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

        # Layer 0
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
        self.assertEqual(agent.get_agentType(), 'agent_type')

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
        # Layer 3
        copyrightDocumentationIdentifier = CopyrightDocumentationIdentifier('copyright_documentation_identifier_type', 'copyright_documentation_identifier_value')
        self.assertEqual(copyrightDocumentationIdentifier.get_name(), 'copyrightDocumentationIdentifier')

        self.assertEqual(copyrightDocumentationIdentifier.get_copyrightDocumentationIdentifierType(), 'copyright_documentation_identifier_type')
        self.assertEqual(copyrightDocumentationIdentifier.get_copyrightDocumentationIdentifierValue(), 'copyright_documentation_identifier_value')
        copyrightDocumentationIdentifier_2 = CopyrightDocumentationIdentifier('copyright_documentation_identifier_type_2', 'copyright_documentation_identifier_value_2')

        copyrightApplicableDates = CopyrightApplicableDates()
        self.assertEqual(copyrightApplicableDates.get_name(), 'copyrightApplicableDates')

        copyrightApplicableDates.set_startDate('start_date')
        self.assertEqual(copyrightApplicableDates.get_startDate(), 'start_date')
        copyrightApplicableDates.set_endDate('end_date')
        self.assertEqual(copyrightApplicableDates.get_endDate(), 'end_date')

        licenseDocumentationIdentifier = LicenseDocumentationIdentifier('license_documentation_identifier_type', 'license_documentation_identifier_value')
        self.assertEqual(licenseDocumentationIdentifier.get_name(), 'licenseDocumentationIdentifier')

        self.assertEqual(licenseDocumentationIdentifier.get_licenseDocumentationIdentifierType(), 'license_documentation_identifier_type')
        self.assertEqual(licenseDocumentationIdentifier.get_licenseDocumentationIdentifierValue(), 'license_documentation_identifier_value')
        licenseDocumentationIdentifier.set_licenseDocumentationRole('license_documentation_role')
        self.assertEqual(licenseDocumentationIdentifier.get_licenseDocumentationRole(), 'license_documentation_role')
        licenseDocumentationIdentifier_2 = LicenseDocumentationIdentifier('license_documenation_identifier_type_2', 'license_documentation_identifier_value_2')

        licenseApplicableDates = LicenseApplicableDates()
        self.assertEqual(licenseApplicableDates.get_name(), 'licenseApplicableDates')

        licenseApplicableDates.set_startDate('start_date')
        self.assertEqual(licenseApplicableDates.get_startDate(), 'start_date')
        licenseApplicableDates.set_endDate('end_date')
        self.assertEqual(licenseApplicableDates.get_endDate(), 'end_date')

        statuteDocumentationIdentifier = StatuteDocumentationIdentifier('statute_documentation_identifier_type', 'statute_documentation_identifier_value')
        self.assertEqual(statuteDocumentationIdentifier.get_name(), 'statuteDocumentationIdentifier')

        self.assertEqual(statuteDocumentationIdentifier.get_statuteDocumentationIdentifierType(), 'statute_documentation_identifier_type')
        self.assertEqual(statuteDocumentationIdentifier.get_statuteDocumentationIdentifierValue(), 'statute_documentation_identifier_value')
        statuteDocumentationIdentifier.set_statuteDocumentationRole('statute_documentation_role')
        self.assertEqual(statuteDocumentationIdentifier.get_statuteDocumentationRole(), 'statute_documentation_role')
        statuteDocumentationIdentifier_2 = StatuteDocumentationIdentifier('statute_documentation_identifier_type_2', 'statute_documentation_identifier_value_2')

        statuteApplicableDates = StatuteApplicableDates()
        self.assertEqual(statuteApplicableDates.get_name(), 'statuteApplicableDates')

        statuteApplicableDates.set_startDate('start_date')
        self.assertEqual(statuteApplicableDates.get_startDate(), 'start_date')
        statuteApplicableDates.set_endDate('end_date')
        self.assertEqual(statuteApplicableDates.get_endDate(), 'end_date')

        otherRightsDocumentationIdentifier = OtherRightsDocumentationIdentifier('other_rights_documentation_identifier_type', 'other_rights_documentation_identifier_value')
        self.assertEqual(otherRightsDocumentationIdentifier.get_name(), 'otherRightsDocumentationIdentifier')

        self.assertEqual(otherRightsDocumentationIdentifier.get_otherRightsDocumentationIdentifierType(), 'other_rights_documentation_identifier_type')
        self.assertEqual(otherRightsDocumentationIdentifier.get_otherRightsDocumentationIdentifierValue(), 'other_rights_documentation_identifier_value')
        otherRightsDocumentationIdentifier.set_otherRightsDocumentationRole('other_rights_documentation_role')
        self.assertEqual(otherRightsDocumentationIdentifier.get_otherRightsDocumentationRole(), 'other_rights_documentation_role')
        otherRightsDocumentationIdentifier_2 = OtherRightsDocumentationIdentifier('other_rights_documentation_identifier_type', 'other_rights_documentation_identifier_value')

        otherRightsApplicableDates = OtherRightsApplicableDates()
        self.assertEqual(otherRightsApplicableDates.get_name(), 'otherRightsApplicableDates')

        otherRightsApplicableDates.set_startDate('start_date')
        self.assertEqual(otherRightsApplicableDates.get_startDate(), 'start_date')
        otherRightsApplicableDates.set_endDate('end_date')
        self.assertEqual(otherRightsApplicableDates.get_endDate(), 'end_date')

        termOfGrant = TermOfGrant('start_date')
        self.assertEqual(termOfGrant.get_name(), 'termOfGrant')

        self.assertEqual(termOfGrant.get_startDate(), 'start_date')
        termOfGrant.set_endDate('end_date')
        self.assertEqual(termOfGrant.get_endDate(), 'end_date')

        termOfRestriction = TermOfRestriction('start_date')
        self.assertEqual(termOfRestriction.get_name(), 'termOfRestriction')

        self.assertEqual(termOfRestriction.get_startDate(), 'start_date')
        termOfRestriction.set_endDate('end_date')
        self.assertEqual(termOfRestriction.get_endDate(), 'end_date')

        # Layer 2
        rightsStatementIdentifier = RightsStatementIdentifier('rights_statement_identifier_type', 'rights_statement_identifier_value')
        self.assertEqual(rightsStatementIdentifier.get_name(), 'rightsStatementIdentifier')

        self.assertEqual(rightsStatementIdentifier.get_rightsStatementIdentifierType(), 'rights_statement_identifier_type')
        self.assertEqual(rightsStatementIdentifier.get_rightsStatementIdentifierValue(), 'rights_statement_identifier_value')

        copyrightInformation = CopyrightInformation('copyright_status', 'copyright_jurisdiction')
        self.assertEqual(copyrightInformation.get_name(), 'copyrightInformation')

        self.assertEqual(copyrightInformation.get_copyrightStatus(), 'copyright_status')
        self.assertEqual(copyrightInformation.get_copyrightJurisdiction(), 'copyright_jurisdiction')

        copyrightInformation.set_copyrightStatusDeterminationDate('copyright_status_determination_date')
        self.assertEqual(copyrightInformation.get_copyrightStatusDeterminationDate(), 'copyright_status_determination_date')
        copyrightInformation.set_copyrightNote('copyright_note')
        self.assertEqual(copyrightInformation.get_copyrightNote(), ['copyright_note'])
        copyrightInformation.add_copyrightNote('copyright_note_2')
        self.assertEqual(copyrightInformation.get_copyrightNote(), ['copyright_note', 'copyright_note_2'])
        copyrightInformation.set_copyrightDocumentationIdentifier(copyrightDocumentationIdentifier)
        self.assertEqual(copyrightInformation.get_copyrightDocumentationIdentifier(), [copyrightDocumentationIdentifier])
        copyrightInformation.add_copyrightDocumentationIdentifier(copyrightDocumentationIdentifier_2)
        self.assertEqual(copyrightInformation.get_copyrightDocumentationIdentifier(), [copyrightDocumentationIdentifier, copyrightDocumentationIdentifier_2])
        copyrightInformation.set_copyrightApplicableDates(copyrightApplicableDates)
        self.assertEqual(copyrightInformation.get_copyrightApplicableDates(), copyrightApplicableDates)

        licenseInformation = LicenseInformation()
        self.assertEqual(licenseInformation.get_name(), 'licenseInformation')

        licenseInformation.set_licenseDocumentationIdentifier(licenseDocumentationIdentifier)
        self.assertEqual(licenseInformation.get_licenseDocumentationIdentifier(), [licenseDocumentationIdentifier])
        licenseInformation.add_licenseDocumentationIdentifier(licenseDocumentationIdentifier_2)
        self.assertEqual(licenseInformation.get_licenseDocumentationIdentifier(), [licenseDocumentationIdentifier, licenseDocumentationIdentifier_2])
        self.assertEqual(licenseInformation.get_licenseDocumentationIdentifier(1), licenseDocumentationIdentifier_2)
        licenseInformation.set_licenseTerms('license_terms')
        self.assertEqual(licenseInformation.get_licenseTerms(), 'license_terms')
        licenseInformation.set_licenseNote('license_note')
        self.assertEqual(licenseInformation.get_licenseNote(), ['license_note'])
        licenseInformation.add_licenseNote('license_note_2')
        self.assertEqual(licenseInformation.get_licenseNote(), ['license_note', 'license_note_2'])
        self.assertEqual(licenseInformation.get_licenseNote(1), 'license_note_2')
        licenseInformation.set_licenseApplicableDates(licenseApplicableDates)
        self.assertEqual(licenseInformation.get_licenseApplicableDates(), licenseApplicableDates)

        statuteInformation = StatuteInformation('statute_jurisdiction', 'statute_citation')
        self.assertEqual(statuteInformation.get_name(), 'statuteInformation')

        self.assertEqual(statuteInformation.get_statuteJurisdiction(), 'statute_jurisdiction')
        self.assertEqual(statuteInformation.get_statuteCitation(), 'statute_citation')
        statuteInformation.set_statuteInformationDeterminationDate('statute_information_determination_date')
        self.assertEqual(statuteInformation.get_statuteInformationDeterminationDate(), 'statute_information_determination_date')
        statuteInformation.set_statuteNote('statute_note')
        self.assertEqual(statuteInformation.get_statuteNote(), ['statute_note'])
        statuteInformation.add_statuteNote('statute_note_2')
        self.assertEqual(statuteInformation.get_statuteNote(), ['statute_note', 'statute_note_2'])
        self.assertEqual(statuteInformation.get_statuteNote(1), 'statute_note_2')
        statuteInformation.set_statuteDocumentationIdentifier(statuteDocumentationIdentifier)
        self.assertEqual(statuteInformation.get_statuteDocumentationIdentifier(), [statuteDocumentationIdentifier])
        statuteInformation.add_statuteDocumentationIdentifier(statuteDocumentationIdentifier_2)
        self.assertEqual(statuteInformation.get_statuteDocumentationIdentifier(), [statuteDocumentationIdentifier, statuteDocumentationIdentifier_2])
        self.assertEqual(statuteInformation.get_statuteDocumentationIdentifier(1), statuteDocumentationIdentifier_2)
        statuteInformation.set_statuteApplicableDates(statuteApplicableDates)
        self.assertEqual(statuteInformation.get_statuteApplicableDates(), statuteApplicableDates)
        statuteInformation_2 = StatuteInformation('statute_jurisdiction_2', 'statute_citation_2')

        otherRightsInformation = OtherRightsInformation('other_rights_basis')
        self.assertEqual(otherRightsInformation.get_name(), 'otherRightsInformation')

        self.assertEqual(otherRightsInformation.get_otherRightsBasis(), 'other_rights_basis')
        otherRightsInformation.set_otherRightsDocumentationIdentifier(otherRightsDocumentationIdentifier)
        self.assertEqual(otherRightsInformation.get_otherRightsDocumentationIdentifier(), [otherRightsDocumentationIdentifier])
        otherRightsInformation.add_otherRightsDocumentationIdentifier(otherRightsDocumentationIdentifier_2)
        self.assertEqual(otherRightsInformation.get_otherRightsDocumentationIdentifier(), [otherRightsDocumentationIdentifier, otherRightsDocumentationIdentifier_2])
        self.assertEqual(otherRightsInformation.get_otherRightsDocumentationIdentifier(1), otherRightsDocumentationIdentifier_2)
        otherRightsInformation.set_otherRightsApplicableDates(otherRightsApplicableDates)
        self.assertEqual(otherRightsInformation.get_otherRightsApplicableDates(), otherRightsApplicableDates)
        otherRightsInformation.set_otherRightsNote('other_rights_note')
        self.assertEqual(otherRightsInformation.get_otherRightsNote(), ['other_rights_note'])
        otherRightsInformation.add_otherRightsNote('other_rights_note_2')
        self.assertEqual(otherRightsInformation.get_otherRightsNote(), ['other_rights_note', 'other_rights_note_2'])
        self.assertEqual(otherRightsInformation.get_otherRightsNote(1), 'other_rights_note_2')

        rightsGranted = RightsGranted('act')
        self.assertEqual(rightsGranted.get_name(), 'rightsGranted')

        self.assertEqual(rightsGranted.get_act(), 'act')
        rightsGranted.set_restriction('restriction')
        self.assertEqual(rightsGranted.get_restriction(), ['restriction'])
        rightsGranted.add_restriction('restriction_2')
        self.assertEqual(rightsGranted.get_restriction(), ['restriction', 'restriction_2'])
        self.assertEqual(rightsGranted.get_restriction(1), 'restriction_2')
        rightsGranted.set_termOfGrant(termOfGrant)
        self.assertEqual(rightsGranted.get_termOfGrant(), termOfGrant)
        rightsGranted.set_termOfRestriction(termOfRestriction)
        self.assertEqual(rightsGranted.get_termOfRestriction(), termOfRestriction)
        rightsGranted.set_rightsGrantedNote('rights_granted_note')
        self.assertEqual(rightsGranted.get_rightsGrantedNote(), ['rights_granted_note'])
        rightsGranted.add_rightsGrantedNote('rights_granted_note_2')
        self.assertEqual(rightsGranted.get_rightsGrantedNote(), ['rights_granted_note', 'rights_granted_note_2'])
        self.assertEqual(rightsGranted.get_rightsGrantedNote(1), 'rights_granted_note_2')
        rightsGranted_2 = RightsGranted('act_2')

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

        # Layer 1
        rightsStatement = RightsStatement(rightsStatementIdentifier, 'rights_basis')
        self.assertEqual(rightsStatement.get_name(), 'rightsStatement')

        self.assertEqual(rightsStatement.get_rightsStatementIdentifier(), rightsStatementIdentifier)
        self.assertEqual(rightsStatement.get_rightsBasis(), 'rights_basis')
        rightsStatement.set_copyrightInformation(copyrightInformation)
        self.assertEqual(rightsStatement.get_copyrightInformation(), copyrightInformation)
        rightsStatement.set_licenseInformation(licenseInformation)
        self.assertEqual(rightsStatement.get_licenseInformation(), licenseInformation)
        rightsStatement.set_statuteInformation(statuteInformation)
        self.assertEqual(rightsStatement.get_statuteInformation(), [statuteInformation])
        rightsStatement.add_statuteInformation(statuteInformation_2)
        self.assertEqual(rightsStatement.get_statuteInformation(), [statuteInformation, statuteInformation_2])
        self.assertEqual(rightsStatement.get_statuteInformation(1), statuteInformation_2)
        rightsStatement.set_otherRightsInformation(otherRightsInformation)
        self.assertEqual(rightsStatement.get_otherRightsInformation(), otherRightsInformation)
        rightsStatement.set_rightsGranted(rightsGranted)
        self.assertEqual(rightsStatement.get_rightsGranted(), [rightsGranted])
        rightsStatement.add_rightsGranted(rightsGranted_2)
        self.assertEqual(rightsStatement.get_rightsGranted(), [rightsGranted, rightsGranted_2])
        self.assertEqual(rightsStatement.get_rightsGranted(1), rightsGranted_2)
        rightsStatement.set_linkingObjectIdentifier(linkingObjectIdentifier)
        self.assertEqual(rightsStatement.get_linkingObjectIdentifier(), [linkingObjectIdentifier])
        rightsStatement.add_linkingObjectIdentifier(linkingObjectIdentifier_2)
        self.assertEqual(rightsStatement.get_linkingObjectIdentifier(), [linkingObjectIdentifier, linkingObjectIdentifier_2])
        self.assertEqual(rightsStatement.get_linkingObjectIdentifier(1), linkingObjectIdentifier_2)
        rightsStatement.set_linkingAgentIdentifier(linkingAgentIdentifier)
        self.assertEqual(rightsStatement.get_linkingAgentIdentifier(), [linkingAgentIdentifier])
        rightsStatement.add_linkingAgentIdentifier(linkingAgentIdentifier_2)
        self.assertEqual(rightsStatement.get_linkingAgentIdentifier(), [linkingAgentIdentifier, linkingAgentIdentifier_2])
        self.assertEqual(rightsStatement.get_linkingAgentIdentifier(1), linkingAgentIdentifier_2)
        rightsStatement_2 = RightsStatement(rightsStatementIdentifier, 'rights_basis_2')

        # Layer 0
        rights = Rights(rightsStatement=rightsStatement)
        self.assertEqual(rights.get_name(), 'rights')

        self.assertEqual(rights.get_rightsStatement(), [rightsStatement])
        rights.add_rightsStatement(rightsStatement_2)
        self.assertEqual(rights.get_rightsStatement(), [rightsStatement, rightsStatement_2])
        self.assertEqual(rights.get_rightsStatement(1), rightsStatement_2)
        rights.set_rightsExtension('rights_extension')
        self.assertEqual(rights.get_rightsExtension(), ['rights_extension'])
        rights.add_rightsExtension('rights_extension_2')
        self.assertEqual(rights.get_rightsExtension(), ['rights_extension', 'rights_extension_2'])
        self.assertEqual(rights.get_rightsExtension(1), 'rights_extension_2')

if __name__ == '__main__':
    unittest.main()
