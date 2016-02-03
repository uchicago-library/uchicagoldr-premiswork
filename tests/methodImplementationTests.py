import unittest

from pypremis.premisrecord import *


class TestObjectMethods(unittest.TestCase):
    def testObject(self):
        a = PremisObject()

        a.set_objectIdentifier(1)
        a.get_objectIdentifier()
        a.add_objectIdentifier(1)

        a.set_objectCategory(1)
        a.get_objectCategory()

        a.set_preservationLevel(1)
        a.get_preservationLevel()
        a.add_preservationLevel(1)

        a.set_significantProperties(1)
        a.get_significantProperties()
        a.add_significantProperties(1)

        a.set_objectCharacteristics(1)
        a.get_objectCharacteristics()
        a.add_objectCharacteristics(1)

        a.set_originalName(1)
        a.get_originalName()

        a.set_storage(1)
        a.get_storage()
        a.add_storage(1)

        a.set_signatureInformation(1)
        a.get_signatureInformation()
        a.add_signatureInformation(1)

        a.set_environmentFunction(1)
        a.get_environmentFunction()
        a.add_environmentFunction(1)

        a.set_environmentDesignation(1)
        a.get_environmentDesignation()
        a.add_environmentDesignation(1)

        a.set_environmentRegistry(1)
        a.get_environmentRegistry()
        a.add_environmentRegistry(1)

        a.set_environmentExtension(1)
        a.get_environmentExtension()
        a.add_environmentExtension(1)

        a.set_relationship(1)
        a.get_relationship()
        a.add_relationship(1)

        a.set_linkingEventIdentifier(1)
        a.get_linkingEventIdentifier()
        a.add_linkingEventIdentifier(1)

        a.set_linkingRightsStatementIdentifier(1)
        a.get_linkingRightsStatementIdentifier()
        a.add_linkingRightsStatementIdentifier(1)

    def testObjectIdentifier(self):
        a = ObjectIdentifier()

        a.set_objectIdentifierType(1)
        a.get_objectIdentifierType()

        a.set_objectIdentifierValue(1)
        a.get_objectIdentifierValue()

    def testPreservationLevel(self):
        a = PreservationLevel()

        a.set_preservationLevelType(1)
        a.get_preservationLevelType()

        a.set_preservationLevelValue(1)
        a.get_preservationLevelValue()

        a.set_preservationLevelRole(1)
        a.get_preservationLevelRole()

        a.set_preservationLevelRationale(1)
        a.get_preservationLevelRationale()
        a.add_preservationLevelRationale(1)

        a.set_preservationLevelDateAssigned(1)
        a.get_preservationLevelDateAssigned()

    def testSignificantProperties(self):
        a = SignificantProperties()

        a.set_significantPropertiesType(1)
        a.get_significantPropertiesType()

        a.set_significantPropertiesValue(1)
        a.get_significantPropertiesValue()

        a.set_significantPropertiesExtension(1)
        a.get_significantPropertiesExtension()
        a.add_significantPropertiesExtension(1)

    def testObjectCharacteristics(self):
        a = ObjectCharacteristics()

        a.set_compositionLevel(1)
        a.get_compositionLevel()

        a.set_fixity(1)
        a.get_fixity()
        a.add_fixity(1)

        a.set_size(1)
        a.get_size()

        a.set_format(1)
        a.get_format()
        a.add_format(1)

        a.set_creatingApplication(1)
        a.get_creatingApplication()
        a.add_creatingApplication(1)

        a.set_inhibitors(1)
        a.get_inhibitors()
        a.add_inhibitors(1)

        a.set_objectCharacteristicsExtension(1)
        a.get_objectCharacteristicsExtension()
        a.add_objectCharacteristicsExtension(1)


    def testStorage(self):
        a = Storage()

        a.set_contentLocation(1)
        a.get_contentLocation()

        a.set_storageMedium(1)
        a.get_storageMedium()

    def testContentLocation(self):
        a = ContentLocation()

        a.set_contentLocationType(1)
        a.get_contentLocationType

        a.set_contentLocationValue(1)
        a.get_contentLocationValue()

    def testSignatureInformation(self):
        a = SignatureInformation()

        a.set_signature(1)
        a.get_signature()
        a.add_signature(1)

        a.set_signatureInformationExtension(1)
        a.get_signatureInformationExtension()
        a.add_signatureInformationExtension(1)

    def testSignature(self):
        a = Signature()

        a.set_signatureEncoding(1)
        a.get_signatureEncoding()

        a.set_signer(1)
        a.get_signer()

        a.set_signatureMethod(1)
        a.get_signatureMethod()

        a.set_signatureValue(1)
        a.get_signatureValue()

        a.set_signatureValidationRules(1)
        a.get_signatureValidationRules()

        a.set_signatureProperties(1)
        a.get_signatureProperties()
        a.add_signatureProperties(1)

        a.set_keyInformation(1)
        a.get_keyInformation()

    def testEnvironmentFunction(self):
        a = EnvironmentFunction()

        a.set_environmentFunctionType(1)
        a.get_environmentFunctionType()

        a.set_environmentFunctionLevel(1)
        a.get_environmentFunctionLevel()

    def testEnvironmentDesignation(self):
        a = EnvironmentDesignation()

        a.set_environmentName(1)
        a.get_environmentName()

        a.set_environmentVersion(1)
        a.get_environmentVersion()

        a.set_environmentOrigin(1)
        a.get_environmentOrigin()

        a.set_environmentDesignationNote(1)
        a.get_environmentDesignationNote()
        a.add_environmentDesignationNote(1)

        a.set_environmentDesignationExtension(1)
        a.get_environmentDesignationExtension()
        a.add_environmentDesignationExtension(1)

    def testEnvironmentRegistry(self):
        a = EnvironmentRegistry()

        a.set_environmentRegistryName(1)
        a.get_environmentRegistryName()

        a.set_environmentRegistryKey(1)
        a.get_environmentRegistryKey()

        a.set_environmentRegistryRole(1)
        a.get_environmentRegistryRole()

    def testRelationship(self):
        a = Relationship()

        a.set_relationshipType(1)
        a.get_relationshipType()

        a.set_relationshipSubType(1)
        a.get_relationshipSubType()

        a.set_relatedObjectIdentifier(1)
        a.get_relatedObjectIdentifier()
        a.add_relatedObjectIdentifier(1)

        a.set_relatedEventIdentifier(1)
        a.get_relatedEventIdentifier()
        a.add_relatedEventIdentifier(1)

        a.set_relatedEnvironmentPurpose(1)
        a.get_relatedEnvironmentPurpose()
        a.add_relatedEnvironmentPurpose(1)

        a.set_relatedEnvironmentCharacteristic(1)
        a.get_relatedEnvironmentCharacteristic()

    def testLinkingEventIdentifier(self):
        a = LinkingEventIdentifier()

        a.set_linkingEventIdentifierType(1)
        a.get_linkingEventIdentifierType()

        a.set_linkingEventIdentifierValue(1)
        a.get_linkingEventIdentifierValue()

    def testLinkingRightsStatementIdentifier(self):
        a = LinkingRightsStatementIdentifier()

        a.set_linkingRightsStatementIdentifierType(1)
        a.get_linkingRightsStatementIdentifierType()

        a.set_linkingRightsStatementIdentifierValue(1)
        a.get_linkingRightsStatementIdentifierValue()

    def testRelatedEventIdentifier(self):
        a = RelatedEventIdentifier()

        a.set_relatedEventIdentifierType(1)
        a.get_relatedEventIdentifierType()

        a.set_relatedEventIdentifierValue(1)
        a.get_relatedEventIdentifierValue()

        a.set_relatedEventSequence(1)
        a.get_relatedEventSequence()


    def testRelatedObjectIdentifier(self):
        a = RelatedObjectIdentifier()

        a.set_relatedObjectIdentifierType(1)
        a.get_relatedObjectIdentifierType()

        a.set_relatedObjectIdentifierValue(1)
        a.get_relatedObjectIdentifierValue()

        a.set_relatedObjectSequence(1)
        a.get_relatedObjectSequence()


    def testInhibitors(self):
        a = Inhibitors()

        a.set_inhibitorType(1)
        a.get_inhibitorType()

        a.set_inhibitorTarget(1)
        a.get_inhibitorTarget()
        a.add_inhibitorTarget(1)

        a.set_inhibitorKey(1)
        a.get_inhibitorKey()

    def testCreatingApplication(self):
        a = CreatingApplication()

        a.set_creatingApplicationName(1)
        a.get_creatingApplicationName()

        a.set_creatingApplicationVersion(1)
        a.get_creatingApplicationVersion()

        a.set_dateCreatedByApplication(1)
        a.get_dateCreatedByApplication()

        a.set_creatingApplicationExtension(1)
        a.get_creatingApplicationExtension()
        a.add_creatingApplicationExtension(1)

    def testFormat(self):
        a = Format()

        a.set_formatDesignation(1)
        a.get_formatDesignation()

        a.set_formatRegistry(1)
        a.get_formatRegistry()

        a.set_formatNote(1)
        a.get_formatNote()
        a.add_formatNote(1)

    def testFormatDesignation(self):
        a = FormatDesignation()

        a.set_formatName(1)
        a.get_formatName()

        a.set_formatVersion(1)
        a.get_formatVersion()

    def testFormatRegistry(self):
        a = FormatRegistry()

        a.set_formatRegistryName(1)
        a.get_formatRegistryName()

        a.set_formatRegistryKey(1)
        a.get_formatRegistryKey()

        a.set_formatRegistryRole(1)
        a.get_formatRegistryRole()

    def testFixity(self):
        a = Fixity()

        a.set_messageDigestAlgorithm(1)
        a.get_messageDigestAlgorithm()

        a.set_messageDigest(1)
        a.get_messageDigest()

        a.set_messageDigestOriginator(1)
        a.get_messageDigestOriginator()

if __name__ == '__main__':
    unittest.main()
