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


class PremisObjRecord(object):
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


class PremisEventRecord(object):
    def __init__(self):
        self.root = ET.element('event')
        pass

    def __repr__(self):
        return ET.tostring(self.root, encoding="unicode")


class PremisEntityRecord(object):
    def __init__(self):
        pass
        self.root = ET.element('entity')

    def __repr__(self):
        return ET.tostring(self.root, encoding="unicode")


class PremisRightsRecord(object):
    def __init__(self):
        pass
        self.root = ET.element('rights')

    def __repr__(self):
        return ET.tostring(self.root, encoding="unicode")
