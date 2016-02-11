import xml.etree.ElementTree as ET

from pypremis.nodes import *


class XMLNodeFactory(object):
    def __init__(self, xmlfile):
        ET.register_namespace('premis', "http://www.loc.gov/premis/v3")
        ET.register_namespace('xsi', "http://www.w3.org/2001/XMLSchema-instance")
        tree = ET.parse(xmlfile)
        self.xml = tree.getroot()

    def _find_all(self, node, tag, req=False):
        parse = [x for x in node.findall(tag)]
        if len(parse) < 1 and req:
            raise ValueError("The {} tag is required but was not found.".format(tag))
        result = [x.text for x in parse]
        return result

    def _find(self, node, tag, req=False):
        parse = node.find(tag)
        if parse is None and req:
            raise ValueError("The {} tag is required but was not found.".format(tag))
        try:
            result = parse.text
            return result
        except AttributeError:
            return ""

    def _find_node(self, node, tag, req=False):
        parse = node.find(tag)
        if parse is None and req:
            raise ValueError("The {} tag is required but was not found.".format(tag))
        if parse is None:
            return False
        return parse

    def _find_all_nodes(self, node, tag, req=False):
        parse = node.findall(tag)
        if not parse and req:
            raise ValueError("The {} tag is required but was not found.".format(tag))
        if parse is None:
            return False
        return parse

    def _process_nodes(self, func, node, tag, req=False):
        parse = self._find_all_nodes(node, tag, req)
        if parse:
            result = [func(x) for x in parse]
            return result
        return False

    def _pn(self, func, node, tag, req=False):
        return self._process_nodes(func, node, tag, req)

    def find_objects(self):
        return [self.buildObject(x) for x in self._find_all_nodes(self.xml, '{http://www.loc.gov/premis/v3}object')]

    def find_agents(self):
        return [self.buildAgent(x) for x in self._find_all_nodes(self.xml, '{http://www.loc.gov/premis/v3}agent')]

    def find_events(self):
        return [self.buildEvent(x) for x in self._find_all_nodes(self.xml, '{http://www.loc.gov/premis/v3}event')]

    def find_rights(self):
        return [self.buildRights(x) for x in self._find_all_nodes(self.xml, '{http://www.loc.gov/premis/v3}rights')]

    def buildObject(self, node):
        objIDs = self._pn(self.buildObjectIdentifier, node, '{http://www.loc.gov/premis/v3}objectIdentifier', req=True)
        objectCategory = node.get('{http://www.w3.org/2001/XMLSchema-instance}type').lstrip('premis:')
        if not objectCategory:
            raise ValueError("The object category was not specified and is required.")
        objectCharacteristics = self._pn(self.buildObjectCharacteristics, node, '{http://www.loc.gov/premis/v3}objectCharacteristics', req=True)
        obj = Object(objIDs, objectCategory, objectCharacteristics)

        preservationLevel = self._pn(self.buildPreservationLevel, node, '{http://www.loc.gov/premis/v3}preservationLevel')
        if preservationLevel:
            obj.set_preservationLevel(preservationLevel)

        significantProperties = self._pn(self.buildSignificantProperties, node, '{http://www.loc.gov/premis/v3}significantProperties')
        if significantProperties:
            obj.set_significantProperties(significantProperties)

        originalName = self._find(node, '{http://www.loc.gov/premis/v3}originalName')
        if originalName:
            obj.set_originalName(originalName)

        storage = self._pn(self.buildStorage, node, '{http://www.loc.gov/premis/v3}storage')
        if storage:
            obj.set_storage(storage)

        signatureInformation = self._pn(self.buildSignatureInformation, node, '{http://www.loc.gov/premis/v3}signatureInformation')
        if signatureInformation:
            obj.set_signatureInformation(signatureInformation)

        environmentFunction = self._pn(self.buildEnvironmentFunction, node, '{http://www.loc.gov/premis/v3}environmentFunction')
        if environmentFunction:
            obj.set_environmentFunction(environmentFunction)

        environmentDesignation = self._pn(self.buildEnvironmentDesignation, node, '{http://www.loc.gov/premis/v3}environmentDesignation')
        if environmentDesignation:
            obj.set_environmentDesignation(environmentDesignation)

        environmentRegistry = self._pn(self.buildEnvironmentRegistry, node, '{http://www.loc.gov/premis/v3}environmentRegistry')
        if environmentRegistry:
            obj.set_environmentRegistry(environmentRegistry)

        environmentExtension = self._find_all(node, '{http://www.loc.gov/premis/v3}environmentExtension')
        if environmentExtension:
            obj.set_environmentExtension(environmentExtension)

        relationship = self._pn(self.buildRelationship, node, '{http://www.loc.gov/premis/v3}relationship')
        if relationship:
            obj.set_relationship(relationship)

        linkingEventIdentifier = self._pn(self.buildLinkingEventIdentifier, node, '{http://www.loc.gov/premis/v3}linkingEventIdentifier')
        if linkingEventIdentifier:
            obj.set_linkingEventIdentifier(linkingEventIdentifier)

        linkingRightsStatementIdentifier = self._pn(self.buildLinkingRightsStatementIdentifier, node, '{http://www.loc.gov/premis/v3}linkingRightsStatementIdentifier')
        if linkingRightsStatementIdentifier:
            obj.set_linkingRightsStatementIdentifier(linkingRightsStatementIdentifier)

        return obj

    def buildObjectIdentifier(self, node):
        objectIdentifierType = self._find(node, '{http://www.loc.gov/premis/v3}objectIdentifierType', req=True)
        objectIdentifierValue = self._find(node, '{http://www.loc.gov/premis/v3}objectIdentifierValue', req=True)
        objID = ObjectIdentifier(objectIdentifierType, objectIdentifierValue)
        return objID

    def buildPreservationLevel(self, node):
        preservationLevelValue = self._find(node, '{http://www.loc.gov/premis/v3}preservationLevelValue', req=True)
        preservationLevel = PreservationLevel(preservationLevelValue)

        preservationLevelType = self._find(node, '{http://www.loc.gov/premis/v3}preservationLevelType')
        if preservationLevelType:
            preservationLevel.set_preservationLevelType(preservationLevelType)

        preservationLevelRole = self._find(node, '{http://www.loc.gov/premis/v3}preservationLevelRole')
        if preservationLevelRole:
            preservationLevel.set_preservationLevelRole(preservationLevelRole)

        preservationLevelRationale = self._find_all(node, '{http://www.loc.gov/premis/v3}preservationLevelRationale')
        if preservationLevelRationale:
            preservationLevel.set_preservationLevelRationale(preservationLevelRationale)

        preservationLevelDateAssigned = self._find(node, '{http://www.loc.gov/premis/v3}preservationLevelDateAssigned')
        if preservationLevelDateAssigned:
            preservationLevel.set_preservationLevelDateAssigned(preservationLevelDateAssigned)

        return preservationLevel

    def buildSignificantProperties(self, node):
        significantProperties = SignificantProperties()

        significantPropertiesType = self._find(node, '{http://www.loc.gov/premis/v3}significantPropertiesType')
        if significantPropertiesType:
            significantProperties.set_significantPropertiesType(significantPropertiesType)

        significantPropertiesValue = self._find(node, '{http://www.loc.gov/premis/v3}significantPropertiesValue')
        if significantPropertiesValue:
            significantProperties.set_significantPropertiesValue(significantPropertiesValue)

        significantPropertiesExtension = self._find_all(node, '{http://www.loc.gov/premis/v3}significantPropertiesExtension')
        if significantPropertiesExtension:
            significantProperties.set_significantPropertiesExtension(significantPropertiesExtension)

        return significantProperties

    def buildObjectCharacteristics(self, node):
        format = self._pn(self.buildFormat, node, '{http://www.loc.gov/premis/v3}format', req=True)
        objectCharacteristics = ObjectCharacteristics(format)

        compositionLevel = self._find(node, '{http://www.loc.gov/premis/v3}compositionLevel')
        if compositionLevel:
            objectCharacteristics.set_compositionLevel(compositionLevel)

        fixity = self._pn(self.buildFixity, node, '{http://www.loc.gov/premis/v3}fixity')
        if fixity:
            objectCharacteristics.set_fixity(fixity)

        size = self._find(node, '{http://www.loc.gov/premis/v3}size')
        if size:
            objectCharacteristics.set_size(size)

        creatingApplication = self._pn(self.buildCreatingApplication, node, '{http://www.loc.gov/premis/v3}creatingApplication')
        if creatingApplication:
            objectCharacteristics.set_creatingApplication(creatingApplication)

        inhibitors = self._pn(self.buildInhibitors, node, '{http://www.loc.gov/premis/v3}inhibitors')
        if inhibitors:
            objectCharacteristics.set_inhibitors(inhibitors)

        objectCharacteristicsExtension = self._find_all(node, '{http://www.loc.gov/premis/v3}objectCharacteristicsExtension')
        if objectCharacteristicsExtension:
            objectCharacteristics.set_objectCharacteristicsExtension(objectCharacteristicsExtension)

        return objectCharacteristics

    def buildStorage(self, node):
        storage = Storage()

        contentLocationNode = self._find_node(node, '{http://www.loc.gov/premis/v3}contentLocation')
        if contentLocationNode:
            contentLocation = self.buildContentLocation(contentLocationNode)
            storage.set_contentLocation(contentLocation)

        storageMedium = self._find(node, '{http://www.loc.gov/premis/v3}storageMedium')
        if storageMedium:
            storage.set_storageMedium(storageMedium)

        return storage

    def buildSignatureInformation(self, node):
        signatureInformation = SignatureInformation()
        signature = self._pn(self.buildSignature, node, '{http://www.loc.gov/premis/v3}signature')
        if signature:
            signatureInformation.set_signature(signature)

        signatureInformationExtension = self._find_all(node, '{http://www.loc.gov/premis/v3}signatureInformationExtension')
        if signatureInformationExtension:
            signatureInformation.set_signatureInformationExtension(signatureInformationExtension)

        return signatureInformation

    def buildEnvironmentFunction(self, node):
        environmentFunctionType = self._find(node, '{http://www.loc.gov/premis/v3}environmentFunctionType', req=True)
        environmentFunctionLevel = self._find(node, '{http://www.loc.gov/premis/v3}environmentFunctionLevel', req=True)

        environmentFunction = EnvironmentFunction(environmentFunctionType, environmentFunctionLevel)

        return environmentFunction

    def buildEnvironmentDesignation(self, node):
        environmentDesignationName = self._find(node, '{http://www.loc.gov/premis/v3}environmentName', req=True)

        environmentDesignation = EnvironmentDesignation(environmentDesignationName)

        environmentVersion = self._find(node, '{http://www.loc.gov/premis/v3}environmentVersion')
        if environmentVersion:
            environmentDesignation.set_environmentVersion(environmentVersion)

        environmentOrigin = self._find(node, '{http://www.loc.gov/premis/v3}environmentOrigin')
        if environmentOrigin:
            environmentDesignation.set_environmentOrigin(environmentOrigin)

        environmentDesignationNote = self._find_all(node, '{http://www.loc.gov/premis/v3}environmentDesignationNote')
        if environmentDesignationNote:
            environmentDesignation.set_environmentDesignationNote(environmentDesignationNote)

        environmentDesignationExtension = self._find_all(node, '{http://www.loc.gov/premis/v3}environmentDesignationExtension')
        if environmentDesignationExtension:
            environmentDesignation.set_environmentDesignationExtension(environmentDesignationExtension)

        return environmentDesignation

    def buildEnvironmentRegistry(self, node):
        environmentRegistryName = self._find(node, '{http://www.loc.gov/premis/v3}environmentRegistryName', req=True)
        environmentRegistryKey = self._find(node, '{http://www.loc.gov/premis/v3}environmentRegistryKey', req=True)

        environmentRegistry = EnvironmentRegistry(environmentRegistryName, environmentRegistryKey)

        environmentRegistryRole = self._find(node, '{http://www.loc.gov/premis/v3}environmentRegistryRole')
        if environmentRegistryRole:
            environmentRegistry.set_environmentRegistryRole(environmentRegistryRole)

        return environmentRegistry

    def buildRelationship(self, node):
        relationshipType = self._find(node, '{http://www.loc.gov/premis/v3}relationshipType', req=True)
        relationshipSubType = self._find(node, '{http://www.loc.gov/premis/v3}relationshipSubType', req=True)
        relatedObjectIdentifier = self._pn(self.buildRelatedObjectIdentifier, node, '{http://www.loc.gov/premis/v3}relatedObjectIdentifier', req=True)

        relationship = Relationship(relationshipType, relationshipSubType, relatedObjectIdentifier)

        relatedEventIdentifier = self._pn(self.buildRelatedEventIdentifier, node, '{http://www.loc.gov/premis/v3}relatedEventIdentifier')
        if relatedEventIdentifier:
            relationship.set_relatedEventIdentifier(relatedEventIdentifier)

        relatedEnvironmentPurpose = self._find_all(node, '{http://www.loc.gov/premis/v3}relatedEnvironmentPurpose')
        if relatedEnvironmentPurpose:
            relationship.set_relatedEnvironmentPurpose(relatedEnvironmentPurpose)

        relatedEnvironmentCharacteristic = self._find(node, '{http://www.loc.gov/premis/v3}relatedEnvironmentCharacteristic')
        if relatedEnvironmentCharacteristic:
            relationship.set_relatedEnvironmentCharacteristic(relatedEnvironmentCharacteristic)

        return relationship

    def buildLinkingEventIdentifier(self, node):
        linkingEventIdentifierType = self._find(node, '{http://www.loc.gov/premis/v3}linkingEventIdentifierType', req=True)
        linkingEventIdentifierValue = self._find(node, '{http://www.loc.gov/premis/v3}linkingEventIdentifierValue', req=True)

        linkingEventIdentifier = LinkingEventIdentifier(linkingEventIdentifierType, linkingEventIdentifierValue)

        return linkingEventIdentifier

    def buildLinkingRightsStatementIdentifier(self, node):
        linkingRightsStatementIdentifierType = self._find(node, '{http://www.loc.gov/premis/v3}linkingRightsStatementIdentifierType', req=True)
        linkingRightsStatementIdentifierValue = self._find(node, '{http://www.loc.gov/premis/v3}linkingRightsStatementIdentifierValue', req=True)

        linkingRightsStatementIdentifier = LinkingRightsStatementIdentifier(linkingRightsStatementIdentifierType, linkingRightsStatementIdentifierValue)

        return linkingRightsStatementIdentifier

    def buildFixity(self, node):
        messageDigestAlgorithm = self._find(node, '{http://www.loc.gov/premis/v3}messageDigestAlgorithm')
        messageDigest = self._find(node, '{http://www.loc.gov/premis/v3}messageDigest')

        fixity = Fixity(messageDigestAlgorithm, messageDigest)

        messageDigestOriginator = self._find(node, '{http://www.loc.gov/premis/v3}messageDigestOriginator')
        if messageDigestOriginator:
            fixity.set_messageDigestOriginator(messageDigestOriginator)

        return fixity

    def buildFormat(self, node):
        format = Format()

        formatDesignationNode = self._find_node(node, '{http://www.loc.gov/premis/v3}formatDesignation')
        if formatDesignationNode:
            formatDesignation = self.buildFormatDesignation(formatDesignationNode)
            format.set_formatDesignation(formatDesignation)

        formatRegistryNode = self._find_node(node, '{http://www.loc.gov/premis/v3}formatRegistry')
        if formatRegistryNode:
            formatRegistry = self.buildFormatRegistry(formatRegistryNode)
            format.set_formatRegistry(formatRegistry)

        formatNote = self._find_all(node, '{http://www.loc.gov/premis/v3}formatNote')
        if formatNote:
            format.set_formatNote(formatNote)

        return format

    def buildCreatingApplication(self, node):
        creatingApplication = CreatingApplication()

        creatingApplicationName = self._find(node, '{http://www.loc.gov/premis/v3}creatingApplicationName')
        if creatingApplicationName:
            creatingApplication.set_creatingApplicationName(creatingApplicationName)

        creatingApplicationVersion = self._find(node, '{http://www.loc.gov/premis/v3}creatingApplicationVersion')
        if creatingApplicationVersion:
            creatingApplication.set_creatingApplicationVersion(creatingApplicationVersion)

        dateCreatedByApplication = self._find(node, '{http://www.loc.gov/premis/v3}dateCreatedByApplication')
        if dateCreatedByApplication:
            creatingApplication.set_dateCreatedByApplication(dateCreatedByApplication)

        creatingApplicationExtension = self._find_all(node, '{http://www.loc.gov/premis/v3}creatingApplicationExtension')
        if creatingApplicationExtension:
            creatingApplication.set_creatingApplicationExtension(creatingApplicationExtension)

        return creatingApplication

    def buildInhibitors(self, node):
        inhibitorType = self._find(node, '{http://www.loc.gov/premis/v3}inhibitorType', req=True)

        inhibitors = Inhibitors(inhibitorType)

        inhibitorTarget = self._find_all(node, '{http://www.loc.gov/premis/v3}inhibitorTarget')
        if inhibitorTarget:
            inhibitors.set_inhibitorTarget(inhibitorTarget)

        inhibitorKey = self._find(node, '{http://www.loc.gov/premis/v3}inhibitorKey')
        if inhibitorKey:
            inhibitors.set_inhibitorKey(inhibitorKey)

        return inhibitors

    def buildContentLocation(self, node):
        contentLocationType = self._find(node, '{http://www.loc.gov/premis/v3}contentLocationType', req=True)
        contentLocationValue = self._find(node, '{http://www.loc.gov/premis/v3}contentLocationValue', req=True)

        contentLocation = ContentLocation(contentLocationType, contentLocationValue)

        return contentLocation

    def buildSignature(self, node):
        signatureEncoding = self._find(node, '{http://www.loc.gov/premis/v3}signatureEncoding', req=True)
        signatureMethod = self._find(node, '{http://www.loc.gov/premis/v3}signatureMethod', req=True)
        signatureValue = self._find(node, '{http://www.loc.gov/premis/v3}signatureValue', req=True)
        signatureValidationRules = self._find(node, '{http://www.loc.gov/premis/v3}signatureValidationRules', req=True)

        signature = Signature(signatureEncoding, signatureMethod, signatureValue, signatureValidationRules)

        signer = self._find(node, '{http://www.loc.gov/premis/v3}signer')
        if signer:
            signature.set_signer(signer)

        signatureProperties = self._find_all(node, '{http://www.loc.gov/premis/v3}signatureProperties')
        if signatureProperties:
            signature.set_signatureProperties(signatureProperties)

        keyInformation = self._find(node, '{http://www.loc.gov/premis/v3}keyInformation')
        if keyInformation:
            signature.set_keyInformation(keyInformation)

        return signature

    def buildRelatedObjectIdentifier(self, node):
        relatedObjectIdentifierType = self._find(node, '{http://www.loc.gov/premis/v3}relatedObjectIdentifierType', req=True)
        relatedObjectIdentifierValue = self._find(node, '{http://www.loc.gov/premis/v3}relatedObjectIdentifierValue', req=True)

        relatedObjectIdentifier = RelatedObjectIdentifier(relatedObjectIdentifierType, relatedObjectIdentifierValue)

        relatedObjectSequence = self._find(node, '{http://www.loc.gov/premis/v3}relatedObjectSequence')
        if relatedObjectSequence:
            relatedObjectIdentifier.set_relatedObjectSequence(relatedObjectSequence)

        return relatedObjectIdentifier

    def buildRelatedEventIdentifier(self, node):
        relatedEventIdentifierType = self._find(node, '{http://www.loc.gov/premis/v3}relatedEventIdentifierType', req=True)
        relatedEventIdentifierValue = self._find(node, '{http://www.loc.gov/premis/v3}relatedEventIdentifierValue', req=True)

        relatedEventIdentifier = RelatedEventIdentifier(relatedEventIdentifierType, relatedEventIdentifierValue)

        relatedEventSequence = self._find(node, '{http://www.loc.gov/premis/v3}relatedEventSequence')
        if relatedEventSequence:
            relatedEventIdentifier.set_relatedEventSequence(relatedEventSequence)

        return relatedEventIdentifier

    def buildFormatDesignation(self, node):
        formatName = self._find(node, '{http://www.loc.gov/premis/v3}formatName', req=True)
        formatDesignation = FormatDesignation(formatName)

        formatVersion = self._find(node, '{http://www.loc.gov/premis/v3}formatVersion')
        if formatVersion:
            formatDesignation.set_formatVersion(formatVersion)

        return formatDesignation

    def buildFormatRegistry(self, node):
        formatRegistryName = self._find(node, '{http://www.loc.gov/premis/v3}formatRegistryName', req=True)
        formatRegistryKey = self._find(node, '{http://www.loc.gov/premis/v3}formatRegistryKey', req=True)

        formatRegistry = FormatRegistry(formatRegistryName, formatRegistryKey)

        formatRegistryRole = self._find(node, '{http://www.loc.gov/premis/v3}formatRegistryRole')
        if formatRegistryRole:
            formatRegistry.set_formatRegistryRole(formatRegistryRole)

        return formatRegistry

    def buildEvent(self, node):
        eventIdentifier = self.buildEventIdentifier(self._find_node(node, '{http://www.loc.gov/premis/v3}eventIdentifier', req=True))
        eventType = self._find(node, '{http://www.loc.gov/premis/v3}eventType', req=True)
        eventDateTime = self._find(node, '{http://www.loc.gov/premis/v3}eventDateTime', req=True)

        event = Event(eventIdentifier, eventType, eventDateTime)

        eventDetailInformation = self._pn(self.buildEventDetailInformation, node, '{http://www.loc.gov/premis/v3}eventDetailInformation')
        if eventDetailInformation:
            event.set_eventDetailInformation(eventDetailInformation)

        eventOutcomeInformation = self._pn(self.buildEventOutcomeInformation, node, '{http://www.loc.gov/premis/v3}eventOutcomeInformation')
        if eventOutcomeInformation:
            event.set_eventOutcomeInformation(eventOutcomeInformation)

        linkingAgentIdentifier = self._pn(self.buildLinkingAgentIdentifier, node, '{http://www.loc.gov/premis/v3}linkingAgentIdentifier')
        if linkingAgentIdentifier:
            event.set_linkingAgentIdentifier(linkingAgentIdentifier)

        linkingObjectIdentifier = self._pn(self.buildLinkingObjectIdentifier, node, '{http://www.loc.gov/premis/v3}linkingObjectIdentifier')
        if linkingObjectIdentifier:
            event.set_linkingObjectIdentifier(linkingObjectIdentifier)

        return event

    def buildEventIdentifier(self, node):
        eventIdentifierType = self._find(node, '{http://www.loc.gov/premis/v3}eventIdentifierType', req=True)
        eventIdentifierValue = self._find(node, '{http://www.loc.gov/premis/v3}eventIdentifierValue', req=True)

        eventIdentifier = EventIdentifier(eventIdentifierType, eventIdentifierValue)

        return eventIdentifier

    def buildEventDetailInformation(self, node):
        eventDetailInformation = EventDetailInformation()

        eventDetail = self._find(node, '{http://www.loc.gov/premis/v3}eventDetail')
        if eventDetail:
            eventDetailInformation.set_eventDetail(eventDetail)

        eventDetailExtension = self._find_all(node, '{http://www.loc.gov/premis/v3}eventDetailExtension')
        if eventDetailExtension:
            eventDetailInformation.set_eventDetailExtension(eventDetailExtension)

        return eventDetailInformation

    def buildEventOutcomeInformation(self, node):
        eventOutcomeInformation = EventOutcomeInformation()

        eventOutcome = self._find(node, '{http://www.loc.gov/premis/v3}eventOutcome')
        if eventOutcome:
            eventOutcomeInformation.set_eventOutcome(eventOutcome)

        eventOutcomeDetail = self._pn(self.buildEventOutcomeDetail, node, '{http://www.loc.gov/premis/v3}eventOutcomeDetail')
        if eventOutcomeDetail:
            eventOutcomeInformation.set_eventOutcomeDetail(eventOutcomeDetail)

        return eventOutcomeInformation

    def buildLinkingAgentIdentifier(self, node):
        linkingAgentIdentifierType = self._find(node, '{http://www.loc.gov/premis/v3}linkingAgentIdentifierType', req=True)
        linkingAgentIdentifierValue = self._find(node, '{http://www.loc.gov/premis/v3}linkingAgentIdentifierValue', req=True)

        linkingAgentIdentifier = LinkingAgentIdentifier(linkingAgentIdentifierType, linkingAgentIdentifierValue)

        linkingAgentRole = self._find_all(node, '{http://www.loc.gov/premis/v3}linkingAgentRole')
        if linkingAgentRole:
            linkingAgentIdentifier.set_linkingAgentRole(linkingAgentRole)

        return linkingAgentIdentifier

    def buildLinkingObjectIdentifier(self, node):
        linkingObjectIdentifierType = self._find(node, '{http://www.loc.gov/premis/v3}linkingObjectIdentifierType', req=True)
        linkingObjectIdentifierValue = self._find(node, '{http://www.loc.gov/premis/v3}linkingObjectIdentifierValue', req=True)

        linkingObjectIdentifier = LinkingObjectIdentifier(linkingObjectIdentifierType, linkingObjectIdentifierValue)

        linkingObjectRole = self._find_all(node, '{http://www.loc.gov/premis/v3}linkingObjectRole')
        if linkingObjectRole:
            linkingObjectIdentifier.set_linkingObjectRole(linkingObjectRole)

        return linkingObjectIdentifier

    def buildEventOutcomeDetail(self, node):
        eventOutcomeDetail = EventOutcomeDetail()

        eventOutcomeDetailNote = self._find(node, '{http://www.loc.gov/premis/v3}eventOutcomeDetailNote')
        if eventOutcomeDetailNote:
            eventOutcomeDetail.set_eventOutcomeDetailNote(eventOutcomeDetailNote)

        eventOutcomeDetailExtension = self._find_all(node, '{http://www.loc.gov/premis/v3}eventOutcomeDetailExtension')
        if eventOutcomeDetailExtension:
            eventOutcomeDetail.set_eventOutcomeDetailExtension(eventOutcomeDetailExtension)

        return eventOutcomeDetail
