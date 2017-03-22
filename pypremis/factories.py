import xml.etree.ElementTree as ET
from abc import ABCMeta, abstractmethod

from pypremis.nodes import *

"""
### Factory classes for building pypremis nodes from serializations ###

1. **XMLNodeFactory** is a class implementing .find_objects(), .find_events(),
.find_rights(), and .find_agents() meant to build PremisNode instances from
valid premis XML records
"""


class XMLNodeFactory(object):
    """
    A class for ingesting an xml document and building PremisNodes out of it.

    __Attributes__

    1. xml: an ElementTree xml Element object meant to act as the root to attach
    objects too from the xml.
    """
    def __init__(self, xmlfile):
        """
        Initializes an XML node factory and points it to a PREMIS xml file
        to be used to build PremisNode instances.

        __Args__

        1. xmlfile: the path to a PREMIS xml serialization on disk
        """
        ET.register_namespace('premis', "http://www.loc.gov/premis/v3")
        ET.register_namespace('xsi', "http://www.w3.org/2001/XMLSchema-instance")
        tree = ET.parse(xmlfile)
        self.xml = tree.getroot()

    def _find_all(self, node, tag, req=False):
        """
        Searches a given Element instance for all values corresponding to the
        given [tag] in [node].

        __Args__

        1. node (ET.Element): an ElementTree Element instance to search
        2. tag (str): a string, the tag name to find

        __KWArgs__

        * req (bool): A bool, if set to true and no nodes are found raise a ValueError

        __Returns__

        * (list): a list of strings (the values)
        """
        parse = [x for x in node.findall(tag)]
        if len(parse) < 1 and req:
            raise ValueError("The {} tag is required but was not found.".format(tag))
        result = [x.text for x in parse]
        return result

    def _find(self, node, tag, req=False):
        """
        Searches a given Element instance for the value corresponding to the
        given [tag] in [node].

        __Args__

        1. node (ET.Element): an ElementTree Element instance to search
        2. tag (str): a string, the tag name to find

        __KWArgs__

        * req (bool): A bool, if set to true if no element with that tag is found
        in the given node raise a ValueError

        __Returns__

        * (str): the value
        """
        parse = node.find(tag)
        if parse is None and req:
            raise ValueError("The {} tag is required but was not found.".format(tag))
        try:
            result = parse.text
            return result
        except AttributeError:
            return ""

    def _find_node(self, node, tag, req=False):
        """
        Searches a given Element instance for a tag and returns the whole
        Element instances which has that tag.

        __Args__

        1. node (ET.Element): an ElementTree Element instance to search
        2. tag (str): a string, the tag to find

        __KWArgs__

        * req (bool): A bool, if set to true if no element with the specified tag
        in the specified node is found raise a ValueError

        __Returns__

        * (ET.Element): the node
        """
        parse = node.find(tag)
        if parse is None and req:
            raise ValueError("The {} tag is required but was not found.".format(tag))
        if parse is None:
            return False
        return parse

    def _find_all_nodes(self, node, tag, req=False):
        """
        Searches a given Element instance for a tag and returns a list of
        Element instances which have that tag.

        __Args__

        1. node (ET.Element): an ElementTree Element instance to search
        2. tag (str): a string, the tag to find

        __KWArgs__

        * req (bool): A bool, if set to true if no element with the specified tag is
        found in the given node raise a ValueError

        __Returns__

        * (list): a list of ET.Elements
        """
        parse = node.findall(tag)
        if not parse and req:
            raise ValueError("The {} tag is required but was not found.".format(tag))
        if parse is None:
            return False
        return parse

    def _process_nodes(self, func, node, tag, req=False):
        """
        Search a given [node] for all children with the the given [tag].
        Feed the resulting list, item by item, into a function. Return
        a list of the function return values for each entry in the original
        list.

        __Args__

        1. func (func): A function to be used to process the nodes
        2. node (ET.Element): A node to search for children to process
        3. tag (str): The tag of the children which will be processed by the function

        __KWArgs__

        * req (bool): A bool, if set to True if no element with the specified tag is
        found in the given node instance raise a ValueError

        __Returns__

        * (list or False): A list of PremisNodes, or False if no applicable
        nodes were found.
        """
        parse = self._find_all_nodes(node, tag, req)
        if parse:
            result = [func(x) for x in parse]
            return result
        return False

    def _pn(self, func, node, tag, req=False):
        """
        wraps ._process_nodes(), because I got tired of typing the whole thing
        so many times.
        """
        return self._process_nodes(func, node, tag, req)

    def find_objects(self):
        """
        finds all of the objects in an xml record and builds Object PremisNodes
        from them. Returns a list of these nodes.

        __Returns__

        * (list): a list of built PremisNode.Objects
        """
        return [self.buildObject(x) for x in self._find_all_nodes(self.xml, '{http://www.loc.gov/premis/v3}object')]

    def find_agents(self):
        """
        finds all of the agents in an xml record and builds Agent PremisNodes
        from them. Returns a list of these nodes.

        __Returns__

        * (list): a list of built PremisNode.Agents
        """
        return [self.buildAgent(x) for x in self._find_all_nodes(self.xml, '{http://www.loc.gov/premis/v3}agent')]

    def find_events(self):
        """
        finds all of the events in an xml record and builds Event PremisNodes
        from them. Returns a list of these nodes.

        __Rturns__

        * (list): a list of built PremisNode.Events
        """
        return [self.buildEvent(x) for x in self._find_all_nodes(self.xml, '{http://www.loc.gov/premis/v3}event')]

    def find_rights(self):
        """
        finds all of the rights in an xml record and builds Rights PremisNodes
        from them. Returns a list of these nodes.

        __Returns__

        * (list): a list of built PremisNode.Rights...'s?
        """
        return [self.buildRights(x) for x in self._find_all_nodes(self.xml, '{http://www.loc.gov/premis/v3}rights')]

    def buildExtensionNode(self, node):
        """
        build an uncontrolled ExtensionNode PremisNode and return it.

        __Args__

        1. node (ET.Element): an ElementTree Element instance to turn into a PremisNode
        ExtensionNode instance.

        __Returns__

        * (ExtensionNode): the built ExtensionNode
        """
        result = ExtensionNode()
        for child in node:
            if len(child) == 0:
                result.add_to_field(child.tag, child.text)
            else:
                result.add_to_field(child.tag, self.buildExtensionNode(child))
        return result

    def buildExtendedNode(self, extendedNode, node):
        """
        Wraps tacking Extension nodes to extended nodes.

        __Args__

        1. extendedNode (cls): a class, the specific ExtendedNode PremisNode
        2. node (ET.Element): the ElementTree Element instance to turn into an
        ExtendedNode PremisNode instance.

        __Returns__

        * (ExtendedNode): the built ExtendedNode
        """
        result = extendedNode()
        for child in node:
            if len(child) == 0:
                result.add_to_field(child.tag, child.text)
            else:
                result.add_to_field(child.tag, self.buildExtensionNode(child))
        return result

    # From here on out each of these functions takes one ElementTree Element
    # instance as an arg. It runs different searches and functions over
    # that Element instance in order to construct a PremisNode instance of
    # a given type, respecting the cardinality and requirement statements
    # in the PREMISv3 data dictionary.

    def buildSignificantPropertiesExtension(self, node):
        return self.buildExtendedNode(SignificantPropertiesExtension, node)

    def buildCreatingApplicationExtension(self, node):
        return self.buildExtendedNode(CreatingApplicationExtension, node)

    def buildObjectCharacteristicsExtension(self, node):
        return self.buildExtendedNode(ObjectCharacteristicsExtension, node)

    def buildKeyInformation(self, node):
        return self.buildExtendedNode(KeyInformation, node)

    def buildSignatureInformationExtension(self, node):
        return self.buildExtendedNode(SignatureInformationExtension, node)

    def buildEnvironmentDesignationExtension(self, node):
        return self.buildExtendedNode(EnvironmentDesignationExtension, node)

    def buildEnvironmentExtension(self, node):
        return self.buildExtendedNode(EnvironmentExtension, node)

    def buildEventDetailExtension(self, node):
        return self.buildExtendedNode(EventDetailExtension, node)

    def buildEventOutcomeDetailExtension(self, node):
        return self.buildExtendedNode(EventOutcomeDetailExtension, node)

    def buildAgentExtension(self, node):
        return self.buildExtendedNode(AgentExtension, node)

    def buildRightsExtension(self, node):
        return self.buildExtendedNode(RightsExtension, node)

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
            obj.set_environmentExtension(self._pn(self.buildEnvironmentExtension, node, '{http://www.loc.gov/premis/v3}environmentExtension'))

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
        significantPropertiesValue = None
        significantPropertiesExtension = None

        significantPropertiesValue = self._find(node, '{http://www.loc.gov/premis/v3}significantPropertiesValue')
        significantPropertiesExtension = self._find_all_nodes(node, '{http://www.loc.gov/premis/v3}significantPropertiesExtension')

        if not (significantPropertiesValue or significantPropertiesExtension):
            raiseValueError('missing required significantPropertiesValue or significantPropertiesExtension')
        elif significantPropertiesValue and not significantPropertiesExtension:
            significantProperties = SignificantProperties(significantPropertiesValue=significantPropertiesValue)
        elif significantPropertiesExtension and not significantPropertiesValue:
            significantProperties = SignificantProperties(significantPropertiesExtension=self._pn(self.buildSignificantPropertiesExtension, node, '{http://www.loc.gov/premis/v3}significantPropertiesExtension'))
        else:
            significantProperties = SignificantProperties(significantPropertiesValue=significantPropertiesValue, significantPropertiesExtension=self._pn(self.buildSignificantPropertiesExtension, node, '{http://www.loc.gov/premis/v3}significantPropertiesExtension'))

        significantPropertiesType = self._find(node, '{http://www.loc.gov/premis/v3}significantPropertiesType')
        if significantPropertiesType:
            significantProperties.set_significantPropertiesType(significantPropertiesType)

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
            objectCharacteristics.set_objectCharacteristicsExtension(self._pn(self.buildObjectCharacteristicsExtension, node, '{http://www.loc.gov/premis/v3}objectCharacteristicsExtension'))

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
            signatureInformation.set_signatureInformationExtension(self._pn(self.buildSignatureInformationExtension, node, '{http://www.loc.gov/premis/v3}signatureInformationExtension'))

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
            environmentDesignation.set_environmentDesignationExtension(self._pn(self.buildEnvironmentDesignationExtension, node, '{http://www.loc.gov/premis/v3}environmentDesignationExtension'))

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
        formatDesignation = None
        formatRegistry = None

        formatDesignationNode = self._find_node(node, '{http://www.loc.gov/premis/v3}formatDesignation')
        if formatDesignationNode:
            formatDesignation = self.buildFormatDesignation(formatDesignationNode)

        formatRegistryNode = self._find_node(node, '{http://www.loc.gov/premis/v3}formatRegistry')
        if formatRegistryNode:
            formatRegistry = self.buildFormatRegistry(formatRegistryNode)

        if not (formatDesignation or formatRegistry):
            raise ValueError("missing essential node: formatDesignation or formatRegistry")
        elif formatDesignation and not formatRegistry:
            format = Format(formatDesignation=formatDesignation)
        elif formatRegistry and not formatDesignation:
            format = Format(formatRegistry=formatRegistry)
        else:
            format = Format(formatDesignation=formatDesignation, formatRegistry=formatRegistry)

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
            creatingApplication.set_creatingApplicationExtension(self._pn(self.buildCreatingApplicationExtension, node, '{http://www.loc.gov/premis/v3}creatingApplicationExtension'))

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

        keyInformationNode = self._find_node(node, '{http://www.loc.gov/premis/v3}keyInformation')
        if keyInformationNode:
            signature.set_keyInformation(self.buildKeyInformation(keyInformationNode))

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
        eventDetail = self._find(node, '{http://www.loc.gov/premis/v3}eventDetail')
        eventDetailExtension = self._find_all(node, '{http://www.loc.gov/premis/v3}eventDetailExtension')

        if not (eventDetail or eventDetailExtension):
            raise ValueError("eventDetail and/or eventDetailExtension must be present in order to construct an eventDetailInformation node.")
        elif eventDetail and not eventDetailExtension:
            eventDetailInformation = EventDetailInformation(eventDetail=eventDetail)
        elif eventDetailExtension and not eventDetail:
            eventDetailInformation = EventDetailInformation(eventDetailExtension=self._pn(self.buildEventDetailExtension, node, '{http://www.loc.gov/premis/v3}eventDetailExtension'))
        else:
            eventDetailInformation = EventDetailInformation(eventDetail=eventDetail, eventDetailExtension=self._pn(self.buildEventDetailExtension, node, '{http://www.loc.gov/premis/v3}eventDetailExtension'))
        return eventDetailInformation

    def buildEventOutcomeInformation(self, node):
        eventOutcome = self._find(node, '{http://www.loc.gov/premis/v3}eventOutcome')
        eventOutcomeDetail = self._pn(self.buildEventOutcomeDetail, node, '{http://www.loc.gov/premis/v3}eventOutcomeDetail')

        if not (eventOutcome or eventOutcomeDetail):
            raise ValueError("eventOutcome and/or eventOutcomeExtension must be present in order to construct an eventOutcomeInformation node.")
        elif eventOutcome and not eventOutcomeDetail:
            eventOutcomeInformation = EventOutcomeInformation(eventOutcome=eventOutcome)
        elif eventOutcomeDetail and not eventOutcome:
            eventOutcomeInformation = EventOutcomeInformation(eventOutcomeDetail=eventOutcomeDetail)
        else:
            eventOutcomeInformation = EventOutcomeInformation(eventOutcome=eventOutcome, eventOutcomeDetail=eventOutcomeDetail)

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
        eventOutcomeDetailNote = self._find(node, '{http://www.loc.gov/premis/v3}eventOutcomeDetailNote')
        eventOutcomeDetailExtension = self._find_all(node, '{http://www.loc.gov/premis/v3}eventOutcomeDetailExtension')

        if not (eventOutcomeDetailNote or eventOutcomeDetailExtension):
            raise ValueError("eventOutcomeDetailNote and/or eventOutcomeDetailExtension required to construct an eventOutcomeDetail node.")
        elif eventOutcomeDetailNote and not eventOutcomeDetailExtension:
            eventOutcomeDetail = EventOutcomeDetail(eventOutcomeDetailNote=eventOutcomeDetailNote)
        elif eventOutcomeDetailExtension and not eventOutcomeDetailExtension:
            eventOutcomeDetail = EventOutcomeDetail(eventOutcomeDetailExtension=self._pn(self.buildEventOutcomeDetailExtension, node, '{http://www.loc.gov/premis/v3}eventOutcomeDetailExtension'))
        else:
            eventOutcomeDetail = EventOutcomeDetail(eventOutcomeDetailNote=eventOutcomeDetailNote, eventOutcomeDetailExtension=self._pn(self.buildEventOutcomeDetailExtension, node, '{http://www.loc.gov/premis/v3}eventOutcomeDetailExtension'))

        return eventOutcomeDetail

    def buildAgent(self, node):
        agentIdentifier = self._pn(self.buildAgentIdentifier, node, '{http://www.loc.gov/premis/v3}agentIdentifier', req=True)

        agent = Agent(agentIdentifier)

        agentName = self._find_all(node, '{http://www.loc.gov/premis/v3}agentName')
        if agentName:
            agent.set_agentName(agentName)

        agentType = self._find(node, '{http://www.loc.gov/premis/v3}agentType')
        if agentType:
            agent.set_agentType(agentType)

        agentVersion = self._find(node, '{http://www.loc.gov/premis/v3}agentVersion')
        if agentVersion:
            agent.set_agentVersion(agentVersion)

        agentNote = self._find_all(node, '{http://www.loc.gov/premis/v3}agentNote')
        if agentNote:
            agent.set_agentNote(agentNote)

        agentExtension = self._find_all(node, '{http://www.loc.gov/premis/v3}agentExtension')
        if agentExtension:
            agent.set_agentExtension(self._pn(self.buildAgentExtension, node, '{http://www.loc.gov/premis/v3}agentExtension'))

        linkingEventIdentifier = self._pn(self.buildLinkingEventIdentifier, node, '{http://www.loc.gov/premis/v3}linkingEventIdentifier')
        if linkingEventIdentifier:
            agent.set_linkingEventIdentifier(linkingEventIdentifier)

        linkingRightsStatementIdentifier = self._pn(self.buildLinkingRightsStatementIdentifier, node, '{http://www.loc.gov/premis/v3}linkingRightsStatementIdentifier')
        if linkingRightsStatementIdentifier:
            agent.set_linkingRightsStatementIdentifier(linkingRightsStatementIdentifier)

        linkingEnvironmentIdentifier = self._pn(self.buildLinkingEnvironmentIdentifier, node, '{http://www.loc.gov/premis/v3}linkingEnvironmentIdentifier')
        if linkingEnvironmentIdentifier:
            agent.set_linkingEnvironmentIdentifier(linkingEnvironmentIdentifier)

        return agent

    def buildAgentIdentifier(self, node):
        agentIdentifierType = self._find(node, '{http://www.loc.gov/premis/v3}agentIdentifierType', req=True)
        agentIdentifierValue = self._find(node, '{http://www.loc.gov/premis/v3}agentIdentifierValue', req=True)

        agentIdentifier = AgentIdentifier(agentIdentifierType, agentIdentifierValue)

        return agentIdentifier

    def buildLinkingEnvironmentIdentifier(self, node):
        linkingEnvironmentIdentifierType = self._find(node, '{http://www.loc.gov/premis/v3}linkingEnvironmentIdentifierType', req=True)
        linkingEnvironmentIdentifierValue = self._find(node, '{http://www.loc.gov/premis/v3}linkingEnvironmentIdentifierValue', req=True)

        linkingEnvironmentIdentifier = LinkingEnvironmentIdentifier(linkingEnvironmentIdentifierType, linkingEnvironmentIdentifierValue)

        linkingEnvironmentRole = self._find_all(node, '{http://www.loc.gov/premis/v3}linkingEnvironmentRole')
        if linkingEnvironmentRole:
            linkingEnvironmentIdentifier.set_linkingEnvironmentRole(linkingEnvironmentRole)

        return linkingEnvironmentIdentifier

    def buildRights(self, node):
        rightsStatement = self._pn(self.buildRightsStatement, node, '{http://www.loc.gov/premis/v3}rightsStatement')
        rightsExtension = self._find_all(node, '{http://www.loc.gov/premis/v3}rightsExtension')

        if not (rightsStatement or rightsExtension):
            raise ValueError("Either a rightsStatement or a rightsExtension must be present.")
        elif rightsStatement and not rightsExtension:
            rights = Rights(rightsStatement=rightsStatement)
        elif rightsExtension and not rightsStatement:
            rights = Rights(rightsExtension=self._pn(self.buildRightsExtension, node, '{http://www.loc.gov/premis/v3}rightsExtension'))
        else:
            rights = Rights(rightsStatement=rightsStatement, rightsExtension=self._pn(self.buildRightsExtension, node, '{http://www.loc.gov/premis/v3}rightsExtension'))

        return rights

    def buildRightsStatement(self, node):
        rightsStatementIdentifierNode = self._find_node(node, '{http://www.loc.gov/premis/v3}rightsStatementIdentifier', req=True)
        rightsStatementIdentifier = self.buildRightsStatementIdentifier(rightsStatementIdentifierNode)
        rightsBasis = self._find(node, '{http://www.loc.gov/premis/v3}rightsBasis', req=True)

        rightsStatement = RightsStatement(rightsStatementIdentifier, rightsBasis)

        copyrightInformationNode = self._find_node(node, '{http://www.loc.gov/premis/v3}copyrightInformation')
        if copyrightInformationNode:
            copyrightInformation = self.buildCopyrightInformation(copyrightInformationNode)
            rightsStatement.set_copyrightInformation(copyrightInformation)

        licenseInformationNode = self._find_node(node, '{http://www.loc.gov/premis/v3}licenseInformation')
        if licenseInformationNode:
            licenseInformation = self.buildLicenseInformation(licenseInformationNode)
            rightsStatement.set_licenseInformation(licenseInformation)

        statuteInformation = self._pn(self.buildStatuteInformation, node, '{http://www.loc.gov/premis/v3}statuteInformation')
        if statuteInformation:
            rightsStatement.set_statuteInformation(statuteInformation)

        otherRightsInformationNode = self._find_node(node, '{http://www.loc.gov/premis/v3}otherRightsInformation')
        if otherRightsInformationNode:
            otherRightsInformation = self.buildOtherRightsInformation(otherRightsInformationNode)
            rightsStatement.set_otherRightsInformation(otherRightsInformation)

        rightsGranted = self._pn(self.buildRightsGranted, node, '{http://www.loc.gov/premis/v3}rightsGranted')
        if rightsGranted:
            rightsStatement.set_rightsGranted(rightsGranted)

        linkingObjectIdentifier = self._pn(self.buildLinkingObjectIdentifier, node, '{http://www.loc.gov/premis/v3}linkingObjectIdentifier')
        if linkingObjectIdentifier:
            rightsStatement.set_linkingObjectIdentifier(linkingObjectIdentifier)

        linkingAgentIdentifier = self._pn(self.buildLinkingAgentIdentifier, node, '{http://www.loc.gov/premis/v3}linkingAgentIdentifier')
        if linkingAgentIdentifier:
            rightsStatement.set_linkingAgentIdentifier(linkingAgentIdentifier)

        return rightsStatement

    def buildRightsStatementIdentifier(self, node):
        rightsStatementIdentifierType = self._find(node, '{http://www.loc.gov/premis/v3}rightsStatementIdentifierType', req=True)
        rightsStatementIdentifierValue = self._find(node, '{http://www.loc.gov/premis/v3}rightsStatementIdentifierValue', req=True)

        rightsStatementIdentifier = RightsStatementIdentifier(rightsStatementIdentifierType, rightsStatementIdentifierValue)

        return rightsStatementIdentifier

    def buildCopyrightInformation(self, node):
        copyrightStatus = self._find(node, '{http://www.loc.gov/premis/v3}copyrightStatus', req=True)
        copyrightJurisdiction = self._find(node, '{http://www.loc.gov/premis/v3}copyrightJurisdiction', req=True)

        copyrightInformation = CopyrightInformation(copyrightStatus, copyrightJurisdiction)

        copyrightStatusDeterminationDate = self._find(node, '{http://www.loc.gov/premis/v3}copyrightStatusDeterminationDate')
        if copyrightStatusDeterminationDate:
            copyrightInformation.set_copyrightStatusDeterminationDate(copyrightStatusDeterminationDate)

        copyrightNote = self._find_all(node, '{http://www.loc.gov/premis/v3}copyrightNote')
        if copyrightNote:
            copyrightInformation.set_copyrightNote(copyrightNote)

        copyrightDocumentationIdentifier = self._pn(self.buildCopyrightDocumentationIdentifier, node, '{http://www.loc.gov/premis/v3}copyrightDocumentationIdentifier')
        if copyrightDocumentationIdentifier:
            copyrightInformation.set_copyrightDocumentationIdentifier(copyrightDocumentationIdentifier)

        copyrightApplicableDatesNode = self._find_node(node, '{http://www.loc.gov/premis/v3}copyrightApplicableDates')
        if copyrightApplicableDatesNode:
            copyrightApplicableDates = self.buildCopyrightApplicableDates(copyrightApplicableDatesNode)
            copyrightInformation.set_copyrightApplicableDates(copyrightApplicableDates)

        return copyrightInformation

    def buildLicenseInformation(self, node):
        licenseInformation = LicenseInformation()

        licenseDocumentationIdentifier = self._pn(self.buildLicenseDocumentationIdentifier, node, '{http://www.loc.gov/premis/v3}licenseDocumentationIdentifier')
        if licenseDocumentationIdentifier:
            licenseInformation.set_licenseDocumentationIdentifier(licenseDocumentationIdentifier)

        licenseTerms = self._find(node, '{http://www.loc.gov/premis/v3}licenseTerms')
        if licenseTerms:
            licenseInformation.set_licenseTerms(licenseTerms)

        licenseNote = self._find_all(node, '{http://www.loc.gov/premis/v3}licenseNote')
        if licenseNote:
            licenseInformation.set_licenseNote(licenseNote)

        licenseApplicableDatesNode = self._find_node(node, '{http://www.loc.gov/premis/v3}licenseApplicableDates')
        if licenseApplicableDatesNode:
            licenseApplicableDates = self.buildLicenseApplicableDates(licenseApplicableDatesNode)
            licenseInformation.set_licenseApplicableDates(licenseApplicableDates)

        return licenseInformation

    def buildStatuteInformation(self, node):
        statuteJurisdiction = self._find(node, '{http://www.loc.gov/premis/v3}statuteJurisdiction', req=True)
        statuteCitation = self._find(node, '{http://www.loc.gov/premis/v3}statuteCitation', req=True)

        statuteInformation = StatuteInformation(statuteJurisdiction, statuteCitation)

        statuteInformationDeterminationDate = self._find(node, '{http://www.loc.gov/premis/v3}statuteInformationDeterminationDate')
        if statuteInformationDeterminationDate:
            statuteInformation.set_statuteInformationDeterminationDate(statuteInformationDeterminationDate)

        statuteNote = self._find_all(node, '{http://www.loc.gov/premis/v3}statuteNote')
        if statuteNote:
            statuteInformation.set_statuteNote(statuteNote)

        statuteDocumentationIdentifier = self._pn(self.buildStatuteDocumentationIdentifier, node, '{http://www.loc.gov/premis/v3}statuteDocumentationIdentifier')
        if statuteDocumentationIdentifier:
            statuteInformation.set_statuteDocumentationIdentifier(statuteDocumentationIdentifier)

        statuteApplicableDatesNode = self._find_node(node, '{http://www.loc.gov/premis/v3}statuteApplicableDates')
        if statuteApplicableDatesNode:
            statuteApplicableDates = self.buildStatuteApplicableDates(statuteApplicableDatesNode)
            statuteInformation.set_statuteApplicableDates(statuteApplicableDates)

        return statuteInformation

    def buildOtherRightsInformation(self, node):
        otherRightsBasis = self._find(node, '{http://www.loc.gov/premis/v3}otherRightsBasis', req=True)

        otherRightsInformation = OtherRightsInformation(otherRightsBasis)

        otherRightsDocumentationIdentifier = self._pn(self.buildOtherRightsDocumentationIdentifier, node, '{http://www.loc.gov/premis/v3}otherRightsDocumentationIdentifier')
        if otherRightsDocumentationIdentifier:
            otherRightsInformation.set_otherRightsDocumentationIdentifier(otherRightsDocumentationIdentifier)

        otherRightsApplicableDatesNode = self._find_node(node, '{http://www.loc.gov/premis/v3}otherRightsApplicableDates')
        if otherRightsApplicableDatesNode:
            otherRightsApplicableDates = self.buildOtherRightsApplicableDates(otherRightsApplicableDatesNode)
            otherRightsInformation.set_otherRightsApplicableDates(otherRightsApplicableDates)

        otherRightsNote = self._find_all(node, '{http://www.loc.gov/premis/v3}otherRightsNote')
        if otherRightsNote:
            otherRightsInformation.set_otherRightsNote(otherRightsNote)

        return otherRightsInformation

    def buildRightsGranted(self, node):
        act = self._find(node, '{http://www.loc.gov/premis/v3}act', req=True)

        rightsGranted = RightsGranted(act)

        restriction = self._find_all(node, '{http://www.loc.gov/premis/v3}restriction')
        if restriction:
            rightsGranted.set_restriction(restriction)

        termOfGrantNode = self._find_node(node, '{http://www.loc.gov/premis/v3}termOfGrant')
        if termOfGrantNode:
            termOfGrant = self.buildTermOfGrant(termOfGrantNode)
            rightsGranted.set_termOfGrant(termOfGrant)

        termOfRestrictionNode = self._find_node(node, '{http://www.loc.gov/premis/v3}termOfRestriction')
        if termOfRestrictionNode:
            termOfRestriction = self.buildTermOfRestriction(termOfRestrictionNode)
            rightsGranted.set_termOfRestriction(termOfRestriction)

        rightsGrantedNote = self._find_all(node, '{http://www.loc.gov/premis/v3}rightsGrantedNote')
        if rightsGrantedNote:
            rightsGranted.set_rightsGrantedNote(rightsGrantedNote)

        return rightsGranted

    def buildCopyrightDocumentationIdentifier(self, node):
        copyrightDocumentationIdentifierType = self._find(node, '{http://www.loc.gov/premis/v3}copyrightDocumentationIdentifierType', req=True)
        copyrightDocumentationIdentifierValue = self._find(node, '{http://www.loc.gov/premis/v3}copyrightDocumentationIdentifierValue', req=True)

        copyrightDocumentationIdentifier = CopyrightDocumentationIdentifier(copyrightDocumentationIdentifierType, copyrightDocumentationIdentifierValue)

        copyrightDocumentationRole = self._find(node, '{http://www.loc.gov/premis/v3}copyrightDocumentationRole')
        if copyrightDocumentationRole:
            copyrightDocumentationIdentifier.set_copyrightDocumentationRole(copyrightDocumentationRole)

        return copyrightDocumentationIdentifier

    def buildCopyrightApplicableDates(self, node):
        copyrightApplicableDates = CopyrightApplicableDates()

        startDate = self._find(node, '{http://www.loc.gov/premis/v3}startDate')
        if startDate:
            copyrightApplicableDates.set_startDate(startDate)

        endDate = self._find(node, '{http://www.loc.gov/premis/v3}endDate')
        if endDate:
            copyrightApplicableDates.set_endDate(endDate)

        return copyrightApplicableDates

    def buildLicenseDocumentationIdentifier(self, node):
        licenseDocumentationIdentifierType = self._find(node, '{http://www.loc.gov/premis/v3}licenseDocumentationIdentifierType', req=True)
        licenseDocumentationIdentifierValue = self._find(node, '{http://www.loc.gov/premis/v3}licenseDocumentationIdentifierValue', req=True)

        licenseDocumentationIdentifier = LicenseDocumentationIdentifier(licenseDocumentationIdentifierType, licenseDocumentationIdentifierValue)

        licenseDocumentationRole = self._find(node, '{http://www.loc.gov/premis/v3}licenseDocumentationRole')
        if licenseDocumentationRole:
            licenseDocumentationIdentifier.set_licenseDocumentationRole(licenseDocumentationRole)

        return licenseDocumentationIdentifier

    def buildLicenseApplicableDates(self, node):
        licenseApplicableDates = LicenseApplicableDates()

        startDate = self._find(node, '{http://www.loc.gov/premis/v3}startDate')
        if startDate:
            licenseApplicableDates.set_startDate(startDate)

        endDate = self._find(node, '{http://www.loc.gov/premis/v3}endDate')
        if endDate:
            licenseApplicableDates.set_endDate(endDate)

        return licenseApplicableDates

    def buildStatuteDocumentationIdentifier(self, node):
        statuteDocumentationIdentifierType = self._find(node, '{http://www.loc.gov/premis/v3}statuteDocumentationIdentifierType', req=True)
        statuteDocumentationIdentifierValue = self._find(node, '{http://www.loc.gov/premis/v3}statuteDocumentationIdentifierValue', req=True)

        statuteDocumentationIdentifier = StatuteDocumentationIdentifier(statuteDocumentationIdentifierType, statuteDocumentationIdentifierValue)

        statuteDocumentationRole = self._find(node, '{http://www.loc.gov/premis/v3}statuteDocumentationRole')
        if statuteDocumentationRole:
            statuteDocumentationIdentifier.set_statuteDocumentationRole(statuteDocumentationRole)

        return statuteDocumentationIdentifier

    def buildStatuteApplicableDates(self, node):
        statuteApplicableDates = StatuteApplicableDates()

        startDate = self._find(node, '{http://www.loc.gov/premis/v3}startDate')
        if startDate:
            statuteApplicableDates.set_startDate(startDate)

        endDate = self._find(node, '{http://www.loc.gov/premis/v3}endDate')
        if endDate:
            statuteApplicableDates.set_endDate(endDate)

        return statuteApplicableDates

    def buildOtherRightsDocumentationIdentifier(self, node):
        otherRightsDocumentationIdentifierType = self._find(node, '{http://www.loc.gov/premis/v3}otherRightsDocumentationIdentifierType', req=True)
        otherRightsDocumentationIdentifierValue = self._find(node, '{http://www.loc.gov/premis/v3}otherRightsDocumentationIdentifierValue', req=True)

        otherRightsDocumentationIdentifier = OtherRightsDocumentationIdentifier(otherRightsDocumentationIdentifierType, otherRightsDocumentationIdentifierValue)

        otherRightsDocumentationRole = self._find(node, '{http://www.loc.gov/premis/v3}otherRightsDocumentationRole')
        if otherRightsDocumentationRole:
            otherRightsDocumentationIdentifier.set_otherRightsDocumentationRole(otherRightsDocumentationRole)

        return otherRightsDocumentationIdentifier

    def buildOtherRightsApplicableDates(self, node):
        otherRightsApplicableDates = OtherRightsApplicableDates()

        startDate = self._find(node, '{http://www.loc.gov/premis/v3}startDate')
        if startDate:
            otherRightsApplicableDates.set_startDate(startDate)

        endDate = self._find(node, '{http://www.loc.gov/premis/v3}endDate')
        if endDate:
            otherRightsApplicableDates.set_endDate(endDate)

        return otherRightsApplicableDates

    def buildTermOfGrant(self, node):
        startDate = self._find(node, '{http://www.loc.gov/premis/v3}startDate')

        termOfGrant = TermOfGrant(startDate)

        endDate = self._find(node, '{http://www.loc.gov/premis/v3}endDate')
        if endDate:
            termOfGrant.set_endDate(endDate)

        return termOfGrant

    def buildTermOfRestriction(self, node):
        startDate = self._find(node, '{http://www.loc.gov/premis/v3}startDate')

        termOfRestriction = TermOfRestriction(startDate)

        endDate = self._find(node, '{http://www.loc.gov/premis/v3}endDate')
        if endDate:
            termOfRestriction.set_endDate(endDate)

        return termOfRestriction


class JSONNodeFactory(object):
    def __init__(self, j):
        self.j = j

    def find_objects(self):
        r = []
        for x in self.j['object']:
            r.append(self.buildObject(x))
        return r

    def find_events(self):
        r = []
        for x in self.j['event']:
            r.append(self.buildEvent(x))
        return r

    def find_rights(self):
        r = []
        for x in self.j['rights']:
            r.append(self.buildRights(x))
        return r

    def find_agents(self):
        r = []
        for x in self.j['agent']:
            r.append(self.buildAgent(x))
        return r

    def buildCreatingApplicationExtension(self, d):
        return CreatingApplicationExtension()

    def buildObjectCharacteristicsExtension(self, d):
        return ObjectCharacteristicsExtension()

    def buildSignificantPropertiesExtension(self, d):
        return SignificantPropertiesExtension()

    def buildKeyInformation(self, d):
        return KeyInformation()

    def buildSignatureInformationExtension(self, d):
        return SignatureInformationExtension()

    def buildEventDetailExtension(self, d):
        return EventDetailExtension()

    def buildEventOutcomeDetailExtension(self, d):
        return EventOutcomeDetailExtension()

    def buildObject(self, d):
        objectIdentifier = [self.buildObjectIdentifier(x) for x in d['objectIdentifier']]
        objectCategory = d['objectCategory']
        objectCharacteristics = [self.buildObjectCharacteristics(x) for x in d['objectCharacteristics']]

        obj = Object(objectIdentifier, objectCategory, objectCharacteristics)

        if d.get('preservationLevel'):
            for x in d['preservationLevel']:
                obj.add_preservationLevel(self.buildPreservationLevel(x))

        if d.get('significantProperties'):
            for x in d['significantProperties']:
                obj.add_significantProperties(self.buildSignificantProperties(x))

        if d.get('originalName'):
            obj.set_originalName(d['originalName'])

        if d.get('storage'):
            for x in d['storage']:
                obj.add_storage(self.buildStorage(x))

        if d.get('signatureInformation'):
            for x in d['signatureInformation']:
                obj.add_signatureInformation(self.buildSignatureInformation(x))

        if d.get('environmentFunction'):
            for x in d['environmentFunction']:
                obj.add_environmentFunction(self.buildEnvironmentFunction(x))

        if d.get('environmentDesignation'):
            for x in d['environmentDesignation']:
                obj.add_environmentDesignation(self.buildEnvironmentDesignation(x))

        if d.get('environmentRegistry'):
            for x in d['environmentRegistry']:
                obj.add_environmentRegistry(self.buildEnvironmentRegistry(x))

        if d.get('environmentExtension'):
            obj.set_environmentExtension(self.buildEnvironmentExtension(x))

        if d.get('relationship'):
            for x in d['relationship']:
                obj.add_relationship(self.buildRelationship(x))

        if d.get('linkingEventIdentifier'):
            for x in d['linkingEventIdentifier']:
                obj.add_linkingEventIdentifier(self.buildLinkingEventIdentifier(x))

        if d.get('linkingRightsStatementIdentifier'):
            for x in d['linkingRightsStatementIdentifier']:
                obj.add_linkingRightsStatementIdentifier(self.buildLinkingRightsStatementIdentifier(x))

        return obj

    def buildObjectIdentifier(self, d):
        objectIdentifierType = d['objectIdentifierType']
        objectIdentifierValue = d['objectIdentifierValue']
        return ObjectIdentifier(objectIdentifierType, objectIdentifierValue)

    def buildPreservationLevel(self, d):
        preservationLevelValue = d['preservationLevelValue']
        preservationLevel = PreservationLevel(preservationLevelValue)

        if d.get('preservationLevelType'):
            preservationLevel.set_preservationLevelType(d['preservationLevelType'])

        if d.get('preservationLevelRole'):
            preservationLevel.set_preservationLevelRole(d['preservationLevelRole'])

        if d.get('preservationLevelRationale'):
            for x in d['preservationLevelRationale']:
                preservationLevel.add_preservationLevelRationale(x)

        if d.get('preservationLevelDateAssigned'):
            preservationLevel.set_preservationLevelDateAssigned(d['preservationLevelDateAssigned'])

        return preservationLevel

    def buildSignificantProperties(self, d):
        significantPropertiesValue = None
        if d.get('significantPropertiesValue'):
            significantPropertiesValue = d['significantPropertiesValue']

        significantPropertiesExtension = None
        if d.get('significantPropertiesExtension'):
            significantPropertiesExtension = self.buildSignificantPropertiesExtension(d['significantPropertiesExtension'])

        significantProperties = SignificantProperties(significantPropertiesValue, significantPropertiesExtension)

        if d.get('significantPropertiesType'):
            significantProperties.set_significantPropertiesType(d['significantPropertiesType'])

        return significantProperties

    def buildObjectCharacteristics(self, d):
        format = [self.buildFormat(x) for x in d['format']]

        objectCharacteristics = ObjectCharacteristics(format)

        if d.get('compositionLevel'):
            objectCharacteristics.set_compositionLevel(d['compositionLevel'])

        if d.get('fixity'):
            for x in d['fixity']:
                objectCharacteristics.add_fixity(self.buildFixity(x))

        if d.get('size'):
            objectCharacteristics.set_size(d['size'])

        if d.get('format'):
            for x in d['format']:
                objectCharacteristics.add_format(self.buildFormat(x))

        if d.get('creatingApplication'):
            for x in d['creatingApplication']:
                objectCharacteristics.add_creatingApplication(self.buildCreatingApplication(x))

        if d.get('inhibitors'):
            for x in d['inhibitors']:
                objectCharacteristics.add_inhibitors(self.buildInhibitors(x))

        if d.get('objectCharacteristicsExtension'):
            objectCharacteristics.set_objectCharacteristicsExtension(
                self.buildObjectCharacteristicsExtension(d['objectCharacteristicsExtension'])
            )

        return objectCharacteristics

    def buildFixity(self, d):
        messageDigestAlgorithm = d['messageDigestAlgorithm']
        messageDigest = d['messageDigest']

        fixity = Fixity(messageDigestAlgorithm, messageDigest)

        if d.get('messageDigestOriginator'):
            fixity.set_messageDigestOriginator(d.get('messageDigestOriginator'))

        return fixity

    def buildFormat(self, d):
        formatDesignation = None
        if d.get('formatDesignation'):
            formatDesignation = self.buildFormatDesignation(d['formatDesignation'])

        formatRegistry = None
        if d.get('formatRegistry'):
            formatRegistry = self.buildFormatRegistry(d['formatRegistry'])

        format = Format(formatDesignation, formatRegistry)

        if d.get('formatNote'):
            for x in d['formatNote']:
                format.add_formatNote(x)

        return format

    def buildFormatDesignation(self, d):
        formatName = d['formatName']

        formatDesignation = FormatDesignation(formatName)

        if d.get('formatVersion'):
            formatDesignation.set_formatVersion(d['formatVersion'])

        return formatDesignation

    def buildFormatRegistry(self, d):
        formatRegistryName = d['formatRegistryName']
        formatRegistryKey = d['formatRegistryKey']

        formatRegistry = FormatRegistry(formatRegistryName, formatRegistryKey)

        if d.get('formatRegistryRole'):
            formatRegistry.set_formatRegistryRole(d['formatRegistryRole'])

        return formatRegistry

    def buildCreatingApplication(self, d):
        creatingApplication = CreatingApplication()

        if d.get('creatingApplicationName'):
            creatingApplication.set_creatingApplicationName(d['creatingApplicationName'])

        if d.get('creatingApplicationVersion'):
            creatingApplication.set_creatingApplicationVersion(d['creatingApplicationVersion'])

        if d.get('dateCreatedByApplication'):
            creatingApplication.set_dateCreatedByApplication(d['dateCreatedByApplication'])

        if d.get('creatingApplicationExtension'):
            creatingApplication.set_creatingApplicationExtension(
                self.buildCreatingApplicationExtension(d['creatingApplicationExtension'])
            )

        return creatingApplication

    def buildInhibitors(self, d):
        inhibitorType = d['inhibitorType']
        inhibitors = Inhibitors(inhibitorType)

        if d.get('inhibitorTarget'):
            for x in d['inhibitorTarget']:
                inhibitors.add_inhibitorTarget(x)

        if d.get('inhibitorKey'):
            inhibitors.set_inhibitorKey(d['inhibitorKey'])

        return inhibitors

    def buildStorage(self, d):
        storage = Storage()

        if d.get('contentLocation'):
            storage.set_contentLocation(self.buildContentLocation(d['contentLocation']))

        if d.get('storageMedium'):
            storage.set_storageMedium(d['storageMedium'])

        return storage

    def buildContentLocation(self, d):
        contentLocationType = d['contentLocationType']
        contentLocationValue = d['contentLocationValue']

        return ContentLocation(contentLocationType, contentLocationValue)

    def buildSignatureInformation(self, d):
        signatureInformation = SignatureInformation()
        if d.get('signature'):
            for x in d['signature']:
                signatureInformation.add_signature(self.buildSignature(x))

        if d.get('signatureInformationExtension'):
            signatureInformation.set_signatureInformationExtension(
                self.buildSignatureInformationExtension(d['signatureInformationExtension'])
            )

        return signatureInformation

    def buildSignature(self, d):
        signatureEncoding = d['signatureEncoding']
        signatureMethod = d['signatureMethod']
        signatureValue = d['signatureValue']
        signatureValidationRules = d['signatureValidationRules']

        signature = Signature(signatureEncoding, signatureMethod, signatureValue, signatureValidationRules)

        if d.get('signer'):
            signature.set_signer(d['signer'])

        if d.get('signatureProperties'):
            for x in d['signatureProperties']:
                signature.add_signatureProperties(x)

        if d.get('keyInformation'):
            signature.set_keyInformation(
                self.buildKeyInformation(d['keyInformation'])
            )

        return signature

    def buildEnvironmentFunction(self, d):
        environmentFunctionType = d['environmentFunctionType']
        environmentFunctionLevel = d['environmentFunctionLevel']

        return EnvironmentFunction(environmentFunctionType, environmentFunctionLevel)

    def buildEnvironmentDesignation(self, d):
        environmentName = d['environmentName']

        environmentDesignation = EnvironmentDesignation(environmentName)

        if d.get('environmentVersion'):
            environmentDesignation.set_environmentVersion(d['environmentVersion'])

        if d.get('environmentOrigin'):
            environmentDesignation.set_environmentOrigin(d['environmentOrigin'])

        if d.get('environmentDesignationNote'):
            for x in d['environmentDesignationNote']:
                environmentDesignation.add_environmentDesignationNote(x)

        if d.get('environmentDesignationExtension'):
            environmentDesignation.set_environmentDesignationExtension(d['environmentDesignationExtension'])

        return environmentDesignation

    def buildEnvironmentRegistry(self, d):
        environmentRegistryName = d['environmentRegistryName']
        environmentRegistryKey = d['environmentRegistryKey']

        environmentRegistry = EnvironmentRegistry(environmentRegistryName, environmentRegistryKey)

        if d.get('environmentRegistryRole'):
            environmentRegistry.set_environmentRegistryRole(d['environmentRegistryRole'])

        return environmentRegistry

    def buildRelationship(self, d):
        relationshipType = d['relationshipType']
        relationshipSubType = d['relationshipSubType']
        relatedObjectIdentifier = [self.buildRelatedObjectIdentifier(x) for x in d['relatedObjectIdentifier']]

        relationship = Relationship(relationshipType, relationshipSubType, relatedObjectIdentifier)

        if d.get('relatedEventIdentifier'):
            for x in d['relatedEventIdentifier']:
                relationship.add_relatedEventIdentifier(self.buildRelatedEventIdentifier(x))

        if d.get('relatedEnvironmentPurpose'):
            for x in d['relatedEnvironmentPurpose']:
                relationship.add_relatedEnvironmentPurpose(x)

        if d.get('relatedEnvironmentCharacteristic'):
            relationship.set_relatedEnvironmentCharacteristic(d['relatedEnvironmentCharacteristic'])

        return relationship

    def buildRelatedObjectIdentifier(self, d):
        relatedObjectIdentifierType = d['relatedObjectIdentifierType']
        relatedObjectIdentifierValue = d['relatedObjectIdentifierValue']

        relatedObjectIdentifier = RelatedObjectIdentifier(relatedObjectIdentifierType, relatedObjectIdentifierValue)

        if d.get('relatedObjectSequence'):
            relatedObjectIdentifier.set_relatedObjectSequence(d['relatedObjectSequence'])

        return relatedObjectIdentifier

    def buildRelatedEventIdentifier(self, d):
        relatedEventIdentifierType = d['relatedEventIdentifierType']
        relatedEventIdentifierValue = d['relatedEventIdentifierValue']

        relatedEventIdentifier = RelatedEventIdentifier(relatedEventIdentifierType, relatedEventIdentifierValue)

        if d.get('relatedEventSequence'):
            relatedEventIdentifier.set_relatedEventSequence(d['relatedEventSequence'])

        return relatedEventIdentifier

    def buildLinkingEventIdentifier(self, d):
        linkingEventIdentifierType = d['linkingEventIdentifierType']
        linkingEventIdentifierValue = d['linkingEventIdentifierValue']

        return LinkingEventIdentifier(linkingEventIdentifierType, linkingEventIdentifierValue)

    def buildLinkingRightsStatementIdentifier(self, d):
        linkingRightsStatementIdentifierType = d['linkingRightsStatementIdentifierType']
        linkingRightsStatementIdentifierValue = d['linkingRightsStatementIdentifierValue']

        return LinkingRightsStatementIdentifier(linkingRightsStatementIdentifierType, linkingRightsStatementIdentifierValue)

    def buildEvent(self, d):
        eventIdentifier = self.buildEventIdentifier(d['eventIdentifier'])
        eventType = d['eventType']
        eventDateTime = d['eventDateTime']

        event = Event(eventIdentifier, eventType, eventDateTime)

        if d.get('eventDetailInformation'):
            for x in d['eventDetailInformation']:
                event.add_eventDetailInformation(self.buildEventDetailInformation(x))

        if d.get('eventOutcomeInformation'):
            for x in d['eventOutcomeInformation']:
                event.add_eventOutcomeInformation(self.buildEventOutcomeInformation(x))

        if d.get('linkingAgentIdentifier'):
            for x in d['linkingAgentIdentifier']:
                event.add_linkingAgentIdentifier(self.buildLinkingAgentIdentifier(x))

        if d.get('linkingObjectIdentifier'):
            for x in d['linkingObjectIdentifier']:
                event.add_linkingObjectIdentifier(self.buildLinkingObjectIdentifier(x))

        return event

    def buildEventIdentifier(self, d):
        eventIdentifierType = d['eventIdentifierType']
        eventIdentifierValue = d['eventIdentifierValue']
        return EventIdentifier(eventIdentifierType, eventIdentifierValue)

    def buildEventDetailInformation(self, d):
        eventDetail = None
        if d.get('eventDetail'):
            eventDetail = d['eventDetail']

        eventDetailExtension = None
        if d.get('eventDetailExtension'):
            eventDetailExtension = self.buildEventDetailExtension(d['eventDetailExtension'])

        return EventDetailInformation(eventDetail, eventDetailExtension)


    def buildEventOutcomeInformation(self, d):

        eventOutcome = None
        if d.get('eventOutcome'):
            eventOutcome = d['eventOutcome']

        eventOutcomeDetail = None
        if d.get('eventOutcomeDetail'):
            eventOutcomeDetail = [self.buildEventOutcomeDetail(x) for x in d['eventOutcomeDetail']]

        return EventOutcomeInformation(eventOutcome, eventOutcomeDetail)

    def buildEventOutcomeDetail(self, d):
        eventOutcomeDetailNote = None
        if d.get('eventOutcomeDetailNote'):
            eventOutcomeDetailNote = d['eventOutcomeDetailNote']

        eventOutcomeDetailExtension = None
        if d.get('eventOutcomeDetailExtension'):
                eventOutcomeDetailExtension = self.buildEventOutcomeDetailExtension(d['eventOutcomeDetailExtension'])

        return EventOutcomeDetail(eventOutcomeDetailNote, eventOutcomeDetailExtension)

    def buildLinkingAgentIdentifier(self, d):
        linkingAgentIdentifierType = d['linkingAgentIdentifierType']
        linkingAgentIdentifierValue = d['linkingAgentIdentifierValue']

        linkingAgentIdentifier = LinkingAgentIdentifier(linkingAgentIdentifierType, linkingAgentIdentifierValue)

        if d.get('linkingAgentRole'):
            for x in d['linkingAgentRole']:
                linkingAgentIdentifier.add_linkingAgentRole(x)

        return linkingAgentIdentifier

    def buildLinkingObjectIdentifier(self, d):
        linkingObjectIdentifierType = d['linkingObjectIdentifierType']
        linkingObjectIdentifierValue = d['linkingObjectIdentifierValue']

        linkingObjectIdentifier = LinkingObjectIdentifier(linkingObjectIdentifierType, linkingObjectIdentifierValue)

        if d.get('linkingObjectRole'):
            for x in d['linkingObjectRole']:
                linkingObjectIdentifier.add_linkingObjectRole(x)

        return linkingObjectIdentifier






class LinkingXIdentifierFactory(metaclass=ABCMeta):

    _input_node = None
    _output_node_type = None

    @abstractmethod
    def __init__(self, input_node):
        self.set_input_node(input_node)


    @abstractmethod
    def get_input_identifier_type(self):
        raise NotImplementedError(
            "The ABC doesn't provide any functionality for this method."
        )

    @abstractmethod
    def get_input_identifier_value(self):
        raise NotImplementedError(
            "The ABC doesn't provide any functionality for this method."
        )

    @abstractmethod
    def set_output_node_role(self, node, role):
        raise NotImplementedError(
            "The ABC doesn't provide any functionality for this method."
        )

    def get_output_node_type(self):
        x = self._output_node_type
        if x is None:
            raise NotImplementedError(
                "You need to call set_output_node_type in your init."
            )
        return x

    def get_input_node(self):
        return self._input_node

    def set_input_node(self, x):
        self._input_node = x

    def set_output_node_type(self, x):
        self._output_node_type = x

    def produce_linking_node(self, role=None):
        linkingXIdentifierType = self.get_input_identifier_type()
        linkingXIdentifierValue = self.get_input_identifier_value()
        linking_node = self.get_output_node_type()(
            linkingXIdentifierType,
            linkingXIdentifierValue
        )
        if role is not None:
            self.set_output_node_role(linking_node, role)
        return linking_node

    input_node = property(get_input_node, set_input_node)
    output_node_type = property(get_output_node_type, set_output_node_type)


class LinkingObjectIdentifierFactory(LinkingXIdentifierFactory):
    def __init__(self, input_node):
        super().__init__(input_node)
        self.set_output_node_type(LinkingObjectIdentifier)

    def set_input_node(self, x):
        if not isinstance(x, Object):
            raise ValueError(
                "{} is not an Object.".format(str(type(x)))
            )
        super().set_input_node(x)

    def get_input_identifier_type(self):
        return self.get_input_node().get_objectIdentifier(0).get_objectIdentifierType()

    def get_input_identifier_value(self):
        return self.get_input_node().get_objectIdentifier(0).get_objectIdentifierValue()

    def set_output_node_role(self, node, role):
        node.set_linkingObjectRole(role)


class LinkingAgentIdentifierFactory(LinkingXIdentifierFactory):
    def __init__(self, input_node):
        super().__init__(input_node)
        self.set_output_node_type(LinkingAgentIdentifier)

    def set_input_node(self, x):
        if not isinstance(x, Agent):
            raise ValueError(
                "{} is not an Agent.".format(str(type(x)))
            )
        super().set_input_node(x)

    def get_input_identifier_type(self):
        return self.get_input_node().get_agentIdentifier(0).get_agentIdentifierType()

    def get_input_identifier_value(self):
        return self.get_input_node().get_agentIdentifier(0).get_agentIdentifierValue()

    def set_output_node_role(self, node, role):
        node.set_linkingAgentRole(role)


class LinkingEventIdentifierFactory(LinkingXIdentifierFactory):
    def __init__(self, input_node):
        super().__init__(input_node)
        self.set_output_node_type(LinkingEventIdentifier)

    def set_input_node(self, x):
        if not isinstance(x, Event):
            raise ValueError(
                "{} is not an Event.".format(str(type(x)))
            )
        super().set_input_node(x)

    def get_input_identifier_type(self):
        return self.get_input_node().get_eventIdentifier().get_eventIdentifierType()

    def get_input_identifier_value(self):
        return self.get_input_node().get_eventIdentifier().get_eventIdentifierValue()

    def set_output_node_role(self, node, role):
        node.set_linkingEventRole(role)


class LinkingRightsStatementIdentifierFactory(LinkingXIdentifierFactory):
    # This one ends up being a little funky, requiring you pass it a
    # rightsStatement instead of just a rights entity.
    # I complained about incongruities like this on the PREMIS Implementors
    # Group mailing list - I guess we'll see if anything comes of it.
    def __init__(self, input_node):
        super().__init__(input_node)
        self.set_output_node_type(LinkingRightsStatementIdentifier)

    def set_input_node(self, x):
        if not isinstance(x, RightsStatement):
            raise ValueError(
                "{} is not a RightsStatement.".format(str(type(x)))
            )
        super().set_input_node(x)

    def get_input_identifier_type(self):
        return self.get_input_node().get_rightsStatementIdentifier().get_rightsStatementIdentifierType()

    def get_input_identifier_value(self):
        return self.get_input_node().get_rightsStatementIdentifier().get_rightsStatementIdentifierValue()

    def set_output_node_role(self, node, role):
        raise NotImplementedError(
            "You can not set a role for a LinkingRightsStatement"
        )
        # Because PREMIS says so!


class LinkingEnvironmentIdentifierFactory(LinkingXIdentifierFactory):
    def __init__(self, input_node):
        super().__init__(input_node)
        self.set_output_node_type(LinkingEnvironmentIdentifier)

    def set_input_node(self, x):
        if not isinstance(x, Object):
            raise ValueError(
                "{} is not an Object.".format(str(type(x)))
            )
        super().set_input_node(x)

    def get_input_identifier_type(self):
        return self.get_input_node().get_objectIdentifier(0).get_objectIdentifierType()

    def get_input_identifier_value(self):
        return self.get_input_node().get_objectIdentifier(0).get_objectIdentifierValue()

    def set_output_node_role(self, node, role):
        node.set_linkingEnvironmentRole(role)
