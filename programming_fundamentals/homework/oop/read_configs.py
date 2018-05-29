#!/usr/bin/env python
import xml.etree.ElementTree

"""
This module contains tasks related to object-oriented programming in Python.
Please read docstrings and complete this task.
"""
__author__ = "Pavlo Ivanchyshyn"
__maintainer__ = "Pavlo Ivanchyshyn"
__email__ = "p.ivanchyshyn@gmail.com"

# You should create a custom configuration parser.
# It should be able to parse *.ini, *.json, *.yaml and *.xml files.
# You should implement an appropriate classes for each configuration format.

class XmlParser:
    def parse (self, filename):
        if filename.split('.')[1] != 'xml':
            return None
        xml_dict = {}
        e = xml.etree.ElementTree.parse(filename).getroot()
        for child in e:
            inner_dict = {}
            for grand_child in child:
                inner_dict[grand_child.tag] = grand_child.text
            xml_dict[child.tag] = inner_dict
        return (xml_dict)


class IniParser:
    pass


class YamlParser:
    pass


class JsonParser:
    pass


class Parser(XmlParser, IniParser, YamlParser, JsonParser):
    """
    You should implement this class.
    """
    def parse(self, filename):
        parsed_dict = super().parse(filename)
        return parsed_dict




# The following code should works fine.
# Each `parse` method should return a dict object
# with configuration parsed from the configuration file.

parser = Parser()
xml_data = parser.parse("config.xml")
"""ini_data = parser.parse("config.ini")
yaml_data = parser.parse('config.yaml')
json_data = parser.parse('config.json')"""