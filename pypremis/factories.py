import xml.etree.ElementTree as ET

from pypremis.nodes import *


class XMLNodeFactory(object):
    def __init__(self, xmlfile):
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
        if not parse and req:
            raise ValueError("The {} tag is required but was not found.".format(tag))
        result = parse.text
        return result

    def _find_node(self, node, tag, req=False):
        parse = node.find(tag)
        if not parse and req:
            raise ValueError("The {} tag is required but was not found.".format(tag))
        return parse

    def _find_all_nodes(self, node, tag, req=False):
        parse = node.findall(tag)
        if not parse and req:
            raise ValueError("The {} tag is required but was not found.".format(tag))
        return parse

    def _process_nodes(self, func, node, tag, req=False):
        parse = self._find_all_nodes(node, tag, req)
        result = [func(x) for x in parse]
        return result

    def _pn(self, func, node, tag, req=False):
        return self._process_nodes(func, node, tag, req)

    def buildObject(self, node):
        objIDs = self._pn(buildObjectIdentifier, node, 'premis:objectIdentifier', req=True)
        objectCategory = self._find('premis:objectCategory', req=True)
        objectCharacteristics = self._pn(buildObjectCharacteristics, node, 'premis:objectCharacteristics', req=True)
        obj = Object(objIDs, objectCategory, objectCharacteristics)

        preservationLevel = self._pn(buildPreservationLevel, node, 'premis:preservationLevel')
        obj.set_preservationLevel(preservationLevel)

        significantProperties = self._pn(buildSignificantProperties, node, 'premis:significantProperties')
        obj.set_significantProperties(significantProperties)

        obj.set_originalName(self._find('premis:originalName'))

        storage = self._pn(buildStorage, node, 'premis:storage')
        obj.set_storage(storage)

        signatureInformation = self._pn(buildSignatureInformation, node, 'premis:signatureInformation')
        obj.set_signatureInformation(signatureInformation)

        environmentFunction = self._pn(buildEnvironmentFunction, node, 'premis:environmentFunction')
        obj.set_environmentFunction(environmentFunction)

        environmentDesignation = self._pn(buildEnvironmentDesignation, node, 'premis:environmentDesignation')
        obj.set_environmentDesignation(environmentDesignation)

        environmentRegistry = self._pn(buildEnvironmentRegistry, node, 'premis:environmentRegistry')
        obj.set_environmentRegistry(environmentRegistry)

        environmentExtension = self._find_all(node, 'premis:environmentExtension')
        obj.set_environmentExtension(environmentExtension)

        relationship = self._pn(buildRelationship, node, 'premis:relationship')
        obj.set_relationship(relationship)

        linkingEventIdentifier = self._pn(buildLinkingEventIdentifier, node, 'premis:linkingEventIdentifier')
        obj.set_linkingEventIdentifier(linkingEventIdentifier)

        linkingRightsStatementIdentifier = self._pn(buildLinkingRightsStatementIdentifier, node, 'premis:linkingRightsStatementIdentifier')
        obj.set_linkingRightsStatementIdentifier(linkingRightsStatementIdentifier)

        return obj

    def buildObjectIdentifier(self, node):
        objectIdentifierType = self._find(node, 'premis:objectIdentifierType', req=True)
        objectIdentifierValue = self._find(node, 'premis:objectIdentifierValue', req=True)
        objID = ObjectIdentifier(objectIdentifierType, objectIdentifierValue)
        return objID

    def buildPreservationLevel(self, node):
        preservationLevelValue = self._find(node, 'premis:preservationLevelValue', req=True)
        preservationLevel = PreservationLevel(preservationLevelValue)

        preservationLevelType = self._find(node, 'premis:preservationLevelType')
        preservationLevel.set_preservationLevelType(preservationLevelType)

        preservationLevelRole = self._find(node, 'premis:preservationLevelRole')
        preservationLevel.set_preservationLevelRole(preservationLevelRole)

        preservationLevelRationale = self._find_all(node, 'premis:preservationLevelRationale')
        preservationLevel.set_preservationLevelRationale(preservationLevelRationale)

        preservationLevelDateAssigned = self._find(node, 'premis:preservationLevelDateAssigned')
        preservationLevel.set_preservationLevelDateAssigned(preservationLevelDateAssigned)

        return preservationLevel

    def buildSignificantProperties(self, node):
        significantProperties = SignificantProperties()

        significantPropertiesType = self._find(node, 'premis:significantPropertiesType')
        significantProperties.set_significantPropertiesType(significantPropertiesType)

        significantPropertiesValue = self._find(node, 'premis:significantPropertiesValue')
        significantProperties.set_significantPropertiesValue(significantPropertiesValue)

        significantPropertiesExtension = self._find_all(node, 'premis:significantPropertiesExtension')
        significantProperties.set_significantPropertiesExtension(significantPropertiesExtension)

        return significantProperties

    def buildObjectCharacteristics(self, node):
        format = self._pn(buildFormat, node, 'premis:format', req=True)
        objectCharacteristics = ObjectCharacteristics(format)

        compositionLevel = self._find(node, 'premis:compositionLevel')
        objectCharacteristics.set_compositionLevel(compositionLevel)

        fixity = self._pn(buildFixity, node, 'premis:fixity')
        objectCharacteristics.set_fixity(fixity)

        size = self._find(node, 'premis:size')
        objectCharacteristics.set_size(size)

        creatingApplication = self._pn(buildCreatingApplicable, node, 'premis:creatingApplication')
        objectCharacteristics.set_creatingApplication(creatingApplication)

        inhibitors = self.pn(buildInhibitors, node, 'premis:inhibitors')
        objectCharacteristics.set_inhibitors(inhibitors)

        objectCharacteristicsExtension = self._find_all(node, 'premis:objectCharacteristicsExtension')
        objectCharacteristics.set_objectCharacteristicsExtension(objectCharacteristicsExtension)

        return objectCharacteristics

    def buildStorage(self, node):
        storage = Storage()

        contentLocation = buildContentLocation(self._find_node(node, 'premis:contentLocation'))
        storage.set_contentLocation(contentLocation)

        storageMedium = self._find('premis:storageMedium')
        storage.set_storageMedium(storageMedium)

        return storage

    def buildSignatureInformation(self, node):
        signatureInformation = SignatureInformation()

        signature = self._pn(buildSignature, node, 'premis:signature')
        signatureInformation.set_signature(signature)

        signatureInformationExtension = self._find_all('premis:signatureInformationExtension')
        signatureInformation.set_signatureInformationExtension(signatureInformationExtension)

        return signatureInformation

    def buildEnvironmentFunction(self, node):
        environmentFunctionType = self._find(node, 'premis:environmentFunctionType', req=True)
        environmentFunctionLevel = self._find(node, 'premis:environmentFunctionLevel', req=True)

        environmentFunction = EnvironmentFunction(environmentFunctionType, environmentFunctionLevel)

        return environmentFunction

    def buildEnvironmentDesignation(self, node):
        environmentDesignationName = self._find(node, 'premis:environmentDesignationName', req=True)

        environmentDesignation = EnvironmentDesignation(environmentDesignationName)

        environmentVersion = self._find(node, 'premis:environmentVersion')
        environmentDesignation.set_environmentVersion(environmentVersion)

        environmentOrigin = self._find(node, 'premis:environmentOrigin')
        environmentDesignation.set_environmentOrigin(environmentOrigin)

        environmentDesignationNote = self._find_all(node, 'premis:environmentDesignationNote')
        environmentDesignation.set_environmentDesignationNode(environmentDesignationNote)

        environmentDesignationExtension = self._find_all(node, 'premis:environmentDesignationExtension')
        environmentDesignation.set_environmentDesignationExtension(environmentDesignationExtension)

        return environmentDesignation

    def buildEnvironmentRegistry(self, node):
        environmentRegistryName = self._find(node, 'premis:environmentRegistryNode', req=True)
        environmentRegistryKey = self._find(node, 'premis:environmentRegistryKey', req=True)

        environmentRegistry = EnvironmentRegistry(environmentRegistryName, environmentRegistryKey)

        environmentRegistryRole = self._find(node, 'premis:environmentRegistryRole')
        environmentRegistry.set_environmentRegistryRole(environmentRegistryRole)

        return environmentRegistry

    def buildRelationship(self, node):
        relationshipType = self._find(node, 'premis:relationshipType', req=True)
        relationshipSubType = self._find(node, 'premis:relationshipSubType', req=True)
        relatedObjectIdentifier = self._pn(buildRelatedObjectIdentifier, node, 'premis:relatedObjectIdentifier', req=True)

        relationship = Relationship(relationshipType, relationshipSubType, relatedObjectIdentifier)

        relatedEventIdentifier = self._pn(buildRelatedEventIdentifier, node, 'premis:relatedEventIdentifier')
        relationship.set_relatedEventIdentifier(relatedEventIdentifier)

        relatedEnvironmentPurpose = self._find_all(node, 'premis:relatedEnvironmentPurpose')
        relationship.set_relatedEnvironmentPurpose(relatedEnvironmentPurpose)

        relatedEnvironmentCharacteristic = self._find(node, 'premis:relatedEnvironmentCharacteristic')
        relationship.set_relatedEnvironmentCharacteristic(relatedEnvironmentCharacteristic)

        return relationship

    def buildLinkingEventIdentifier(self, node):
        linkingEventIdentifierType = self._find(node, 'premis:linkingEventIdentifierType', req=True)
        linkingEventIdentifierValue = self._find(node, 'premis:linkingEventIdentifierValue', req=True)

        linkingEventIdentifier = LinkingEventIdentifier(linkingEventIdentifierType, linkingEventIdentifierValue)

        return linkingEventIdentifier

    def buildLinkingRightsStatementIdentifier(self, node):
        linkingRightsStatementIdentifierType = self._find(node, 'premis:linkingRightsStatementIdentifierType', req=True)
        linkingRightsStatementIdentifierValue = self._find(node, 'premis:linkingRightsStatementIdentifierValue', req=True)

        linkingRightsStatementIdentifier = LinkingRightsStatementIdentifier(linkingRightsStatementIdentifierType, linkingRightsStatementIdentifierValue)

        return linkingRightsStatementIdentifier

    def buildFixity(self, node):
        messageDigestAlgorithm = self._find(node, 'premis:messageDigestAlgorithm')
        messageDigest = self._find(node, 'premis:messageDigest')

        fixity = Fixity(messageDigestAlgorithm, messageDigest)

        messageDigestOriginator = self._find(node, 'premis:messageDigestOriginator')
        fixity.set_messageDigestOriginator(messageDigestOriginator)

        return fixity

    def buildFormat(self, node):
        format = Format()

        formatDesignation = self.buildFormatDesignation(self._find_node(node, 'premis:formatDesignation'))
        format.set_formatDesignation(formatDesignation)

        formatRegistry = self.buildFormatRegistry(self._find_node(node, 'premis:formatRegistry'))
        format.set_formatRegistry(formatRegistry)

        formatNote = self._find_all(node, 'premis:formatNote')
        format.set_formatNote(formatNote)

        return format

    def buildCreatingApplication(self, node):
        creatingApplication = CreatingApplication()

        creatingApplicationName = self._find(node, 'premis:creatingApplicationName')
        creatingApplication.set_creatingApplicationName(creatingApplicationName)

        creatingApplicationVersion = self._find(node, 'premis:creatingApplicationVersion')
        creatingApplication.set_creatingApplicationVersion(creatingApplicationVersion)

        dateCreatedByApplication = self._find(node, 'premis:dateCreatedByApplication')
        creatingApplication.set_dateCreatedByApplication(dateCreatedByApplication)

        creatingApplicationExtension = self._find_all(node, 'premis:creatingApplicationExtension')
        creatingApplication.set_creatingApplicationExtension(creatingApplicationExtension)

        return creatingApplication

    def buildInhibitors(self, node):
        inhibitorType = self._find(node, 'premis:inhibitorType', req=True)

        inhibitor = Inhibitor(inhibitorType)

        inhibitorTarget = self._find_all(node, 'premis:inhibitorTarget')
        inhibitor.set_inhibitorTarget(inhibitorTarget)

        inhibitorKey = self._find(node, 'premis:inhibitorKey')
        inhibitor.set_inhibitorKey(inhibitorKey)

        return inhibitor

    def buildContentLocation(self, node):
        contentLocationType = self._find(node, 'premis:contentLocationType', req=True)
        contentLocationValue = self._find(node, 'premis:contentLocationValue', req=True)

        contentLocation = ContentLocation(contentLocationType, contentLocationValue)

        return contentLocation

    def buildSignature(self, node):
        signatureEncoding = self._find(node, 'premis:signatureEncoding', req=True)
        signatureMethod = self._find(node, 'premis:signatureMethod', req=True)
        signatureValue = self._find(node, 'premis:signatureValue', req=True)
        signatureValidationRules = self._find(node, 'premis:signatureValidationRules', req=True)

        signature = Signature(signatureEncoding, signatureMethod, signatureValue, signatureValidationRules)

        signer = self._find(node, 'premis:signer')
        signature.set_signer(signer)

        signatureProperties = self._find_all(node, 'premis:signatureProperties')
        signature.set_signatureProperties(signatureProperties)

        keyInformation = self._find(node, 'premis:keyInformation')
        signature.set_keyInformation(keyInformation)

        return signature

    def buildRelatedObjectIdentifier(self, node):
        relatedObjectIdentifierType = self._find(node, 'premis:relatedObjectIdentifierType', req=True)
        relatedObjectIdentifierValue = self._find(node, 'premis:relatedObjectIdentifierValue', req=True)

        relatedObjectIdentifier = RelatedObjectIdentifier(relatedObjectIdentifierType, relatedObjectIdentifierValue)

        relatedObjectSequence = self._find(node, 'premis:relatedObjectSequence')
        relatedObjectIdentifier.set_relatedObjectSequence(relatedObjectSequence)

        return relatedObjectIdentifier

    def buildRelatedEventIdentifier(self, node):
        relatedEventIdentifierType = self._find(node, 'premis:relatedEventIdentifierType', req=True)
        relatedEventIdentifierValue = self._find(node, 'premis:relatedEventIdentifierValue', req=True)

        relatedEventIdentifier = RelatedEventIdentifier(relatedEventIdentifierType, relatedEventIdentifierValue)

        relatedEventSequence = self._find(node, 'premis:relatedEventSequence')
        relatedEventIdentifier.set_relatedEventSequence(relatedEventSequence)

        return relatedEventIdentifier

    def buildFormatDesignation(self, node):
        formatName = self._find(node, 'premis:formatName', req=True)
        formatDesignation = FormatDesignation(formatName)

        formatVersion = self._find(node, 'premis:formatDesignation')
        formatDesignation.set_formatVersion(formatVersion)

        return formatDesignation

    def buildFormatRegistry(self, node):
        formatRegistryName = self._find(node, 'premis:formatRegistryName', req=True)
        formatRegistryKey = self._find(node, 'premis:formatRegistryKey', req=True)

        formatRegistry = FormatRegistry(formatRegistryName, formatRegistryKey)

        formatRegistryRole = self._find(node, 'premis:formatRegistryRole')
        formatRegistry.set_formatRegistryRole(formatRegistryRole)

        return formatRegistry
