# pypremis #

## Whats New? ##
* First official release coming soon...

## Introduction ##
Pypremis is a project which aims to make the [PREMISv3](http://www.loc.gov/standards/premis/v3/index.html) metadata standard easily accessible via python library code. This project aims to correctly implement PREMIS metadata creation and reading, mandating full compliance to the PREMIS specification and data dictionary

## Usage Examples ##

### Read an existing PREMIS xml record ###

```python
>>> from pypremis.lib import PremisRecord
>>> example_record = PremisRecord(frompath='testObject.xml')
>>> example_object = example_record.get_object_list()[0]
>>> print(example_object.get_objectIdentifier(0))
<premis:objectIdentifier><premis:objectIdentifierType>object_identifier_type</premis:objectIdentifierType><premis:objectIdentifierValue>object_identifier_value</premis:objectIdentifierValue></premis:objectIdentifier>
>>> example_object_identifier = example_object.get_objectIdentifier(0)
>>> print(example_object_identifier.get_objectIdentifierValue())
object_identifier_value
>>>
```

### Create a PREMIS record from scratch ###

```python
>>> from pypremis.lib import PremisRecord
>>> from pypremis.nodes import *
>>> object_identifier = ObjectIdentifier('object id type example value', 'object id value example value')
>>> format_designation = FormatDesignation(formatName='format name example value')
>>> format = Format(formatDesignation=format_designation)
>>> object_characteristics = ObjectCharacteristics(format=format)
>>> o = Object(object_identifier, "file", object_characteristics)
>>> print(o)
<premis:object xsi:type="premis:file"><premis:objectIdentifier><premis:objectIdentifierType>object id type example value</premis:objectIdentifierType><premis:objectIdentifierValue>object id value example value</premis:objectIdentifierValue></premis:objectIdentifier><premis:objectCharacteristics><premis:format><premis:formatDesignation><premis:formatName>format name example value</premis:formatName></premis:formatDesignation></premis:format></premis:objectCharacteristics></premis:object>
>>> example_record = PremisRecord(objects=[o])
>>> example_record.write_to_file('example_record.xml')
>>> exit()
```
```bash
$ cat example_record.xml | xmllint -format -
<?xml version="1.0" encoding="utf-8"?>
<premis:premis xmlns:premis="http://www.loc.gov/premis/v3" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" version="3.0">
  <premis:object xsi:type="premis:file">
    <premis:objectIdentifier>
      <premis:objectIdentifierType>object id type example value</premis:objectIdentifierType>
      <premis:objectIdentifierValue>object id value example value</premis:objectIdentifierValue>
    </premis:objectIdentifier>
    <premis:objectCharacteristics>
      <premis:format>
        <premis:formatDesignation>
          <premis:formatName>format name example value</premis:formatName>
        </premis:formatDesignation>
      </premis:format>
    </premis:objectCharacteristics>
  </premis:object>
</premis:premis>
```

### Manipulate and add to records easily ###
```python
>>> from pypremis.lib import PremisRecord
>>> from pypremis.nodes import *
>>> example_record = PremisRecord(frompath='example_record.xml')
>>> obj = example_record.get_object_list()[0]
>>> obj.set_originalName('example_file.txt')
>>> obj.get_objectIdentifier(0).set_objectIdentifierType('not the same type as before')
>>> example_record.write_to_file('example_record_v2.xml')
>>> exit()
```
```bash
$ cat example_record_v2.xml | xmllint -format -
<?xml version="1.0" encoding="utf-8"?>
<premis:premis xmlns:premis="http://www.loc.gov/premis/v3" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" version="3.0">
  <premis:object xsi:type="premis:file">
    <premis:objectIdentifier>
      <premis:objectIdentifierType>not the same type as before</premis:objectIdentifierType>
      <premis:objectIdentifierValue>object id value example value</premis:objectIdentifierValue>
    </premis:objectIdentifier>
    <premis:objectCharacteristics>
      <premis:format>
        <premis:formatDesignation>
          <premis:formatName>format name example value</premis:formatName>
        </premis:formatDesignation>
      </premis:format>
    </premis:objectCharacteristics>
    <premis:originalName>example_file.txt</premis:originalName>
  </premis:object>
</premis:premis>
```

## Author ##
Brian Balsamo
balsamo@uchicago.edu
