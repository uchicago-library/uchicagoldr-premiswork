import xml.etree.ElementTree as ET

from pypremis.lib import PremisNode


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

    def add_agent(self, entity):
        pass

    def get_agent(self, entityID):
        pass

    def get_agents(self):
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


class Object(PremisNode):
    def __init__(self, objectIdentifier, objectCategory, objectCharacteristics):
        PremisNode.__init__(self, 'object')
        self.set_objectIdentifier(objectIdentifier)
        self.set_objectCategory(objectCategory)
        self.set_objectCharacteristics(objectCharacteristics)

    def set_objectIdentifier(self, objectIdentifier):
        self._set_field('objectIdentifier', self._listify(objectIdentifier))

    def get_objectIdentifier(self, index=None):
        return self._list_getter('objectIdentifier', index)

    def add_objectIdentifier(self, objectIdentifier):
        self._add_to_field('objectIdentifier', objectIdentifier)

    def set_objectCategory(self, objectCategory):
        self._set_field('objectCategory', objectCategory)

    def get_objectCategory(self):
        return self._get_field('objectCategory')

    def set_preservationLevel(self, preservationLevel):
        self._set_field('preservationLevel', self._listify(preservationLevel))

    def get_preservationLevel(self, index=None):
        return self._list_getter('preservationLevel', index)

    def add_preservationLevel(self, preservationLevel):
        self._add_to_field('preservationLevel', preservationLevel)

    def set_significantProperties(self, significantProperties):
        self._set_field('significantProperties', self._listify(significantProperties))

    def get_significantProperties(self, index=None):
        return self._list_getter('significantProperties', index)

    def add_significantProperties(self, significantProperties):
        self._add_to_field('significantProperties', significantProperties)

    def set_objectCharacteristics(self, objectCharacteristics):
        self._set_field('objectCharacteristics', self._listify(objectCharacteristics))

    def get_objectCharacteristics(self, index=None):
        return self._list_getter('objectCharacteristics', index)

    def add_objectCharacteristics(self, objectCharacteristics):
        self._add_to_field('objectCharacteristics', objectCharacteristics)

    def set_originalName(self, originalName):
        self._set_field('originalName', originalName)

    def get_originalName(self):
        return self._get_field('originalName')

    def set_storage(self, storage):
        self._set_field('storage', self._listify(storage))

    def get_storage(self, index=None):
        return self._list_getter('storage', index)

    def add_storage(self, storage):
        self._add_to_field('storage', storage)

    def set_signatureInformation(self, signatureInformation):
        self._set_field('signatureInformation', self._listify(signatureInformation))

    def get_signatureInformation(self, index=None):
        return self._list_getter('signatureInformation', index)

    def add_signatureInformation(self, signatureInformation):
        self._add_to_field('signatureInformation', signatureInformation)

    def set_environmentFunction(self, environmentFunction):
        self._set_field('environmentFunction', self._listify(environmentFunction))

    def get_environmentFunction(self, index=None):
        return self._list_getter('environmentFunction', index)

    def add_environmentFunction(self, environmentFunction):
        self._add_to_field('environmentFunction', environmentFunction)

    def set_environmentDesignation(self, environmentDesignation):
        self._set_field('environmentDesignation', self._listify(environmentDesignation))

    def get_environmentDesignation(self, index=None):
        return self._list_getter('environmentDesignation', index)

    def add_environmentDesignation(self, environmentDesignation):
        self._add_to_field('environmentDesignation', environmentDesignation)

    def set_environmentRegistry(self, environmentRegistry):
        self._set_field('environmentRegistry', self._listify(environmentRegistry))

    def get_environmentRegistry(self, index=None):
        return self._list_getter('environmentRegistry', index)

    def add_environmentRegistry(self, environmentRegistry):
        self._add_to_field('environmentRegistry', environmentRegistry)

    def set_environmentExtension(self, environmentExtension):
        self._set_field('environmentExtension', self._listify(environmentExtension))

    def get_environmentExtension(self, index=None):
        return self._list_getter('environmentExtension', index)

    def add_environmentExtension(self, environmentExtension):
        self._add_to_field('environmentExtension', environmentExtension)

    def set_relationship(self, relationship):
        self._set_field('relationship', self._listify(relationship))

    def get_relationship(self, index=None):
        return self._list_getter('relationship', index)

    def add_relationship(self, relationship):
        self._add_to_field('relationship', relationship)

    def set_linkingEventIdentifier(self, linkingEventIdentifier):
        self._set_field('linkingEventIdentifier', self._listify(linkingEventIdentifier))

    def get_linkingEventIdentifier(self, index=None):
        return self._list_getter('linkingEventIdentifier', index)

    def add_linkingEventIdentifier(self, linkingEventIdentifier):
        self._add_to_field('linkingEventIdentifier', linkingEventIdentifier)

    def set_linkingRightsStatementIdentifier(self, linkingRightsStatementIdentifier):
        self._set_field('linkingRightsStatementIdentifier', self._listify(linkingRightsStatementIdentifier))

    def get_linkingRightsStatementIdentifier(self, index=None):
        return self._list_getter('linkingRightsStatementIdentifier', index)

    def add_linkingRightsStatementIdentifier(self, linkingRightsStatementIdentifier):
        self._add_to_field('linkingRightsStatementIdentifier', linkingRightsStatementIdentifier)


class ObjectIdentifier(PremisNode):
    def __init__(self, objectIdentifierType, objectIdentifierValue):
        PremisNode.__init__(self, 'objectIdentifier')
        self.set_objectIdentifierType(objectIdentifierType)
        self.set_objectIdentifierValue(objectIdentifierValue)

    def set_objectIdentifierType(self, objectIdentifierType):
        self._set_field('objectIdentifierType', objectIdentifierType)

    def get_objectIdentifierType(self):
        return self._get_field('objectIdentifierType')

    def set_objectIdentifierValue(self, objectIdentifierValue):
        self._set_field('objectIdentifierValue', objectIdentifierValue)

    def get_objectIdentifierValue(self):
        return self._get_field('objectIdentifierValue')


class LinkingObjectIdentifier(PremisNode):
    def __init__(self, linkingObjectIdentifierType, linkingObjectIdentifierValue):
        PremisNode.__init__(self, 'linkingObjectIdentifier')
        self.set_linkingObjectIdentifierType(linkingObjectIdentifierType)
        self.set_linkingObjectIdentifierValue(linkingObjectIdentifierValue)

    def set_linkingObjectIdentifierType(self, linkingObjectIdentifierType):
        self._set_field('linkingObjectIdentifierType', linkingObjectIdentifierType)

    def get_linkingObjectIdentifierType(self):
        return self._get_field('linkingObjectIdentifierType')

    def set_linkingObjectIdentifierValue(self, linkingObjectIdentifierValue):
        self._set_field('linkingObjectIdentifierValue', linkingObjectIdentifierValue)

    def get_linkingObjectIdentifierValue(self):
        return self._get_field('linkingObjectIdentifierValue')

    def set_linkingObjectRole(self, linkingObjectRole):
        self._set_field('linkingObjectRole', self._listify(linkingObjectRole))

    def get_linkingObjectRole(self, index=None):
        return self._list_getter('linkingObjectRole', index)

    def add_linkingObjectRole(self, linkingObjectRole):
        self._add_to_field('linkingObjectRole', linkingObjectRole)


class EventIdentifier(PremisNode):
    def __init__(self, eventIdentifierType, eventIdentifierValue):
        PremisNode.__init__(self, 'eventIdentifier')
        self.set_eventIdentifierType(eventIdentifierType)
        self.set_eventIdentifierValue(eventIdentifierValue)

    def set_eventIdentifierType(self, eventIdentifierType):
        self._set_field('eventIdentifierType', eventIdentifierType)

    def get_eventIdentifierType(self):
        return self._get_field('eventIdentifierType')

    def set_eventIdentifierValue(self, eventIdentifierValue):
        self._set_field('eventIdentifierValue', eventIdentifierValue)

    def get_eventIdentifierValue(self):
        return self._get_field('eventIdentifierValue')


class LinkingEventIdentifier(PremisNode):
    def __init__(self, linkingEventIdentiferType, linkingEventIdentifierValue):
        PremisNode.__init__(self, 'linkingEventIdentifier')
        self.set_linkingEventIdentifierType(linkingEventIdentiferType)
        self.set_linkingEventIdentifierValue(linkingEventIdentifierValue)

    def set_linkingEventIdentifierType(self, linkingEventIdentifierType):
        self._set_field('linkingEventIdentifierType', linkingEventIdentifierType)

    def get_linkingEventIdentifierType(self):
        return self._get_field('linkingEventIdentifierType')

    def set_linkingEventIdentifierValue(self, linkingEventIdentifierValue):
        self._set_field('linkingEventIdentifierValue', linkingEventIdentifierValue)

    def get_linkingEventIdentifierValue(self):
        return self._get_field('linkingEventIdentifierValue')


class LinkingRightsStatementIdentifier(PremisNode):
    def __init__(self, linkingRightsStatementIdentifierType, linkingRightsStatementIdentifierValue):
        PremisNode.__init__(self, 'linkingRightsStatementIdentifier')
        self.set_linkingRightsStatementIdentifierType(linkingRightsStatementIdentifierType)
        self.set_linkingRightsStatementIdentifierValue(linkingRightsStatementIdentifierValue)

    def set_linkingRightsStatementIdentifierType(self, linkingRightsStatementIdentifierType):
        self._set_field('linkingRightsStatementIdentifierType', linkingRightsStatementIdentifierType)

    def get_linkingRightsStatementIdentifierType(self):
        return self._get_field('linkingRightsStatementIdentifierType')

    def set_linkingRightsStatementIdentifierValue(self, linkingRightsStatementIdentifierValue):
        self._set_field('linkingRightsStatementIdentifierValue', linkingRightsStatementIdentifierValue)

    def get_linkingRightsStatementIdentifierValue(self):
        return self._get_field('linkingRightsStatementIdentifierValue')


class Relationship(PremisNode):
    def __init__(self, relationshipType, relationshipSubType, relatedObjectIdentifier):
        PremisNode.__init__(self, 'relationship')
        self.set_relationshipType(relationshipType)
        self.set_relationshipSubType(relationshipSubType)
        self.set_relatedObjectIdentifier(relatedObjectIdentifier)

    def set_relationshipType(self, relationshipType):
        self._set_field('relationshipType', relationshipType)

    def get_relationshipType(self):
        return self._get_field('relationshipType')

    def set_relationshipSubType(self, relationshipSubType):
        self._set_field('relationshipSubType', relationshipSubType)

    def get_relationshipSubType(self):
        return self._get_field('relationshipSubType')

    def set_relatedObjectIdentifier(self, relatedObjectIdentifier):
        self._set_field('relatedObjectIdentifier', self._listify(relatedObjectIdentifier))

    def get_relatedObjectIdentifier(self, index=None):
        return self._list_getter('relatedObjectIdentifier', index)

    def add_relatedObjectIdentifier(self, relatedObjectIdentifier):
        self._add_to_field('relatedObjectIdentifier', relatedObjectIdentifier)

    def set_relatedEventIdentifier(self, relatedEventIdentifier):
        self._set_field('relatedEventIdentifier', self._listify(relatedEventIdentifier))

    def get_relatedEventIdentifier(self, index=None):
        return self._list_getter('relatedEventIdentifier', index)

    def add_relatedEventIdentifier(self, relatedEventIdentifier):
        self._add_to_field('relatedEventIdentifier', relatedEventIdentifier)

    def set_relatedEnvironmentPurpose(self, relatedEnvironmentPurpose):
        self._set_field('relatedEnvironmentPurpose', self._listify(relatedEnvironmentPurpose))

    def get_relatedEnvironmentPurpose(self, index=None):
        return self._list_getter('relatedEnvironmentPurpose', index)

    def add_relatedEnvironmentPurpose(self, relatedEnvironmentPurpose):
        self._add_to_field('relatedEnvironmentPurpose', relatedEnvironmentPurpose)

    def set_relatedEnvironmentCharacteristic(self, relatedEnvironmentCharacteristic):
        self._set_field('relatedEnvironmentCharacteristic', relatedEnvironmentCharacteristic)

    def get_relatedEnvironmentCharacteristic(self):
        return self._get_field('relatedEnvironmentCharacteristic')


class RelatedEventIdentifier(PremisNode):
    def __init__(self, relatedEventIdentifierType, relatedEventIdentifierValue):
        PremisNode.__init__(self, 'relatedEventIdentifier')
        self.set_relatedEventIdentifierType(relatedEventIdentifierType)
        self.set_relatedEventIdentifierValue(relatedEventIdentifierValue)

    def set_relatedEventIdentifierType(self, relatedEventIdentifierType):
        self._set_field('relatedEventIdentifierType', relatedEventIdentifierType)

    def get_relatedEventIdentifierType(self):
        return self._get_field('relatedEventIdentifierType')

    def set_relatedEventIdentifierValue(self, relatedEventIdentifierValue):
        self._set_field('relatedEventIdentifierValue', relatedEventIdentifierValue)

    def get_relatedEventIdentifierValue(self):
        return self._get_field('relatedEventIdentifierValue')

    def set_relatedEventSequence(self, relatedEventSequence):
        self._set_field('relatedEventSequence', relatedEventSequence)

    def get_relatedEventSequence(self):
        return self._get_field('relatedEventSequence')


class RelatedObjectIdentifier(PremisNode):
    def __init__(self, relatedObjectIdentifierType, relatedObjectIdentifierValue):
        PremisNode.__init__(self, 'relatedObjectIdentifier')
        self.set_relatedObjectIdentifierType(relatedObjectIdentifierType)
        self.set_relatedObjectIdentifierValue(relatedObjectIdentifierValue)

    def set_relatedObjectIdentifierType(self, relatedObjectIdentifierType):
        self._set_field('relatedObjectIdentifierType', relatedObjectIdentifierType)

    def get_relatedObjectIdentifierType(self):
        return self._get_field('relatedObjectIdentifierType')

    def set_relatedObjectIdentifierValue(self, relatedObjectIdentifierValue):
        self._set_field('relatedObjectIdentifierValue', relatedObjectIdentifierValue)

    def get_relatedObjectIdentifierValue(self):
        return self._get_field('relatedObjectIdentifierValue')

    def set_relatedObjectSequence(self, relatedObjectSequence):
        self._set_field('relatedObjectSequence', relatedObjectSequence)

    def get_relatedObjectSequence(self):
        return self._get_field('relatedObjectSequence')


class EnvironmentRegistry(PremisNode):
    def __init__(self, environmentRegistryName, environmentRegistryKey):
        PremisNode.__init__(self, 'environmentRegistry')
        self.set_environmentRegistryName(environmentRegistryName)
        self.set_environmentRegistryKey(environmentRegistryKey)

    def set_environmentRegistryName(self, environmentRegistryName):
        self._set_field('environmentRegistryName', environmentRegistryName)

    def get_environmentRegistryName(self):
        return self._get_field('environmentRegistryName')

    def set_environmentRegistryKey(self, environmentRegistryKey):
        self._set_field('environmentRegistryKey', environmentRegistryKey)

    def get_environmentRegistryKey(self):
        return self._get_field('environmentRegistryKey')

    def set_environmentRegistryRole(self, environmentRegistryRole):
        self._set_field('environmentRegistryRole', environmentRegistryRole)

    def get_environmentRegistryRole(self):
        return self._get_field('environmentRegistryRole')


class EnvironmentDesignation(PremisNode):
    def __init__(self, environmentName):
        PremisNode.__init__(self, 'environmentDesignation')
        self.set_environmentName(environmentName)

    def set_environmentName(self, environmentName):
        self._set_field('environmentName', environmentName)

    def get_environmentName(self):
        return self._get_field('environmentName')

    def set_environmentVersion(self, environmentVersion):
        self._set_field('environmentVersion', environmentVersion)

    def get_environmentVersion(self):
        return self._get_field('environmentVersion')

    def set_environmentOrigin(self, environmentOrigin):
        self._set_field('environmentOrigin', environmentOrigin)

    def get_environmentOrigin(self):
        return self._get_field('environmentOrigin')

    def set_environmentDesignationNote(self, environmentDesignationNote):
        self._set_field('environmentDesignationNote', self._listify(environmentDesignationNote))

    def get_environmentDesignationNote(self, index=None):
        return self._list_getter('environmentDesignationNote', index)

    def add_environmentDesignationNote(self, environmentDesignationNote):
        self._add_to_field('environmentDesignationNote', environmentDesignationNote)

    def set_environmentDesignationExtension(self, environmentDesignationExtension):
        self._set_field('environmentDesignationExtension', self._listify(environmentDesignationExtension))

    def get_environmentDesignationExtension(self, index=None):
        return self._list_getter('environmentDesignationExtension', index)

    def add_environmentDesignationExtension(self, environmentDesignationExtension):
        self._add_to_field('environmentDesignationExtension', environmentDesignationExtension)


class EnvironmentFunction(PremisNode):
    def __init__(self, environmentFunctionType, environmentFunctionLevel):
        PremisNode.__init__(self, 'environmentFunction')
        self.set_environmentFunctionType(environmentFunctionType)
        self.set_environmentFunctionLevel(environmentFunctionLevel)

    def set_environmentFunctionType(self, environmentFunctionType):
        self._set_field('environmentFunctionType', environmentFunctionType)

    def get_environmentFunctionType(self):
        return self._get_field('environmentFunctionType')

    def set_environmentFunctionLevel(self, environmentFunctionLevel):
        self._set_field('environmentFunctionLevel', environmentFunctionLevel)

    def get_environmentFunctionLevel(self):
        return self._get_field('environmentFunctionLevel')


class SignatureInformation(PremisNode):
    def __init__(self):
        PremisNode.__init__(self, 'signatureInformation')

    def set_signature(self, signature):
        self._set_field('signature', self._listify(signature))

    def get_signature(self, index=None):
        return self._list_getter('signature', index)

    def add_signature(self, signature):
        self._add_to_field('signature', signature)

    def set_signatureInformationExtension(self, signatureInformationExtension):
        self._set_field('signatureInformationExtension', self._listify(signatureInformationExtension))

    def get_signatureInformationExtension(self, index=None):
        return self._list_getter('signatureInformationExtension', index)

    def add_signatureInformationExtension(self, signatureInformationExtension):
        self._add_to_field('signatureInformationExtension', signatureInformationExtension)


class Signature(PremisNode):
    def __init__(self, signatureEncoding, signatureMethod, signatureValue, signatureValidationRules):
        PremisNode.__init__(self, 'signature')
        self.set_signatureEncoding(signatureEncoding)
        self.set_signatureMethod(signatureMethod)
        self.set_signatureValue(signatureValue)
        self.set_signatureValidationRules(signatureValidationRules)

    def set_signatureEncoding(self, signatureEncoding):
        self._set_field('signatureEncoding', signatureEncoding)

    def get_signatureEncoding(self):
        return self._get_field('signatureEncoding')

    def set_signer(self, signer):
        self._set_field('signer', signer)

    def get_signer(self):
        return self._get_field('signer')

    def set_signatureMethod(self, signatureMethod):
        self._set_field('signatureMethod', signatureMethod)

    def get_signatureMethod(self):
        return self._get_field('signatureMethod')

    def set_signatureValue(self, signatureValue):
        self._set_field('signatureValue', signatureValue)

    def get_signatureValue(self):
        return self._get_field('signatureValue')

    def set_signatureValidationRules(self, signatureValidationRules):
        self._set_field('signatureValidationRules', signatureValidationRules)

    def get_signatureValidationRules(self):
        return self._get_field('signatureValidationRules')

    def set_signatureProperties(self, signatureProperties):
        self._set_field('signatureProperties', self._listify(signatureProperties))

    def add_signatureProperties(self, signatureProperties):
        self._add_to_field('signatureProperties', signatureProperties)

    def get_signatureProperties(self, index=None):
        return self._list_getter('signatureProperties', index)

    def set_keyInformation(self, keyInformation):
        self._set_field('keyInformation', keyInformation)

    def get_keyInformation(self):
        return self._get_field('keyInformation')


class Storage(PremisNode):
    def __init__(self):
        PremisNode.__init__(self, 'storage')

    def set_contentLocation(self, contentLocation):
        self._set_field('contentLocation', contentLocation)

    def get_contentLocation(self):
        return self._get_field('contentLocation')

    def set_storageMedium(self, storageMedium):
        self._set_field('storageMedium', storageMedium)

    def get_storageMedium(self):
        return self._get_field('storageMedium')
        pass


class ContentLocation(PremisNode):
    def __init__(self, contentLocationType, contentLocationValue):
        PremisNode.__init__(self, 'contentLocation')
        self.set_contentLocationType(contentLocationType)
        self.set_contentLocationValue(contentLocationValue)

    def set_contentLocationType(self, contentLocationType):
        self._set_field('contentLocationType', contentLocationType)

    def get_contentLocationType(self):
        return self._get_field('contentLocationType')

    def set_contentLocationValue(self, contentLocationValue):
        self._set_field('contentLocationValue', contentLocationValue)

    def get_contentLocationValue(self):
        return self._get_field('contentLocationValue')


class ObjectCharacteristics(PremisNode):
    def __init__(self, format):
        PremisNode.__init__(self, 'objectCharacteristics')
        self.set_format(format)

    def set_compositionLevel(self, compositionLevel):
        self._set_field('compositionLevel', compositionLevel)

    def get_compositionLevel(self):
        return self._get_field('compositionLevel')

    def set_fixity(self, fixity):
        self._set_field('fixity', self._listify(fixity))

    def get_fixity(self, index=None):
        return self._list_getter('fixity', index)

    def add_fixity(self, fixity):
        self._add_to_field('fixity', fixity)

    def set_size(self, size):
        self._set_field('size', size)

    def get_size(self):
        return self._get_field('size')
        pass

    def set_format(self, format):
        self._set_field('format', self._listify(format))

    def get_format(self, index=None):
        return self._list_getter('format', index)

    def add_format(self, format):
        self._add_to_field('format', format)

    def set_creatingApplication(self, creatingApplication):
        self._set_field('creatingApplication', self._listify(creatingApplication))

    def get_creatingApplication(self, index=None):
        return self._list_getter('creatingApplication', index)

    def add_creatingApplication(self, creatingApplication):
        self._add_to_field('creatingApplication', creatingApplication)

    def set_inhibitors(self, inhibitors):
        self._set_field('inhibitors', self._listify(inhibitors))

    def get_inhibitors(self, index=None):
        return self._list_getter('inhibitors', index)

    def add_inhibitors(self, inhibitors):
        self._add_to_field('inhibitors', inhibitors)

    def set_objectCharacteristicsExtension(self, objectCharacteristicsExtension):
        self._set_field('objectCharacteristicsExtension', self._listify(objectCharacteristicsExtension))

    def get_objectCharacteristicsExtension(self, index=None):
        return self._list_getter('objectCharacteristicsExtension', index)

    def add_objectCharacteristicsExtension(self, objectCharacteristicsExtension):
        self._add_to_field('objectCharacteristicsExtension', objectCharacteristicsExtension)


class Inhibitors(PremisNode):
    def __init__(self, inhibitorType):
        PremisNode.__init__(self, 'inhibitors')
        self.set_inhibitorType(inhibitorType)

    def set_inhibitorType(self, inhibitorType):
        self._set_field('inhibitorType', inhibitorType)

    def get_inhibitorType(self):
        return self._get_field('inhibitorType')

    def set_inhibitorTarget(self, inhibitorTarget):
        self._set_field('inhibitorTarget', self._listify(inhibitorTarget))

    def add_inhibitorTarget(self, inhibitorTarget):
        self._add_to_field('inhibitorTarget', inhibitorTarget)

    def get_inhibitorTarget(self, index=None):
        return self._list_getter('inhibitorTarget', index)

    def set_inhibitorKey(self, inhibitorKey):
        self._set_field('inhibitorKey', inhibitorKey)

    def get_inhibitorKey(self):
        return self._get_field('inhibitorKey')


class CreatingApplication(PremisNode):
    def __init__(self):
        PremisNode.__init__(self, 'creatingApplication')

    def set_creatingApplicationName(self, creatingApplicationName):
        self._set_field('creatingApplicationName', creatingApplicationName)

    def get_creatingApplicationName(self):
        return self._get_field('creatingApplicationName')

    def set_creatingApplicationVersion(self, creatingApplicationVersion):
        self._set_field('creatingApplicationVersion', creatingApplicationVersion)

    def get_creatingApplicationVersion(self):
        return self._get_field('creatingApplicationVersion')

    def set_dateCreatedByApplication(self, dateCreatedByApplication):
        self._set_field('dateCreatedByApplication', dateCreatedByApplication)

    def get_dateCreatedByApplication(self):
        return self._get_field('dateCreatedByApplication')

    def set_creatingApplicationExtension(self, creatingApplicationExtension):
        self._set_field('creatingApplicationExtension', self._listify(creatingApplicationExtension))

    def get_creatingApplicationExtension(self, index=None):
        return self._list_getter('creatingApplicationExtension', index)

    def add_creatingApplicationExtension(self, creatingApplicationExtension):
        self._add_to_field('creatingApplicationExtension', creatingApplicationExtension)


class Format(PremisNode):
    def __init__(self):
        PremisNode.__init__(self, 'format')

    def set_formatDesignation(self, formatDesignation):
        self._set_field('formatDesignation', formatDesignation)

    def get_formatDesignation(self):
        return self._get_field('formatDesignation')

    def set_formatRegistry(self, formatRegistry):
        self._set_field('formatRegistry', formatRegistry)

    def get_formatRegistry(self):
        return self._get_field('formatRegistry')

    def set_formatNote(self, formatNote):
        self._set_field('formatNote', self._listify(formatNote))

    def get_formatNote(self, index=None):
        return self._list_getter('formatNote', index)

    def add_formatNote(self, formatNote):
        self._add_to_field('formatNote', formatNote)


class FormatDesignation(PremisNode):
    def __init__(self, formatName):
        PremisNode.__init__(self, 'formatDesignation')
        self.set_formatName(formatName)

    def set_formatName(self, formatName):
        self._set_field('formatName', formatName)

    def get_formatName(self):
        return self._get_field('formatName')

    def set_formatVersion(self, formatVersion):
        self._set_field('formatVersion', formatVersion)

    def get_formatVersion(self):
        return self._get_field('formatVersion')


class FormatRegistry(PremisNode):
    def __init__(self, formatRegistryName, formatRegistryKey):
        PremisNode.__init__(self, 'formatRegistry')
        self.set_formatRegistryName(formatRegistryName)
        self.set_formatRegistryKey(formatRegistryKey)

    def set_formatRegistryName(self, formatRegistryName):
        self._set_field('formatRegistryName', formatRegistryName)

    def get_formatRegistryName(self):
        return self._get_field('formatRegistryName')

    def set_formatRegistryKey(self, formatRegistryKey):
        self._set_field('formatRegistryKey', formatRegistryKey)

    def get_formatRegistryKey(self):
        return self._get_field('formatRegistryKey')

    def set_formatRegistryRole(self, formatRegistryRole):
        self._set_field('formatRegistryRole', formatRegistryRole)

    def get_formatRegistryRole(self):
        return self._get_field('formatRegistryRole')


class Fixity(PremisNode):
    def __init__(self, messageDigestAlgorithm, messageDigest):
        PremisNode.__init__(self, 'fixity')
        self.set_messageDigestAlgorithm(messageDigestAlgorithm)
        self.set_messageDigest(messageDigest)

    def set_messageDigestAlgorithm(self, messageDigestAlgorithm):
        self._set_field('messageDigestAlgorithm', messageDigestAlgorithm)

    def get_messageDigestAlgorithm(self):
        return self._get_field('messageDigestAlgorithm')

    def set_messageDigest(self, messageDigest):
        self._set_field('messageDigest', messageDigest)

    def get_messageDigest(self):
        return self._get_field('messageDigest')

    def set_messageDigestOriginator(self, messageDigestOriginator):
        self._set_field('messageDigestOriginator', messageDigestOriginator)

    def get_messageDigestOriginator(self):
        return self._get_field('messageDigestOriginator')


class SignificantProperties(PremisNode):
    def __init__(self):
        PremisNode.__init__(self, 'significantProperties')

    def set_significantPropertiesType(self, significantPropertiesType):
        self._set_field('significantPropertiesType', significantPropertiesType)

    def get_significantPropertiesType(self):
        return self._get_field('significantPropertiesType')

    def set_significantPropertiesValue(self, significantPropertiesValue):
        self._set_field('significantPropertiesValue', significantPropertiesValue)

    def get_significantPropertiesValue(self):
        return self._get_field('significantPropertiesValue')

    def set_significantPropertiesExtension(self, significantPropertiesExtension):
        self._set_field('significantPropertiesExtension', self._listify(significantPropertiesExtension))

    def get_significantPropertiesExtension(self, index=None):
        return self._list_getter('significantPropertiesExtension', index)

    def add_significantPropertiesExtension(self, significantPropertiesExtension):
        self._add_to_field('significantPropertiesExtension', significantPropertiesExtension)


class PreservationLevel(PremisNode):
    def __init__(self, preservationLevelValue):
        PremisNode.__init__(self, 'preservationLevel')
        self._set_field('preservationLevelValue', preservationLevelValue)

    def set_preservationLevelType(self, preservationLevelType):
        self._set_field('preservationLevelType', preservationLevelType)

    def get_preservationLevelType(self):
        return self._get_field('preservationLevelType')

    def set_preservationLevelValue(self, preservationLevelValue):
        self._set_field('preservationLevelValue', preservationLevelValue)

    def get_preservationLevelValue(self):
        return self._get_field('preservationLevelValue')

    def set_preservationLevelRole(self, preservationLevelRole):
        self._set_field('preservationLevelRole', preservationLevelRole)

    def get_preservationLevelRole(self):
        return self._get_field('preservationLevelRole')

    def set_preservationLevelRationale(self, preservationLevelRationale):
        self._set_field('preservationLevelRationale', self._listify(preservationLevelRationale))

    def get_preservationLevelRationale(self, index=None):
        return self._list_getter('preservationLevelRationale', index)

    def add_preservationLevelRationale(self, preservationLevelRationale):
        self._add_to_field('preservationLevelRationale', preservationLevelRationale)

    def set_preservationLevelDateAssigned(self, preservationLevelDateAssigned):
        self._set_field('preservationLevelDateAssigned', preservationLevelDateAssigned)

    def get_preservationLevelDateAssigned(self):
        return self._get_field('preservationLevelDateAssigned')


class Event(PremisNode):
    def __init__(self, eventType, eventIdentifier, eventDateTime):
        PremisNode.__init__(self, 'event')
        self.set_eventType(eventType)
        self.set_eventIdentifier(eventIdentifier)
        self.set_eventDateTime(eventDateTime)

    def set_eventIdentifier(self, eventIdentifier):
        self._set_field('eventIdentifier', eventIdentifier)

    def get_eventIdentifier(self):
        return self._get_field('eventIdentifier')

    def set_eventType(self, eventType):
        self._set_field('eventType', eventType)

    def get_eventType(self):
        return self._get_field('eventType')

    def set_eventDateTime(self, eventDateTime):
        self._set_field('eventDateTime', eventDateTime)

    def get_eventDateTime(self):
        return self._get_field('eventDateTime')

    def set_eventDetailInformation(self, eventDetailInformation):
        self._set_field('eventDetailInformation', self._listify(eventDetailInformation))

    def get_eventDetailInformation(self, index=None):
        return self._list_getter('eventDetailInformation', index)

    def add_eventDetailInformation(self, eventDetailInformation):
        self._add_to_field('eventDetailInformation', eventDetailInformation)

    def set_eventOutcomeInformation(self, eventOutcomeInformation):
        self._set_field('eventOutcomeInformation', self._listify(eventOutcomeInformation))

    def get_eventOutcomeInformation(self, index=None):
        return self._list_getter('eventOutcomeInformation', index)

    def add_eventOutcomeInformation(self, eventOutcomeInformation):
        self._add_to_field('eventOutcomeInformation', eventOutcomeInformation)

    def set_linkingAgentIdentifier(self, linkingAgentIdentifier):
        self._set_field('linkingAgentIdentifier', self._listify(linkingAgentIdentifier))

    def get_linkingAgentIdentifier(self, index=None):
        return self._list_getter('linkingAgentIdentifier', index)

    def add_linkingAgentIdentifier(self, linkingAgentIdentifier):
        self._add_to_field('linkingAgentIdentifier', linkingAgentIdentifier)

    def set_linkingObjectIdentifier(self, linkingObjectIdentifier):
        self._set_field('linkingObjectIdentifier', self._listify(linkingObjectIdentifier))

    def get_linkingObjectIdentifier(self, index=None):
        return self._list_getter('linkingObjectIdentifier', index)

    def add_linkingObjectIdentifier(self, linkingObjectIdentifier):
        self._add_to_field('linkingObjectIdentifier', linkingObjectIdentifier)


class EventOutcomeInformation(PremisNode):
    def __init__(self):
        PremisNode.__init__(self, 'eventOutcomeInformation')

    def set_eventOutcome(self, eventOutcome):
        self._set_field('eventOutcome', eventOutcome)

    def get_eventOutcome(self):
        return self._get_field('eventOutcome')

    def set_eventDetailInformation(self, eventDetailInformation):
        self._set_field('eventDetailInformation', self._listify(eventDetailInformation))

    def get_eventDetailInformation(self, index=None):
        return self._list_getter('eventDetailInformation', index)

    def add_eventDetailInformation(self, eventDetailInformation):
        self._add_to_field('eventDetailInformation', eventDetailInformation)

    def set_eventOutcomeDetail(self, eventOutcomeDetail):
        self._set_field('eventOutcomeDetail', self._listify(eventOutcomeDetail))

    def get_eventOutcomeDetail(self, index=None):
        return self._list_getter('eventOutcomeDetail', index)

    def add_eventOutcomeDetail(self, eventOutcomeDetail):
        self._add_to_field('eventOutcomeDetail', eventOutcomeDetail)


class EventDetailInformation(PremisNode):
    def __init__(self):
        PremisNode.__init__(self, 'eventDetailInformation')

    def set_eventDetail(self, eventDetail):
        self._set_field('eventDetail', eventDetail)

    def get_eventDetail(self):
        return self._get_field('eventDetail')

    def set_eventDetailExtension(self, eventDetailExtension):
        self._set_field('eventDetailExtension', self._listify(eventDetailExtension))

    def get_eventDetailExtension(self, index=None):
        return self._list_getter('eventDetailExtension', index)

    def add_eventDetailExtension(self, eventDetailExtension):
        self._add_to_field('eventDetailExtension', eventDetailExtension)


class EventOutcomeDetail(PremisNode):
    def __init__(self):
        PremisNode.__init__(self, 'eventOutcomeDetail')

    def set_eventOutcomeDetailNote(self, eventOutcomeDetailNote):
        self._set_field('eventOutcomeDetailNote', eventOutcomeDetailNote)

    def get_eventOutcomeDetailNote(self):
        return self._get_field('eventOutcomeDetailNote')

    def set_eventOutcomeDetailExtension(self, eventOutcomeDetailExtension):
        self._set_field('eventOutcomeDetailExtension', self._listify(eventOutcomeDetailExtension))

    def get_eventOutcomeDetailExtension(self, index=None):
        return self._list_getter('eventOutcomeDetailExtension', index)

    def add_eventOutcomeDetailExtension(self, eventOutcomeDetailExtension):
        self._add_to_field('eventOutcomeDetailExtension', eventOutcomeDetailExtension)


class Agent(PremisNode):
    def __init__(self, agentIdentifier):
        PremisNode.__init__(self, 'agent')
        self.set_agentIdentifier(agentIdentifier)

    def set_agentIdentifier(self, agentIdentifier):
        self._set_field('agentIdentifier', self._listify(agentIdentifier))

    def get_agentIdentifier(self, index=None):
        return self._list_getter('agentIdentifier', index)

    def add_agentIdentifier(self, agentIdentifier):
        self._add_to_field('agentIdentifier', agentIdentifier)

    def set_agentName(self, agentName):
        self._set_field('agentName', self._listify(agentName))

    def get_agentName(self, index=None):
        return self._list_getter('agentName', index)

    def add_agentName(self, agentName):
        self._add_to_field('agentName', agentName)

    def set_agentType(self, agentType):
        self._set_field('agentType', agentType)

    def get_agentType(self):
        return self._get_field('agentType')

    def set_agentVersion(self, agentVersion):
        self._set_field('agentVersion', agentVersion)

    def get_agentVersion(self):
        return self._get_field('agentVersion')

    def set_agentNote(self, agentNote):
        self._set_field('agentNote', self._listify(agentNote))

    def get_agentNote(self, index=None):
        return self._list_getter('agentNote', index)

    def add_agentNote(self, agentNote):
        self._add_to_field('agentNote', agentNote)

    def set_agentExtension(self, agentExtension):
        self._set_field('agentExtension', self._listify(agentExtension))

    def get_agentExtension(self, index=None):
        return self._list_getter('agentExtension', index)

    def add_agentExtension(self, agentExtension):
        self._add_to_field('agentExtension', agentExtension)

    def set_linkingEventIdentifier(self, linkingEventIdentifier):
        self._set_field('linkingEventIdentifier', self._listify(linkingEventIdentifier))

    def get_linkingEventIdentifier(self, index=None):
        return self._list_getter('linkingEventIdentifier', index)

    def add_linkingEventIdentifier(self, linkingEventIdentifier):
        self._add_to_field('linkingEventIdentifier', linkingEventIdentifier)

    def set_linkingRightsStatementIdentifier(self, linkingRightsStatementIdentifier):
        self._set_field('linkingRightsStatementIdentifier', self._listify(linkingRightsStatementIdentifier))

    def get_linkingRightsStatementIdentifier(self, index=None):
        return self._list_getter('linkingRightsStatementIdentifier', index)

    def add_linkingRightsStatementIdentifier(self, linkingRightsStatementIdentifier):
        self._add_to_field('linkingRightsStatementIdentifier', linkingRightsStatementIdentifier)

    def set_linkingEnvironmentIdentifier(self, linkingEnvironmentIdentifier):
        self._set_field('linkingEnvironmentIdentifier', self._listify(linkingEnvironmentIdentifier))

    def get_linkingEnvironmentIdentifier(self, index=None):
        return self._list_getter('linkingEnvironmentIdentifier', index)

    def add_linkingEnvironmentIdentifier(self, linkingEnvironmentIdentifier):
        self._add_to_field('linkingEnvironmentIdentifier', linkingEnvironmentIdentifier)


class AgentIdentifier(PremisNode):
    def __init__(self, agentIdentifierType, agentIdentifierValue):
        PremisNode.__init__(self, 'agentIdentifier')
        self.set_agentIdentifierType(agentIdentifierType)
        self.set_agentIdentifierValue(agentIdentifierValue)

    def set_agentIdentifierType(self, agentIdentifierType):
        self._set_field('agentIdentifierType', agentIdentifierType)

    def get_agentIdentifierType(self):
        return self._get_field('agentIdentifierType')

    def set_agentIdentifierValue(self, agentIdentifierValue):
        self._set_field('agentIdentifierValue', agentIdentifierValue)

    def get_agentIdentifierValue(self):
        return self._get_field('agentIdentifierValue')


class LinkingEnvironmentIdentifier(PremisNode):
    def __init__(self, linkingEnvironmentIdentifierType, linkingEnvironmentIdentifierValue):
        PremisNode.__init__(self, 'linkingEnvironmentIdentifier')
        self.set_linkingEnvironmentIdentifierType(linkingEnvironmentIdentifierType)
        self.set_linkingEnvironmentIdentifierValue(linkingEnvironmentIdentifierValue)

    def set_linkingEnvironmentIdentifierType(self, linkingEnvironmentIdentifierType):
        self._set_field('linkingEnvironmentIdentifierType', linkingEnvironmentIdentifierType)

    def get_linkingEnvironmentIdentifierType(self):
        return self._get_field('linkingEnvironmentIdentifierType')

    def set_linkingEnvironmentIdentifierValue(self, linkingEnvironmentIdentifierValue):
        self._set_field('linkingEnvironmentIdentifierValue', linkingEnvironmentIdentifierValue)

    def get_linkingEnvironmentIdentifierValue(self):
        return self._get_field('linkingEnvironmentIdentifierValue')

    def set_linkingEnvironmentRole(self, linkingEnvironmentRole):
        self._set_field('linkingEnvironmentRole', self._listify(linkingEnvironmentRole))

    def get_linkingEnvironmentRole(self, index=None):
        return self._list_getter('linkingEnvironmentRole', index)

    def add_linkingEnvironmentRole(self, linkingEnvironmentRole):
        self._add_to_field('linkingEnvironmentRole', linkingEnvironmentRole)


class LinkingAgentIdentifier(PremisNode):
    def __init__(self, linkingAgentIdentifierType, linkingAgentIdentifierValue):
        PremisNode.__init__(self, 'linkingAgentIdentifier')
        self.set_linkingAgentIdentifierType(linkingAgentIdentifierType)
        self.set_linkingAgentIdentifierValue(linkingAgentIdentifierValue)

    def set_linkingAgentIdentifierType(self, linkingAgentIdentifierType):
        self._set_field('linkingAgentIdentifierType', linkingAgentIdentifierType)

    def get_linkingAgentIdentifierType(self):
        return self._get_field('linkingAgentIdentifierType')

    def set_linkingAgentIdentifierValue(self, linkingAgentIdentifierValue):
        self._set_field('linkingAgentIdentifierValue', linkingAgentIdentifierValue)

    def get_linkingAgentIdentifierValue(self):
        return self._get_field('linkingAgentIdentifierValue')

    def set_linkingAgentRole(self, linkingAgentRole):
        self._set_field('linkingAgentRole', self._listify(linkingAgentRole))

    def get_linkingAgentRole(self, index=None):
        return self._list_getter('linkingAgentRole', index)

    def add_linkingAgentRole(self, linkingAgentRole):
        self._add_to_field('linkingAgentRole', linkingAgentRole)


class Rights(PremisNode):
    def __init__(self, rightsStatement=None, rightsExtension=None):
        if rightsStatement is None and rightsExtension is None:
            raise ValueError("Either rightsStatement or rightsExtension must be supplied.")
        PremisNode.__init__(self, 'rights')
        if rightsStatement is not None:
            self.set_rightsStatement(rightsStatement)
        if rightsExtension is not None:
            self.set_rightsExtension(rightsExtension)

    def set_rightsStatement(self, rightsStatement):
        self._set_field('rightsStatement', self._listify(rightsStatement))

    def get_rightsStatement(self, index=None):
        return self._list_getter('rightsStatement', index)

    def add_rightsStatement(self, rightsStatement):
        self._add_to_field('rightsStatement', rightsStatement)

    def set_rightsExtension(self, rightsExtension):
        self._set_field('rightsExtension', self._listify(rightsExtension))

    def get_rightsExtension(self, index=None):
        return self._list_getter('rightsExtension', index)

    def add_rightsExtension(self, rightsExtension):
        self._add_to_field('rightsExtension', rightsExtension)


class RightsStatement(PremisNode):
    def __init__(self, rightsStatementIdentifier, rightsBasis):
        PremisNode.__init__(self, 'rightsStatement')
        self.set_rightsStatementIdentifier(rightsStatementIdentifier)
        self.set_rightsBasis(rightsBasis)

    def set_rightsStatementIdentifier(self, rightsStatementIdentifier):
        self._set_field('rightsStatementIdentifier', rightsStatementIdentifier)

    def get_rightsStatementIdentifier(self):
        return self._get_field('rightsStatementIdentifier')

    def set_rightsBasis(self, rightsBasis):
        self._set_field('rightsBasis', rightsBasis)

    def get_rightsBasis(self):
        return self._get_field('rightsBasis')

    def set_copyrightInformation(self, copyrightInformation):
        self._set_field('copyrightInformation', copyrightInformation)

    def get_copyrightInformation(self):
        return self._get_field('copyrightInformation')

    def set_licenseInformation(self, licenseInformation):
        self._set_field('licenseInformation', licenseInformation)

    def get_licenseInformation(self):
        return self._get_field('licenseInformation')

    def set_statuteInformation(self, statuteInformation):
        self._set_field('statuteInformation', self._listify(statuteInformation))

    def get_statuteInformation(self, index=None):
        return self._list_getter('statuteInformation', index)

    def add_statuteInformation(self, statuteInformation):
        self._add_to_field('statuteInformation', statuteInformation)

    def set_otherRightsInformation(self, otherRightsInformation):
        self._set_field('otherRightsInformation', otherRightsInformation)

    def get_otherRightsInformation(self):
        return self._get_field('otherRightsInformation')

    def set_rightsGranted(self, rightsGranted):
        self._set_field('rightsGranted', self._listify(rightsGranted))

    def get_rightsGranted(self, index=None):
        return self._list_getter('rightsGranted', index)

    def add_rightsGranted(self, rightsGranted):
        self._add_to_field('rightsGranted', rightsGranted)

    def set_linkingObjectIdentifier(self, linkingObjectIdentifier):
        self._set_field('linkingObjectIdentifier', self._listify(linkingObjectIdentifier))

    def get_linkingObjectIdentifier(self, index=None):
        return self._list_getter('linkingObjectIdentifier', index)

    def add_linkingObjectIdentifier(self, linkingObjectIdentifier):
        self._add_to_field('linkingObjectIdentifier', linkingObjectIdentifier)

    def set_linkingAgentIdentifier(self, linkingAgentIdentifier):
        self._set_field('linkingAgentIdentifier', self._listify(linkingAgentIdentifier))

    def get_linkingAgentIdentifier(self, index=None):
        return self._list_getter('linkingAgentIdentifier', index)

    def add_linkingAgentIdentifier(self, linkingAgentIdentifier):
        self._add_to_field('linkingAgentIdentifier', linkingAgentIdentifier)


class RightsGranted(PremisNode):
    def __init__(self, act):
        PremisNode.__init__(self, 'rightsGranted')
        self.set_act(act)

    def set_act(self, act):
        self._set_field('act', act)

    def get_act(self):
        return self._get_field('act')

    def set_restriction(self, restriction):
        self._set_field('restriction', self._listify(restriction))

    def get_restriction(self, index=None):
        return self._list_getter('restriction', index)

    def add_restriction(self, restriction):
        self._add_to_field('restriction', restriction)

    def set_termOfGrant(self, termOfGrant):
        self._set_field('termOfGrant', termOfGrant)

    def get_termOfGrant(self):
        return self._get_field('termOfGrant')

    def set_termOfRestriction(self, termOfRestriction):
        self._set_field('termOfRestriction', termOfRestriction)

    def get_termOfRestriction(self):
        return self._get_field('termOfRestriction')

    def set_rightsGrantedNote(self, rightsGrantedNote):
        self._set_field('rightsGrantedNote', self._listify(rightsGrantedNote))

    def get_rightsGrantedNote(self, index=None):
        return self._list_getter('rightsGrantedNote', index)

    def add_rightsGrantedNote(self, rightsGrantedNote):
        self._add_to_field('rightsGrantedNote', rightsGrantedNote)


class TermOfRestriction(PremisNode):
    def __init__(self, startDate):
        PremisNode.__init__(self, 'termOfRestriction')
        self.set_startDate(startDate)

    def set_startDate(self, startDate):
        self._set_field('startDate', startDate)

    def get_startDate(self):
        return self._get_field('startDate')

    def set_endDate(self, endDate):
        self._set_field('endDate', endDate)

    def get_endDate(self):
        return self._get_field('endDate')


class TermOfGrant(PremisNode):
    def __init__(self, startDate):
        PremisNode.__init__(self, 'termOfGrant')
        self.set_startDate(startDate)

    def set_startDate(self, startDate):
        self._set_field('startDate', startDate)

    def get_startDate(self):
        return self._get_field('startDate')

    def set_endDate(self, endDate):
        self._set_field('endDate', endDate)

    def get_endDate(self):
        return self._get_field('endDate')


class OtherRightsInformation(PremisNode):
    def __init__(self, otherRightsBasis):
        PremisNode.__init__(self, 'otherRightsInformation')
        self.set_otherRightsBasis(otherRightsBasis)

    def set_otherRightsDocumentationIdentifier(self, otherRightsDocumentationIdentifier):
        self._set_field('otherRightsDocumentationIdentifier', self._listify(otherRightsDocumentationIdentifier))

    def get_otherRightsDocumentationIdentifier(self, index=None):
        return self._list_getter('otherRightsDocumentationIdentifier', index)

    def add_otherRightsDocumentationIdentifier(self, otherRightsDocumentationIdentifier):
        self._add_to_field('otherRightsDocumentationIdentifier', otherRightsDocumentationIdentifier)

    def set_otherRightsBasis(self, otherRightsBasis):
        self._set_field('otherRightsBasis', otherRightsBasis)

    def get_otherRightsBasis(self):
        return self._get_field('otherRightsBasis')

    def set_otherRightsApplicableDates(self, otherRightsApplicableDates):
        self._set_field('otherRightsApplicableDates', otherRightsApplicableDates)

    def get_otherRightsApplicableDates(self):
        return self._get_field('otherRightsApplicableDates')

    def set_otherRightsNote(self, otherRightsNote):
        self._set_field('otherRightsNote', self._listify(otherRightsNote))

    def get_otherRightsNote(self, index=None):
        return self._list_getter('otherRightsNote', index)

    def add_otherRightsNote(self, otherRightsNote):
        self._add_to_field('otherRightsNote', otherRightsNote)


class OtherRightsApplicableDates(PremisNode):
    def __init__(self):
        PremisNode.__init__(self, 'otherRightsApplicableDates')

    def set_startDate(self, startDate):
        self._set_field('startDate', startDate)

    def get_startDate(self):
        return self._get_field('startDate')

    def set_endDate(self, endDate):
        self._set_field('endDate', endDate)

    def get_endDate(self):
        return self._get_field('startDate')


class OtherRightsDocumentationIdentifier(PremisNode):
    def __init__(self, otherRightsDocumentationIdentifierType, otherRightsDocumentationIdentifierValue):
        PremisNode.__init__(self, 'otherRightsDocumentationIdentifier')
        self.set_otherRightsDocumentationIdentifierType(otherRightsDocumentationIdentifierType)
        self.set_otherRightsDocumentationIdentifierValue(otherRightsDocumentationIdentifierValue)

    def set_otherRightsDocumentationIdentifierType(self, otherRightsDocumentationIdentifierType):
        self._set_field('otherRightsDocumentationIdentifierType', otherRightsDocumentationIdentifierType)

    def get_otherRightsDocumentationIdentifierType(self):
        return self._get_field('otherRightsDocumentationIdentifierType')

    def set_otherRightsDocumentationIdentifierValue(self, otherRightsDocumentationIdentifierValue):
        self._set_field('otherRightsDocumentationIdentifierValue', otherRightsDocumentationIdentifierValue)

    def get_otherRightsDocumentationIdentifierValue(self):
        return self._get_field('otherRightsDocumentationIdentifierValue')

    def set_otherRightsDocumentationRole(self, otherRightsDocumentationRole):
        self._set_field('otherRightsDocumentationRole', otherRightsDocumentationRole)

    def get_otherRightsDocumentationRole(self):
        return self._get_field('otherRightsDocumentationRole')


class StatuteInformation(PremisNode):
    def __init__(self, statuteJurisdiction, statuteCitation):
        PremisNode.__init__(self, 'StatuteInformation')
        self.set_statuteJurisdiction(statuteJurisdiction)
        self.set_statuteCitation(statuteCitation)

    def set_statuteJurisdiction(self, statuteJurisdiction):
        self._set_field('statuteJurisdiction', statuteJurisdiction)

    def get_statuteJurisdiction(self):
        return self._get_field('statuteJurisdiction')

    def set_statuteCitation(self, statuteCitation):
        self._set_field('statuteCitation', statuteCitation)

    def get_statuteCitation(self):
        return self._get_field('statuteCitation')

    def set_statuteInformationDeterminationDate(self, statuteInformationDeterminationDate):
        self._set_field('statuteInformationDeterminationDate', statuteInformationDeterminationDate)

    def get_statuteInformationDeterminationDate(self):
        return self._get_field('statuteInformationDeterminationDate')

    def set_statuteNote(self, statuteNote):
        self._set_field('statuteNote', self._listify(statuteNote))

    def get_statuteNote(self, index=None):
        return self._list_getter('statuteNote', index)

    def add_statuteNote(self, statuteNote):
        self._add_to_field('statuteNote')

    def set_statuteDocumentationIdentifier(self, statuteDocumentationIdentifier):
        self.set_field('statuteDocumentationIdentifier', self._listify(statuteDocumentationIdentifier))

    def get_statuteDocumentationIdentifier(self, index=None):
        return self._list_getter('statuteDocumentationIdentifier', index)

    def add_statuteDocumentationIdentifier(self, statuteDocumentationIdentifier):
        self._add_to_field('statuteDocumentationIdentifier', statuteDocumentationIdentifier)

    def set_statuteApplicableDates(self, statuteApplicableDates):
        self._set_field('statuteApplicableDates', statuteApplicableDates)

    def get_statuteApplicableDates(self):
        return self._get_field('statuteApplicableDates')


class StatuteApplicableDates(PremisNode):
    def __init__(self):
        PremisNode.__init__(self, 'StatuteApplicableDates')

    def set_startDate(self, startDate):
        self._set_field('startDate', startDate)

    def get_startDate(self):
        return self._get_field('startDate')

    def set_endDate(self, endDate):
        self._set_field('endDate', endDate)

    def get_endDate(self):
        return self._get_field('endDate')


class StatuteDocumentationIdentifier(PremisNode):
    def __init__(self, statuteDocumentationIdentifierType, statuteDocumentationIdentifierValue):
        PremisNode.__init__(self, 'StatuteDocumentationIdentifier')
        self.set_statuteDocumentationIdentifierType(statuteDocumentationIdentifierType)
        self.set_statuteDocumentationIdentifierValue(statuteDocumentationIdentifierValue)

    def set_statuteDocumentationIdentifierType(self, statuteDocumentationIdentifierType):
        self._set_field('statuteDocumentationIdentifierType', statuteDocumentationIdentifierType)

    def get_statuteDocumentationIdentifierType(self):
        return self._get_field('statuteDocumentationIdentifierType')

    def set_statuteDocumentationIdentifierValue(self, statuteDocumentationIdentifierValue):
        self._set_field('statuteDocumentationIdentifierValue', statuteDocumentationIdentifierValue)

    def get_statuteDocumentationIdentifierValue(self):
        return self._get_field('statuteDocumentationIdentifierValue')

    def set_statuteDocumentationRole(self, statuteDocumentationRole):
        self._set_field('statuteDocumentationRole', statuteDocumentationRole)

    def get_statuteDocumentationRole(self):
        return self._get_field('statuteDocumentationRole')


class LicenseInformation(PremisNode):
    def __init__(self):
        PremisNode.__init__(self, 'licenseInformation')

    def set_licenseDocumentationIdentifier(self, licenseDocumentationIdentifier):
        self._set_field('licenseDocumentationIdentifier', self._listify(licenseDocumentationIdentifier))

    def get_licenseDocumentationIdentifier(self, index=None):
        return self._list_getter('licenseDocumentationIdentifier', index)

    def add_licenseDocumentationIdentifier(self, licenseDocumentationIdentifier):
        self._add_to_field('licenseDocumentationIdentifier')

    def set_licenseTerms(self, licenseTerms):
        self._set_field('licenseTerms', licenseTerms)

    def get_licenseTerms(self):
        return self._get_field('licenseTerms')

    def set_licenseNote(self, licenseNote):
        self._set_field('licenseNote', self._listify(licenseNote))

    def get_licenseNote(self, index=None):
        return self._list_getter('licenseNote', index)

    def add_licenseNote(self, licenseNote):
        self._add_to_field('licenseNote', licenseNote)

    def set_licenseApplicableDates(self, licenseApplicableDates):
        self._set_field('licenseApplicableDates', licenseApplicableDates)

    def get_licenseApplicableDates(self):
        return self._get_field('licenseApplicableDates')


class LicenseApplicableDates(PremisNode):
    def __init__(self):
        PremisNode.__init__(self, 'licenseApplicableDates')

    def set_startDate(self, startDate):
        self._set_field('startDate', startDate)

    def get_startDate(self):
        return self._get_field('startDate')

    def set_endDate(self, endDate):
        self._set_field('endDate', endDate)

    def get_endDate(self):
        return self._get_field('endDate')


class LicenseDocumentationIdentifier(PremisNode):
    def __init__(self, licenseDocumentationIdentifierType, licenseDocumentationIdentifierValue):
        PremisNode.__init__(self, 'licenseDocumentationIdentifier')
        self.set_licenseDocumentationIdentifierType(licenseDocumentationIdentifierType)
        self.set_licenseDocumentationIdentifierValue(licenseDocumentationIdentifierValue)

    def set_licenseDocumentationIdentifierType(self, licenseDocumentationIdentifierType):
        self._set_field('licenseDocumentationIdentifierType', licenseDocumentationIdentifierType)

    def get_licenseDocumentationIdentifierType(self):
        return self._get_field('licenseDocumentatinIdentiferType')

    def set_licenseDocumentationIdentifierValue(self, licenseDocumentationIdentifierValue):
        self._set_field('licenseDocumentationIdentifierValue', licenseDocumentationIdentifierValue)

    def get_licenseDocumentationIdentifierValue(self):
        return self._get_field('licenseDocumentationIdentifierValue')

    def set_licenseDocumentationRole(self, licenseDocumentationRole):
        self._set_field('licenseDocumentationRole', licenseDocumentationRole)

    def get_licenseDocumentationRole(self):
        return self._get_field('licenseDocumentationRole')


class CopyrightInformation(PremisNode):
    def __init__(self, copyrightStatus, copyrightJurisdiction):
        PremisNode.__init__(self, 'copyrightInformation')
        self.set_copyrightStatus(copyrightStatus)
        self.set_copyrightJurisdiction(copyrightJurisdiction)

    def set_copyrightStatus(self, copyrightStatus):
        self._set_field('copyrightStatus', copyrightStatus)

    def get_copyrightStatus(self):
        return self._get_field('copyrightStatus')

    def set_copyrightJurisdiction(self, copyrightJurisdiction):
        self._set_field('copyrightJurisdiction', copyrightJurisdiction)

    def get_copyrightJurisdiction(self):
        return self._get_field('copyrightJurisdiction')

    def set_copyrightStatusDeterminationDate(self, copyrightStatusDeterminationDate):
        self._set_field('copyrightStatusDeterminationDate', copyrightStatusDeterminationDate)

    def get_copyrightStatusDeterminationDate(self):
        return self._get_field('copyrightStatusDeterminationDate')

    def set_copyrightNote(self, copyrightNote):
        self._set_field('copyrightNote', self._listify(copyrightNote))

    def get_copyrightNote(self, index=None):
        return self._list_getter('copyrightNote', index)

    def add_copyrightNote(self, copyrightNote):
        self._add_to_field('copyrightNote', copyrightNote)

    def set_copyrightDocumentationIdentifier(self, copyrightDocumentationIdentifier):
        self._set_field('copyrightDocumentationIdentifier', self._listify(copyrightDocumentationIdentifier))

    def get_copyrightDocumentationIdentifier(self, index=None):
        return self._list_getter('copyrightDocumentationIdentifier', index)

    def add_copyrightDocumentationIdentifier(self, copyrightDocumentationIdentifier):
        self._add_to_field('copyrightDocumentationIdentifier', copyrightDocumentationIdentifier)

    def set_copyrightApplicableDates(self, copyrightApplicableDates):
        self._set_field('copyrightApplicableDates', copyrightApplicableDates)

    def get_copyrightApplicableDates(self):
        return self._get_field('copyrightApplicableDates')


class CopyrightApplicableDates(PremisNode):
    def __init__(self):
        PremisNode.__init__(self, 'copyrightApplicableDates')

    def set_startDate(self, startDate):
        self._set_field('startDate', startDate)

    def get_startDate(self):
        return self._get_field('startDate')

    def set_endDate(self, endDate):
        self._set_field('endDate', endDate)

    def get_endDate(self):
        return self._get_field('endDate')


class CopyrightDocumentationIdentifier(PremisNode):
    def __init__(self, copyrightDocumentationIdentifierType, copyrightDocumentationIdentifierValue):
        PremisNode.__init__(self, 'copyrightDocumentationIdentifier')
        self.set_copyrightDocumentationIdentifierType(copyrightDocumentationIdentifierType)
        self.set_copyrightDocumentationIdentifierValue(copyrightDocumentationIdentifierValue)

    def set_copyrightDocumentationIdentifierType(self, copyrightDocumentationIdentifierType):
        self._set_field('copyrightDocumentationIdentifierType', copyrightDocumentationIdentifierType)

    def get_copyrightDocumentationIdentifierType(self):
        return self._get_field('copyrightDocumentationIdentifierType')

    def set_copyrightDocumentationIdentifierValue(self, copyrightDocumentationIdentifierValue):
        self._set_field('copyrightDocumentationIdentifierValue', copyrightDocumentationIdentifierValue)

    def get_copyrightDocumentationIdentifierValue(self):
        return self._get_field('copyrightDocumentationIdentifierValue')

    def set_copyrightDocumentationRole(self, copyrightDocumentationRole):
        self._set_field('copyrightDocumentationRole', copyrightDocumentationRole)

    def get_copyrightDocumentationRole(self):
        return self._get_field('copyrightDocumentationRole')


class RightsStatementIdentifier(PremisNode):
    def __init__(self, rightsStatementIdentifierType, rightsStatementIdentifierValue):
        PremisNode.__init__(self, 'copyrightDocumentationIdentifier')
        self.set_rightsStatementIdentifierType(rightsStatementIdentifierType)
        self.set_rightsStatementIdentifierValue(rightsStatementIdentifierValue)

    def set_rightsStatementIdentifierType(self, rightsStatementIdentifierType):
        self._set_field('rightsStatementIdentifierType', rightsStatementIdentifierType)

    def get_rightsStatementIdentifierType(self):
        return self._get_field('rightsStatementIdentifierType')

    def set_rightsStatementIdentifierValue(self, rightsStatementIdentifierValue):
        self._set_field('rightsStatementIdentifierValue', rightsStatementIdentifierValue)

    def get_rightsStatementIdentifierValue(self):
        return self._get_field('rightsStatementIdentifiervalue')
