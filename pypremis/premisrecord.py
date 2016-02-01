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
    def __init__(self, objectIdentifierType, objectIdentifierValue,
                 objectCategory, ):
        self.root = ET.element('object')
        pass

    def __repr__(self):
        return ET.tostring(self.root, encoding="unicode")

    def set_objectIdentifierType(self, objectIdentifierType):
        pass

    def get_objectIdentifierType(self):
        pass

    def set_objectIdentifierValue(self, objectIdentifierValue):
        pass

    def get_objectIdentifierValue(self):
        pass

    def set_objectCategory(self, objectCategory):
        pass

    def get_objectCategory(self):
        pass

    def set_preservationLevel(self, preservationLevel):
        pass

    def get_preservationLevel(self):
        pass

    def set_significantProperties(self, significantProperties):
        pass

    def get_significantProperties(self):
        pass

    def set_objectCharacteristics(self, objectCharacteristics):
        pass

    def get_objectCharacteristics(self):
        pass

    def set_originalName(self, originalName):
        pass

    def get_originalName(self):
        pass

    def set_storage(self, storage):
        pass

    def get_storage(self):
        pass

    def set_signatureInformation(self, signatureInformation):
        pass

    def get_signatureInformation(self):
        pass

    def set_environmentFunction(self, environmentFunction):
        pass

    def get_environmentFunction(self, environmentFunction):
        pass

    def set_environmentDesignation(self, environmentDesignation):
        pass

    def get_environmentDesignation(self):
        pass

    def set_environmentRegistry(self, environmentRegistry):
        pass

    def get_environmentRegistry(self):
        pass

    def set_environmentExtension(self, environmentExtension):
        pass

    def get_environmentExtension(self):
        pass

    def set_relationship(self, relationship):
        pass

    def get_relationship(self):
        pass

    def set_linkingEventIdentifier(self, linkingEventIdentifier):
        pass

    def get_linkingEventIdentifier(self):
        pass

    def set_linkingRightsStatementIdentifier(self, linkingRightsStatementIdentifier):
        pass

    def get_linkingRightsStatementIdentifier(self):
        pass


class ObjectLinkingEventIdentifier(object):
    def __init__(self):
        self.root = ET.element('linkingEventIdentifier')
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


class ObjectLinkingRightsStatementIdentifier(object):
    def __init__(self):
        self.root = ET.element('linkingRightsStatementIdentifier')
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


class ObjectRelationship(object):
    def __init__(self):
        self.root = ET.element('relationship')
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

    def set_relatedEventIdentifier(self, relatedEventIdentifer):
        pass

    def get_relatedEventIdentifer(self):
        pass

    def set_relatedEnvironmentPurpose(self, relatedEnvironmentPurpose):
        pass

    def get_relatedEnvironmentPurpose(self):
        pass

    def set_relatedEnvironmentCharacteristic(self, relatedEnvironmentCharacteristic):
        pass

    def get_relatedEnvironmentCharacteristic(self):
        pass


class ObjectRelationshipRelatedEventIdentifer(object):
    def __init__(self):
        self.root = ET.element('relatedEventIdentifier')
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


class ObjectRelationshipRelatedObjectIdentifier(object):
    def __init__(self):
        self.root = ET.element('relatedObjectIdentifier')
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


class ObjectEnvironmentRegistry(object):
    def __init__(self):
        self.root = ET.element('environmentRegistry')
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


class ObjectEnvironmentDesignation(object):
    def __init__(self):
        self.root = ET.element('environmentDesignation')
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

    def set_environmentDesignationExtension(self, environmentDesignationExtension):
        pass

    def get_environmentDesignationExtension(self):
        pass


class ObjectEnvironmentFunction(object):
    def __init__(self):
        self.root = ET.element('environmentFunction')
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


class ObjectSignatureInformation(object):
    def __init__(self):
        self.root = ET.element('signatureInformation')
        pass

    def __repr__(self):
        return ET.tostring(self.root, encoding="unicode")

    def set_signature(self, signature):
        pass

    def get_signature(self):
        pass

    def set_signatureInformationExtension(self, signatureInformationExtension):
        pass

    def get_signatureInformationExtension(self):
        pass


class ObjectSignatureInformationSignature(object):
    def __init__(self):
        self.root = ET.element('signature')
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

    def get_signatureProperties(self):
        pass

    def set_keyInformation(self, keyInformation):
        pass

    def get_keyInformation(self):
        pass


class ObjectStorage(object):
    def __init__(self):
        self.root = ET.element('storage')
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


class ObjectStorageContentLocation(object):
    def __init__(self):
        self.root = ET.element('contentLocation')
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
        self.root = ET.element('objectCharacteristics')
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

    def set_size(self, size):
        pass

    def get_size(self):
        pass

    def set_format(self, format):
        pass

    def get_format(self):
        pass

    def set_creatingApplication(self, creationApplication):
        pass

    def get_creatingApplication(self):
        pass

    def set_inhibitors(self, inhibitors):
        pass

    def get_inhibitors(self):
        pass

    def set_objectCharacteristicsExtension(self, objectCharacteristicsExtension):
        pass

    def get_objectCharacteristicsExtension(self):
        pass


class ObjectCharacteristicsInhibitors(object):
    def __init__(self):
        self.root = ET.element('inhibitors')
        pass

    def __repr__(self):
        return ET.tostring(self.root, encoding="unicode")

    def set_inhibitorType(self, inhibitorType):
        pass

    def get_inhibitorType(self):
        pass

    def set_inhibitorTarget(self, inhibitorTarget):
        pass

    def get_inhibitorTarget(self):
        pass

    def set_inhibitorKey(self, inhibitorKey):
        pass

    def get_inhibitorKey(self):
        pass


class ObjectCharacteristicsCreatingApplication(object):
    def __init__(self):
        self.root = ET.element('creatingApplication')
        pass

    def __repr__(self):
        return ET.tostring(self.root, encoding="unicode")

    def set_creatingApplicationName(self, creatingApplicationName):
        pass

    def get_creatingApplicationName(self, creatingApplicationName):
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


class ObjectCharacteristicsFormat(object):
    def __init__(self):
        self.root = ET.element('format')
        pass

    def __repr__(self):
        return ET.tostring(self.root, encoding="unicode")

    def set_formatDesignation(self, formatDesignation):
        pass

    def get_formatDesignation(self):
        pass

    def set_formatRegistry(self):
        pass

    def get_formatRegistry(self):
        pass

    def set_formatNote(self, formatNote):
        pass

    def get_formatNote(self):
        pass


class ObjectCharacteristicsFormatDesignation(object):
    def __init__(self):
        self.root = ET.element('formatDesignation')
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


class ObjectCharacteristicsFormatRegistry(object):
    def __init__(self):
        self.root = ET.element('formatRegistry')
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


class ObjectCharacteristicsFixity(object):
    def __init__(self):
        self.root = ET.element('fixity')
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


class ObjectSignificantProperties(object):
    def __init__(self):
        self.root = ET.element('significantProperties')
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


class ObjectPreservationLevel(object):
    def __init__(self):
        self.root = ET.element('preservationLevel')
        pass

    def __repr__(self):
        return ET.tostring(self.root, encoding="unicode")

    def set_preservationLevelType(self, preservationLevelType):
        pass

    def get_preservationLevelType(self):
        pass

    def set_preservationLevelValue(self, preservationLevelValue):
        pass

    def get_preservationLevelVale(self):
        pass

    def set_preservationLevelRole(self, preservationLevelRole):
        pass

    def get_preservationLevelRole(self):
        pass

    def set_preservationLevelRationale(self, preservationLevelRationale):
        pass

    def get_preservationLevelRationale(self):
        pass

    def set_preservationLevelDateAssigned(self, preservationLevelDateAssigned):
        pass


class PremisEvent(object):
    def __init__(self):
        self.root = ET.element('event')
        pass

    def __repr__(self):
        return ET.tostring(self.root, encoding="unicode")


class PremisEntity(object):
    def __init__(self):
        pass
        self.root = ET.element('entity')

    def __repr__(self):
        return ET.tostring(self.root, encoding="unicode")


class PremisRights(object):
    def __init__(self):
        pass
        self.root = ET.element('rights')

    def __repr__(self):
        return ET.tostring(self.root, encoding="unicode")
