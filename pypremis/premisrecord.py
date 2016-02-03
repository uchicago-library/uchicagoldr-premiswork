import xml.etree.ElementTree as ET


class PremisRecord(object):
    def __init__(self):
        self.root = ET.Element('premis')
        self.events = []
        self.objects = []
        self.entities = []
        self.rights = []
        self.filepath = None

    def __repr__(self):
        return ET.tostring(self.root, encoding="unicode")

    def __iter__(self):
        for x in self.events + self.objects + self.entites + self.rights:
            return x

    def add_event(self, event):
        pass

    def get_event(self, eventID):
        pass

    def get_events(self):
        return self.events

    def add_object(self, obj):
        pass

    def get_object(self, objID):
        pass

    def get_objects(self):
        return self.objects

    def add_entity(self, entity):
        pass

    def get_entity(self, entityID):
        pass

    def get_entities(self):
        return self.entities

    def add_rights(self, rights):
        pass

    def get_rights(self, rightsID):
        pass

    def get_all_rights(self):
        return self.rights

    def validate(self):
        pass

    def populate_from_file(self):
        pass

    def write_to_file(self, targetpath):
        pass


class PremisObject(object):
    def __init__(self):
        self.root = ET.Element('object')
        pass

    def __repr__(self):
        return ET.tostring(self.root, encoding="unicode")

    def set_objectIdentifier(self, objectIdentifier):
        pass

    def get_objectIdentifier(self):
        pass

    def add_objectIdentifier(self, objectIdentifier):
        pass

    def set_objectCategory(self, objectCategory):
        pass

    def get_objectCategory(self):
        pass

    def set_preservationLevel(self, preservationLevel):
        pass

    def get_preservationLevel(self):
        pass

    def add_preservationLevel(self, preservationLevel):
        pass

    def set_significantProperties(self, significantProperties):
        pass

    def get_significantProperties(self):
        pass

    def add_significantProperties(self, significantProperties):
        pass

    def set_objectCharacteristics(self, objectCharacteristics):
        pass

    def get_objectCharacteristics(self):
        pass

    def add_objectCharacteristics(self, objectCharacteristics):
        pass

    def set_originalName(self, originalName):
        pass

    def get_originalName(self):
        pass

    def set_storage(self, storage):
        pass

    def get_storage(self):
        pass

    def add_storage(self, storage):
        pass

    def set_signatureInformation(self, signatureInformation):
        pass

    def get_signatureInformation(self):
        pass

    def add_signatureInformation(self, signatureInformation):
        pass

    def set_environmentFunction(self, environmentFunction):
        pass

    def get_environmentFunction(self):
        pass

    def add_environmentFunction(self, environmentFunction):
        pass

    def set_environmentDesignation(self, environmentDesignation):
        pass

    def get_environmentDesignation(self):
        pass

    def add_environmentDesignation(self, environmentDesignation):
        pass

    def set_environmentRegistry(self, environmentRegistry):
        pass

    def get_environmentRegistry(self):
        pass

    def add_environmentRegistry(self, environmentRegistry):
        pass

    def set_environmentExtension(self, environmentExtension):
        pass

    def get_environmentExtension(self):
        pass

    def add_environmentExtension(self, environmentExtension):
        pass

    def set_relationship(self, relationship):
        pass

    def get_relationship(self):
        pass

    def add_relationship(self, relationship):
        pass

    def set_linkingEventIdentifier(self, linkingEventIdentifier):
        pass

    def get_linkingEventIdentifier(self):
        pass

    def add_linkingEventIdentifier(self, linkingEventIdentifier):
        pass

    def set_linkingRightsStatementIdentifier(self, linkingRightsStatementIdentifier):
        pass

    def get_linkingRightsStatementIdentifier(self):
        pass

    def add_linkingRightsStatementIdentifier(self, linkingRightsStatementIdentifier):
        pass


class ObjectIdentifier(object):
    def __init__(self):
        self.root = ET.Element('objectIdentifier')
        pass

    def __repr__(self):
        return ET.tostring(self.root, encoding='unicode')

    def set_objectIdentifierType(self, objectIdentifierType):
        pass

    def get_objectIdentifierType(self):
        pass

    def set_objectIdentifierValue(self, objectIdentifierValue):
        pass

    def get_objectIdentifierValue(self):
        pass


class LinkingObjectIdentifier(object):
    def __init__(self):
        self.root = ET.Element('linkingObjectIdentifier')
        pass

    def __repr__(self):
        return ET.tostring(self.root, encoding='unicode')

    def set_linkingObjectIdentifierType(self, linkingObjectIdentifierType):
        pass

    def get_linkingObjectIdentifierType(self):
        pass

    def set_linkingObjectIdentifierValue(self, linkingObjectIdentifierValue):
        pass

    def get_linkingObjectIdentifierValue(self):
        pass

    def set_linkingObjectRole(self, linkingObjectRole):
        pass

    def get_linkingObjectRole(self):
        pass

    def add_linkingObjectRole(self, linkingObjectRole):
        pass


class EventIdentifier(object):
    def __init__(self):
        self.root = ET.Element('eventIdentifier')
        pass

    def __repr__(self):
        return ET.tostring(self.root, encoding='unicode')

    def set_eventIdentifierType(self, eventIdentifierType):
        pass

    def get_eventIdentifierType(self):
        pass

    def set_eventIdentifierValue(self, eventIdentifierValue):
        pass

    def get_eventIdentifierValue(self):
        pass


class LinkingEventIdentifier(object):
    def __init__(self):
        self.root = ET.Element('linkingEventIdentifier')
        pass

    def __repr__(self):
        return ET.tostring(self.root, encoding='unicode')

    def set_linkingEventIdentifierType(self, linkingEventIdentifierType):
        pass

    def get_linkingEventIdentifierType(self):
        pass

    def set_linkingEventIdentifierValue(self, linkingEventIdentifierValue):
        pass

    def get_linkingEventIdentifierValue(self):
        pass


class LinkingRightsStatementIdentifier(object):
    def __init__(self):
        self.root = ET.Element('linkingRightsStatementIdentifier')
        pass

    def __repr__(self):
        return ET.tostring(self.root, encoding='unicode')

    def set_linkingRightsStatementIdentifierType(self, linkingRightsStatementIdentifierType):
        pass

    def get_linkingRightsStatementIdentifierType(self):
        pass

    def set_linkingRightsStatementIdentifierValue(self, linkingRightsStatementIdentifierValue):
        pass

    def get_linkingRightsStatementIdentifierValue(self):
        pass


class Relationship(object):
    def __init__(self):
        self.root = ET.Element('relationship')
        pass

    def __repr__(self):
        return ET.tostring(self.root, encoding='unicode')

    def set_relationshipType(self, relationshipType):
        pass

    def get_relationshipType(self):
        pass

    def set_relationshipSubType(self, relationshipSubType):
        pass

    def get_relationshipSubType(self):
        pass

    def set_relatedObjectIdentifier(self, relatedObjectIdentifier):
        pass

    def get_relatedObjectIdentifier(self):
        pass

    def add_relatedObjectIdentifier(self, relatedObjectIdentifier):
        pass

    def set_relatedEventIdentifier(self, relatedEventIdentifer):
        pass

    def get_relatedEventIdentifier(self):
        pass

    def add_relatedEventIdentifier(self, relatedEventIdentifier):
        pass

    def set_relatedEnvironmentPurpose(self, relatedEnvironmentPurpose):
        pass

    def get_relatedEnvironmentPurpose(self):
        pass

    def add_relatedEnvironmentPurpose(self, relatedEnvironmentPurpose):
        pass

    def set_relatedEnvironmentCharacteristic(self, relatedEnvironmentCharacteristic):
        pass

    def get_relatedEnvironmentCharacteristic(self):
        pass


class RelatedEventIdentifier(object):
    def __init__(self):
        self.root = ET.Element('relatedEventIdentifier')
        pass

    def __repr__(self):
        return ET.tostring(self.root, encoding='unicode')

    def set_relatedEventIdentifierType(self, relatedEventIdentifierType):
        pass

    def get_relatedEventIdentifierType(self):
        pass

    def set_relatedEventIdentifierValue(self, relatedEventIdentifierValue):
        pass

    def get_relatedEventIdentifierValue(self):
        pass

    def set_relatedEventSequence(self, relatedEventSequence):
        pass

    def get_relatedEventSequence(self):
        pass


class RelatedObjectIdentifier(object):
    def __init__(self):
        self.root = ET.Element('relatedObjectIdentifier')
        pass

    def __repr__(self):
        return ET.tostring(self.root, encoding='unicode')

    def set_relatedObjectIdentifierType(self, relatedObjectIdentifierType):
        pass

    def get_relatedObjectIdentifierType(self):
        pass

    def set_relatedObjectIdentifierValue(self, relatedObjectIdentifierValue):
        pass

    def get_relatedObjectIdentifierValue(self):
        pass

    def set_relatedObjectSequence(self, relatedObjectSequence):
        pass

    def get_relatedObjectSequence(self):
        pass


class EnvironmentRegistry(object):
    def __init__(self):
        self.root = ET.Element('environmentRegistry')
        pass

    def __repr__(self):
        return ET.tostring(self.root, encoding='unicode')

    def set_environmentRegistryName(self, environmentRegistryName):
        pass

    def get_environmentRegistryName(self):
        pass

    def set_environmentRegistryKey(self, environmentRegistryKey):
        pass

    def get_environmentRegistryKey(self):
        pass

    def set_environmentRegistryRole(self, environmentRegistryRole):
        pass

    def get_environmentRegistryRole(self):
        pass


class EnvironmentDesignation(object):
    def __init__(self):
        self.root = ET.Element('environmentDesignation')
        pass

    def __repr__(self):
        return ET.tostring(self.root, encoding='unicode')

    def set_environmentName(self, environmentName):
        pass

    def get_environmentName(self):
        pass

    def set_environmentVersion(self, environmentVersion):
        pass

    def get_environmentVersion(self):
        pass

    def set_environmentOrigin(self, environmentOrigin):
        pass

    def get_environmentOrigin(self):
        pass

    def set_environmentDesignationNote(self, environmentDesignationNote):
        pass

    def get_environmentDesignationNote(self):
        pass

    def add_environmentDesignationNote(self, environmentDesignationNote):
        pass

    def set_environmentDesignationExtension(self, environmentDesignationExtension):
        pass

    def get_environmentDesignationExtension(self):
        pass

    def add_environmentDesignationExtension(self, environmentDesignationExtension):
        pass


class EnvironmentFunction(object):
    def __init__(self):
        self.root = ET.Element('environmentFunction')
        pass

    def __repr__(self):
        return ET.tostring(self.root, encoding='unicode')

    def set_environmentFunctionType(self, environmentFunctionType):
        pass

    def get_environmentFunctionType(self):
        pass

    def set_environmentFunctionLevel(self, environmentFunctionLevel):
        pass

    def get_environmentFunctionLevel(self):
        pass


class SignatureInformation(object):
    def __init__(self):
        self.root = ET.Element('signatureInformation')
        pass

    def __repr__(self):
        return ET.tostring(self.root, encoding="unicode")

    def set_signature(self, signature):
        pass

    def get_signature(self):
        pass

    def add_signature(self, signature):
        pass

    def set_signatureInformationExtension(self, signatureInformationExtension):
        pass

    def get_signatureInformationExtension(self):
        pass

    def add_signatureInformationExtension(self, signatureInformationExtension):
        pass


class Signature(object):
    def __init__(self):
        self.root = ET.Element('signature')
        pass

    def __repr__(self):
        return ET.tostring(self.root, encoding="unicode")

    def set_signatureEncoding(self, signatureEncoding):
        pass

    def get_signatureEncoding(self):
        pass

    def set_signer(self, signer):
        pass

    def get_signer(self):
        pass

    def set_signatureMethod(self, signatureMethod):
        pass

    def get_signatureMethod(self):
        pass

    def set_signatureValue(self, signatureValue):
        pass

    def get_signatureValue(self):
        pass

    def set_signatureValidationRules(self, signatureValidationRules):
        pass

    def get_signatureValidationRules(self):
        pass

    def set_signatureProperties(self, signatureProperties):
        pass

    def add_signatureProperties(self, signatureProperties):
        pass

    def get_signatureProperties(self):
        pass

    def set_keyInformation(self, keyInformation):
        pass

    def get_keyInformation(self):
        pass


class Storage(object):
    def __init__(self):
        self.root = ET.Element('storage')
        pass

    def __repr__(self):
        return ET.tostring(self.root, encoding="unicode")

    def set_contentLocation(self, contentLocation):
        pass

    def get_contentLocation(self):
        pass

    def set_storageMedium(self, storageMedium):
        pass

    def get_storageMedium(self):
        pass


class ContentLocation(object):
    def __init__(self):
        self.root = ET.Element('contentLocation')
        pass

    def __repr__(self):
        return ET.tostring(self.root, encoding="unicode")

    def set_contentLocationType(self, contentLocationType):
        pass

    def get_contentLocationType(self):
        pass

    def set_contentLocationValue(self, contentLocationValue):
        pass

    def get_contentLocationValue(self):
        pass


class ObjectCharacteristics(object):
    def __init__(self):
        self.root = ET.Element('objectCharacteristics')
        pass

    def __repr__(self):
        return ET.tostring(self.root, encoding="unicode")

    def set_compositionLevel(self, compositionLevel):
        pass

    def get_compositionLevel(self):
        pass

    def set_fixity(self, fixity):
        pass

    def get_fixity(self):
        pass

    def add_fixity(self, fixity):
        pass

    def set_size(self, size):
        pass

    def get_size(self):
        pass

    def set_format(self, format):
        pass

    def get_format(self):
        pass

    def add_format(self, format):
        pass

    def set_creatingApplication(self, creatingApplication):
        pass

    def get_creatingApplication(self):
        pass

    def add_creatingApplication(self, creatingApplication):
        pass

    def set_inhibitors(self, inhibitors):
        pass

    def get_inhibitors(self):
        pass

    def add_inhibitors(self, inhibitors):
        pass

    def set_objectCharacteristicsExtension(self, objectCharacteristicsExtension):
        pass

    def get_objectCharacteristicsExtension(self):
        pass

    def add_objectCharacteristicsExtension(self, objectCharacteristicsExtension):
        pass

class Inhibitors(object):
    def __init__(self):
        self.root = ET.Element('inhibitors')
        pass

    def __repr__(self):
        return ET.tostring(self.root, encoding="unicode")

    def set_inhibitorType(self, inhibitorType):
        pass

    def get_inhibitorType(self):
        pass

    def set_inhibitorTarget(self, inhibitorTarget):
        pass

    def add_inhibitorTarget(self, inhibitorTarget):
        pass

    def get_inhibitorTarget(self):
        pass

    def set_inhibitorKey(self, inhibitorKey):
        pass

    def get_inhibitorKey(self):
        pass


class CreatingApplication(object):
    def __init__(self):
        self.root = ET.Element('creatingApplication')
        pass

    def __repr__(self):
        return ET.tostring(self.root, encoding="unicode")

    def set_creatingApplicationName(self, creatingApplicationName):
        pass

    def get_creatingApplicationName(self):
        pass

    def set_creatingApplicationVersion(self, creatingApplicationVersion):
        pass

    def get_creatingApplicationVersion(self):
        pass

    def set_dateCreatedByApplication(self, dateCreatedByApplication):
        pass

    def get_dateCreatedByApplication(self):
        pass

    def set_creatingApplicationExtension(self, creatingApplicationExtension):
        pass

    def get_creatingApplicationExtension(self):
        pass

    def add_creatingApplicationExtension(self, creatingApplicationExtension):
        pass


class Format(object):
    def __init__(self):
        self.root = ET.Element('format')
        pass

    def __repr__(self):
        return ET.tostring(self.root, encoding="unicode")

    def set_formatDesignation(self, formatDesignation):
        pass

    def get_formatDesignation(self):
        pass

    def set_formatRegistry(self, formatRegistry):
        pass

    def get_formatRegistry(self):
        pass

    def set_formatNote(self, formatNote):
        pass

    def get_formatNote(self):
        pass

    def add_formatNote(self, formateNote):
        pass

class FormatDesignation(object):
    def __init__(self):
        self.root = ET.Element('formatDesignation')
        pass

    def __repr__(self):
        return ET.tostring(self.root, encoding="unicode")

    def set_formatName(self, formatName):
        pass

    def get_formatName(self):
        pass

    def set_formatVersion(self, formatVersion):
        pass

    def get_formatVersion(self):
        pass


class FormatRegistry(object):
    def __init__(self):
        self.root = ET.Element('formatRegistry')
        pass

    def __repr__(self):
        return ET.tostring(self.root, encoding="unicode")

    def set_formatRegistryName(self, formatRegistryName):
        pass

    def get_formatRegistryName(self):
        pass

    def set_formatRegistryKey(self, formatRegistryKey):
        pass

    def get_formatRegistryKey(self):
        pass

    def set_formatRegistryRole(self, formatRegistryRole):
        pass

    def get_formatRegistryRole(self):
        pass


class Fixity(object):
    def __init__(self):
        self.root = ET.Element('fixity')
        pass

    def __repr__(self):
        return ET.tostring(self.root, encoding="unicode")

    def set_messageDigestAlgorithm(self, messageDigestAlgorithm):
        pass

    def get_messageDigestAlgorithm(self):
        pass

    def set_messageDigest(self, messageDigest):
        pass

    def get_messageDigest(self):
        pass

    def set_messageDigestOriginator(self, messageDigestOriginator):
        pass

    def get_messageDigestOriginator(self):
        pass


class SignificantProperties(object):
    def __init__(self):
        self.root = ET.Element('significantProperties')
        pass

    def __repr__(self):
        return ET.tostring(self.root, encoding="unicode")

    def set_significantPropertiesType(self, significantPropertiesType):
        pass

    def get_significantPropertiesType(self):
        pass

    def set_significantPropertiesValue(self, significantPropertiesValue):
        pass

    def get_significantPropertiesValue(self):
        pass

    def set_significantPropertiesExtension(self, significantPropertiesExtension):
        pass

    def get_significantPropertiesExtension(self):
        pass

    def add_significantPropertiesExtension(self, significantPropertiesExtension):
        pass


class PreservationLevel(object):
    def __init__(self):
        self.root = ET.Element('preservationLevel')
        pass

    def __repr__(self):
        return ET.tostring(self.root, encoding="unicode")

    def set_preservationLevelType(self, preservationLevelType):
        pass

    def get_preservationLevelType(self):
        pass

    def set_preservationLevelValue(self, preservationLevelValue):
        pass

    def get_preservationLevelValue(self):
        pass

    def set_preservationLevelRole(self, preservationLevelRole):
        pass

    def get_preservationLevelRole(self):
        pass

    def set_preservationLevelRationale(self, preservationLevelRationale):
        pass

    def get_preservationLevelRationale(self):
        pass

    def add_preservationLevelRationale(self, preservationLevelRationale):
        pass

    def set_preservationLevelDateAssigned(self, preservationLevelDateAssigned):
        pass

    def get_preservationLevelDateAssigned(self):
        pass


class PremisEvent(object):
    def __init__(self):
        self.root = ET.Element('event')
        pass

    def __repr__(self):
        return ET.tostring(self.root, encoding="unicode")

    def set_eventIdentifier(self, eventIdentifier):
        pass

    def get_eventIdentifier(self):
        pass

    def set_eventType(self, eventType):
        pass

    def get_eventType(self):
        pass

    def set_eventDateTime(self, eventDateTime):
        pass

    def get_eventDateTime(self):
        pass

    def set_eventOutcomeInformation(self, eventOutcomeInformation):
        pass

    def set_linkingAgentIdentifier(self, linkingAgentIdentifier):
        pass

    def get_linkingAgentIdentifier(self):
        pass

    def add_linkingAgentIdentifier(self, linkingAgentIdentifier):
        pass

    def set_linkingObjectIdentifier(self, linkingObjectIdentifier):
        pass

    def get_linkingObjectIdentifier(self):
        pass

    def add_linkingObjectIdentifier(self, linkingObjectIdentifier):
        pass


class EventOutcomeInformation(object):
    def __init__(self):
        self.root = ET.Element('eventOutcomeInformation')
        pass

    def __repr__(self):
        return ET.tostring(self.root, encoding='unicode')

    def set_eventOutcome(self, eventOutcome):
        pass

    def get_eventOutcome(self):
        pass

    def set_eventDetailInformation(self, eventDetailInformation):
        pass

    def get_eventDetailInformation(self):
        pass

    def add_eventDetailInformation(self, eventDetailInformation):
        pass

    def set_eventOutcomeDetail(self, eventOutcomeDetail):
        pass

    def get_eventOutcomeDetail(self):
        pass


class EventDetailInformation(object):
    def __init__(self):
        self.root = ET.Element('eventDetailInformation')
        pass

    def __repr__(self):
        return ET.tostring(self.root, encoding='unicode')

    def set_eventDetail(self, eventDetail):
        pass

    def get_eventDetail(self):
        pass

    def set_eventDetailExtension(self, eventDetailExtension):
        pass

    def get_eventDetailExtension(self):
        pass

    def add_eventDetailExtension(self, eventDetailExtension):
        pass


class EventOutcomeDetail(object):
    def __init__(self):
        self.root = ET.Element('eventOutcomeDetail')
        pass

    def __repr__(self):
        return ET.tostring(self.root, encoding='unicode')

    def set_eventOutcomeDetailNote(self, eventOutcomeDetailNote):
        pass

    def get_eventOutcomeDetailNote(self):
        pass

    def set_eventOutcomeDetailExtension(self, eventOutcomeDetailExtension):
        pass

    def get_eventOutcomeDetailExtension(self):
        pass

    def add_eventOutcomeDetailExtension(self, eventOutcomeDetailExtension):
        pass


class PremisAgent(object):
    def __init__(self):
        pass
        self.root = ET.Element('entity')

    def __repr__(self):
        return ET.tostring(self.root, encoding="unicode")

    def set_agentIdentifier(self, agentIdentifier):
        pass

    def get_agentIdentifier(self):
        pass

    def add_agentIdentifier(self, agentIdentifier):
        pass

    def set_agentName(self, agentName):
        pass

    def get_agentName(self):
        pass

    def add_agentName(self, agentName):
        pass

    def set_agentType(self, agentType):
        pass

    def get_agentType(self):
        pass

    def set_agentVersion(self, agentVersion):
        pass

    def get_agentVersion(self):
        pass

    def set_agentNote(self, agentNote):
        pass

    def get_agentNote(self):
        pass

    def add_agentNote(self, agentNote):
        pass

    def set_agentExtension(self, agentExtension):
        pass

    def get_agentExtension(self):
        pass

    def add_agentExtension(self, agentExtension):
        pass

    def set_linkingEventIdentifier(self, linkingEventIdentifier):
        pass

    def get_linkingEventIdentifier(self):
        pass

    def add_linkingEventIdentifier(self, linkingEventIdentifier):
        pass

    def set_linkingRightsStatementIdentifier(self, linkingRightsStatementIdentifier):
        pass

    def get_linkingRightsStatementIdentifier(self):
        pass

    def add_linkingRightsStatementIdentifier(self, linkingRightsStatementIdentifier):
        pass

    def set_linkingEnvironmentIdentifier(self, linkingEnvironmentIdentifier):
        pass

    def get_linkingEnvironmentIdentifier(self):
        pass

    def add_linkingEnvironmentIdentifier(self, linkingEnvironmentIdentifier):
        pass


class LinkingEnvironmentIdentifier(object):
    def __init__(self):
        self.root = ET.Element('linkingEnvironmentIdentifier')
        pass

    def __repr__(self):
        return ET.tostring(self.root, encoding='unicode')

    def set_linkingEnvironmentIdentifierType(self, linkingEnvironmentIdentifierType):
        pass

    def get_linkingEnvironmentIdentifierType(self):
        pass

    def set_linkingEnvironmentIdentifierValue(self, linkingEnvironmentIdentifierValue):
        pass

    def get_linkingEnvironmentIdentifierValue(self):
        pass

    def set_linkingEnvironmentRole(self, linkingEnvironmentRole):
        pass

    def get_linkingEnvironmentRole(self):
        pass

    def add_linkingEnvironmentRole(self, linkingEnvironmentRole):
        pass


class LinkingEntityAgentIdentifier(object):
    def __init__(self):
        self.root = ET.Element('agentIdentifier')
        pass

    def __repr__(self):
        return ET.tostring(self.root, encoding="unicode")

    def set_agentIdentifierType(self, agentIdentifierType):
        pass

    def get_agentIdentifierType(self):
        pass

    def set_agentIdentifierValue(self, agentIdentifierValue):
        pass

    def get_agentIdentifierValue(self):
        pass


class PremisRights(object):
    def __init__(self):
        self.root = ET.Element('rights')
        pass

    def __repr__(self):
        return ET.tostring(self.root, encoding="unicode")

    def set_rightsStatement(self, rightsStatement):
        pass

    def get_rightsStatement(self):
        pass

    def add_rightsStatement(self, rightsStatement):
        pass

    def set_rightsExtension(self, rightsExtension):
        pass

    def get_rightsExtension(self):
        pass

    def add_rightsExtension(self, rightsExtension):
        pass


class RightsStatement(object):
    def __init__(self):
        self.root = ET.Element('rightsStatement')
        pass

    def __repr__(self):
        return ET.tostring(self.root, encoding='unicode')

    def set_rightsStatementIdentifier(self, rightsStatementIdentifier):
        pass

    def get_rightsStatementIdentifier(self):
        pass

    def set_rightsBasis(self, rightsBasis):
        pass

    def get_rightsBasis(self):
        pass

    def set_copyrightInformation(self, copyrightInformation):
        pass

    def get_copyrightInformation(self):
        pass

    def set_licenseInformation(self, licenseInformation):
        pass

    def get_licenseInformation(self):
        pass

    def set_statuteInformation(self, statuteInformation):
        pass

    def get_statuteInformation(self):
        pass

    def add_statuteInformation(self, statuteInformation):
        pass

    def set_otherRightsInformation(self, otherRightsInformation):
        pass

    def get_otherRightsInformation(self):
        pass

    def set_rightsGranted(self, rightsGranted):
        pass

    def get_rightsGranted(self):
        pass

    def add_rightsGranted(self, rightsGranted):
        pass

    def set_linkingObjectIdentifier(self, linkingObjectIdentifier):
        pass

    def get_linkingObjectIdentifier(self):
        pass

    def add_linkingObjectIdentifier(self, linkingObjectIdentifier):
        pass

    def set_linkingAgentIdentifier(self, linkingAgentIdentifier):
        pass

    def get_linkingAgentIdentifier(self):
        pass

    def add_linkingAgentIdentifier(self, linkingAgentIdentifier):
        pass


class RightsGranted(object):
    def __init__(self):
        self.root = ET.Element('rightsGranted')
        pass

    def __repr__(self):
        return ET.tostring(self.root, encoding='unicode')

    def set_act(self, act):
        pass

    def get_act(self):
        pass

    def set_restriction(self, restriction):
        pass

    def get_restriction(self):
        pass

    def add_restriction(self, restriction):
        pass

    def set_termOfGrant(self, termOfGrant):
        pass

    def get_termOfGrant(self):
        pass

    def set_termOfRestriction(self, termOfRestriction):
        pass

    def get_termOfRestriction(self):
        pass

    def set_rightsGrantedNote(self, rightsGrantedNote):
        pass

    def get_rightsGrantedNote(self):
        pass

    def add_rightsGrantedNote(self, rightsGrantedNote):
        pass


class TermOfRestriction(object):
    def __init__(self):
        self.root = ET.Element('termOfRestriction')
        pass

    def __repr__(self):
        return ET.tostring(self.root, encoding='unicode')

    def set_startDate(self, startDate):
        pass

    def get_startDate(self):
        pass

    def set_endDate(self, endDate):
        pass

    def get_endDate(self):
        pass


class TermOfGrant(object):
    def __init__(self):
        self.root = ET.Element('termOfGrant')
        pass

    def __repr__(self):
        return ET.tostring(self.root, encoding='unicode')

    def set_startDate(self, startDate):
        pass

    def get_startDate(self):
        pass

    def set_endDate(self, endDate):
        pass

    def get_endDate(self):
        pass


class OtherRightsInformation(object):
    def __init__(self):
        self.root = ET.Element('otherRightsInformation')
        pass

    def __repr__(self):
        return ET.tostring(self.root, encoding='unicode')

    def set_otherRightsDocumentationIdentifier(self, otherRightsDocumentationIdentifier):
        pass

    def get_otherRightsDocumentationIdentifier(self):
        pass

    def set_otherRightsBasis(self, otherRightsBasis):
        pass

    def get_otherRightsBasis(self):
        pass

    def set_otherRightsApplicableDates(self, otherRightsApplicableDates):
        pass

    def get_otherRightsApplicableDates(self):
        pass

    def set_otherRightsNote(self, otherRightsNote):
        pass

    def get_otherRightsNote(self):
        pass

    def add_otherRightsNote(self):
        pass


class OtherRightsApplicableDates(object):
    def __init__(self):
        self.root = ET.Element('otherRightsApplicableDates')
        pass

    def __repr__(self):
        return ET.tostring(self.root, encoding='unicode')

    def set_startDate(self, startDate):
        pass

    def get_startDate(self):
        pass

    def set_endDate(self, endDate):
        pass

    def get_endDate(self):
        pass


class OtherRightsDocumentationIdentifier(object):
    def __init__(self):
        self.root = ET.Element('otherRightsDocumentationIdentifier')
        pass

    def __repr__(self):
        return ET.tostring(self.root, encoding='unicode')

    def set_otherRightsDocumentationIdentifierType(self, otherRightsDocumentationIdentifierType):
        pass

    def get_otherRightsDocumentationIdentifierType(self):
        pass

    def set_otherRightsDocumentationIdentifierValue(self, otherRightsDocumentationIdentifierValue):
        pass

    def set_otherRightsDocumentationRole(self, otherRightsDocumentationRole):
        pass

    def get_otherRightsDocumentationRole(self):
        pass


class StatuteInformation(object):
    def __init__(self):
        self.root = ET.Element('statuteInformation')
        pass

    def __repr__(self):
        return ET.tostring(self.root, encoding='unicode')

    def set_statuteJurisdiction(self, statuteJurisdiction):
        pass

    def get_statuteJurisdiction(self):
        pass

    def set_statuteCitation(self, statuteCitation):
        pass

    def get_statuteCitation(self):
        pass

    def set_statuteInformationDeterminationDate(self, statuteInformationDeterminationDate):
        pass

    def get_statuteInformationDeterminationDate(self):
        pass

    def set_statuteNote(self, statuteNote):
        pass

    def get_statuteNote(self):
        pass

    def add_statuteNote(self, statuteNote):
        pass

    def set_statuteDocumentationIdentifier(self, statuteDocumentationIdentifier):
        pass

    def get_statuteDocumentationIdentifier(self):
        pass

    def add_statuteDocumentationIdentifier(self, statuteDocumentationIdentifier):
        pass

    def set_statuteApplicableDates(self, statuteApplicableDates):
        pass

    def get_statuteApplicableDates(self):
        pass


class StatuteApplicableDates(object):
    def __init__(self):
        self.root = ET.Element('statuteApplicableDates')
        pass

    def __repr__(self):
        return ET.tostring(self.root, encoding='unicde')

    def set_startDate(self, startDate):
        pass

    def get_startDate(self):
        pass

    def set_endDate(self, endDate):
        pass

    def get_endDate(self):
        pass


class StatuteDocumentationIdentifier(object):
    def __init__(self):
        self.root = ET.Element('statuteDocumentationIdentifier')
        pass

    def __repr__(self):
        return ET.tostring(self.root, encoding='unicode')

    def set_statuteDocumentationIdentifierType(self, statuteDocumentationIdentifierType):
        pass

    def get_statuteDocumentationIdentifierType(self):
        pass

    def set_statuteDocumentationIdentifierValue(self, statuteDocumentationIdentifierValue):
        pass

    def get_statuteDocumentationIdentifierValue(self):
        pass

    def set_statuteDocumentationRole(self, statuteDocumentationRole):
        pass

    def get_statuteDocumentationRole(self):
        pass


class LicenseInformation(object):
    def __init__(self):
        self.root = ET.Element('licenseInformation')
        pass

    def __repr__(self):
        return ET.tostring(self.root, encoding='unicode')

    def set_licenseDocumentationIdentifier(self, licenseDocumentationIdentifier):
        pass

    def get_licenseDocumentationIdentifier(self):
        pass

    def add_licenseDocumentationIdentifier(self, licenseDocumentationIdentifier):
        pass

    def set_licenseTerms(self, licenseTerms):
        pass

    def get_licenseTerms(self):
        pass

    def set_licenseNote(self, licenseNote):
        pass

    def get_licenseNote(self):
        pass

    def set_licenseApplicableDates(self, licenseApplicationDates):
        pass

    def get_licenseApplicableDates(self):
        pass


class LicenseApplicableDates(object):
    def __init__(self):
        self.root = ET.Element('licenseApplicableDates')
        pass

    def __repr__(self):
        return ET.tostring(self.root, encoding='unicode')

    def set_startDate(self, startDate):
        pass

    def get_startDate(self):
        pass

    def set_endDate(self, endDate):
        pass

    def get_endDate(self, endDate):
        pass


class LicenseDocumentationIdentifier(object):
    def __init__(self):
        self.root = ET.Element('licenseInformation')
        pass

    def __repr__(self):
        return ET.tostring(self.root, encoding='unicode')

    def set_licenseDocumentationIdentifierType(self, licenseDocumentationIdentifierType):
        pass

    def get_licenseDocumentationIdentifierType(self):
        pass

    def set_licenseDocumentationIdentifierValue(self, licenseDocumentationIdentifierValue):
        pass

    def get_licenseDocumentationIdentifierValue(self):
        pass

    def set_licenseDocumentationRole(self, licenseDocumentationRole):
        pass

    def get_licenseDocumentationRole(self):
        pass


class CopyrightInformation(object):
    def __init__(self):
        self.root = ET.Element('copyrightInformation')
        pass

    def __repr__(self):
        return ET.tostring(self.root, encoding='unicode')

    def set_copyrightStatus(self, copyrightStatus):
        pass

    def get_copyrightStatus(self):
        pass

    def set_copyrightJurisdiction(self, copyrightJurisdiction):
        pass

    def get_copyrightJurisdiction(self):
        pass

    def set_copyrightStatusDeterminationDate(self, copyrightStatusDeterminationDate):
        pass

    def get_copyrightStatusDeterminationDate(self):
        pass

    def set_copyrightNote(self, copyrightNote):
        pass

    def get_copyrightNote(self):
        pass

    def add_copyrightNote(self, copyrightNote):
        pass

    def set_copyrightDocumentationIdentifier(self, copyrightDocumentationIdentifier):
        pass

    def get_copyrightDocumentationIdentifier(self):
        pass

    def add_copyrightDocumentationIdentifier(self, copyrightDocumentationIdentifier):
        pass

    def set_copyrightApplicableDates(self, copyrightApplicableDates):
        pass

    def get_copyrightApplicableDates(self):
        pass


class CopyrightApplicableDates(object):
    def __init__(self):
        self.root = ET.Element('copyrightApplicableDates')
        pass

    def __repr__(self):
        return ET.tostring(self.root, encoding='unicode')

    def set_startDate(self, startDate):
        pass

    def get_startDate(self):
        pass

    def set_endDate(self, endDate):
        pass

    def get_endDate(self):
        pass


class CopyrightDocumentationIdentifier(object):
    def __init__(self):
        self.root = ET.Element('copyrightDocumentationIdentifier')
        pass

    def __repr__(self):
        return ET.tostring(self.root, encoding='unicode')

    def set_copyrightDocumentationIdentifierType(self, copyrightDocumentationIdentifierType):
        pass

    def get_copyrightDocumentationIdentifierType(self):
        pass

    def set_copyrightDocumentationIdentifierValue(self, copyrightDocumentationIdentifierValue):
        pass

    def get_copyrightDocumentationIdentifierValue(self):
        pass

    def set_copyrightDocumentationRole(self, copyrightDocumentationRole):
        pass

    def get_copyrightDocumentationRole(self):
        pass


class RightsStatementIdentifier(object):
    def __init__(self):
        self.root = ET.Element('rightsStatementIdentifier')
        pass

    def __repr__(self):
        return ET.tostring(self.root, encoding='unicode')

    def set_rightsStatementIdentifierType(self, rightsStatementIdentifierType):
        pass

    def get_rightsStatementIdentifierType(self):
        pass

    def set_rightsStatementIdentifierValue(self, rightsStatementIdentifierValue):
        pass

    def get_rightsStatementIdentifierValue(self):
        pass
