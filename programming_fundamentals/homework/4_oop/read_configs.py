#!/usr/bin/env python
import configparser
import json
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
    """ Parsing xml file.
        Saving child elements of root as keys
        and their child elements as values
    """
    def parse (self, filename):
        if filename.split('.')[-1] != 'xml':
            return None
        xml_dict = {}
        e = xml.etree.ElementTree.parse(filename).getroot()
        for child in e:
            inner_dict = {}
            for grand_child in child:
                inner_dict[grand_child.tag] = grand_child.text
            xml_dict[child.tag] = inner_dict
        return xml_dict


class IniParser:
    """ Parsing ini file.
        Catch exceptions if problem with file parsing ocurred
    """
    def parse(self, filename):
        config = configparser.ConfigParser()
        try:
            config.read(filename)
            config_dict = {s:dict(config.items(s)) for s in config.sections()}
        except (ParsingError) as e:
            return e
        return config_dict


class YamlParser:
    pass


class JsonParser:
    """ Parsing json file.
        Catch exceptions if problem with file opening ocurred
    """
    def parse(self, filename):
        try:
            with open(filename) as data:
                config = json.loads(data.read())
        except (OSError, IOError) as e:
            return e
        return config


class Parser:
    """
    You should implement this class.
    """
    mapping = {'xml': XmlParser,
               'ini': IniParser,
               'yaml': YamlParser,
               'json': JsonParser
              }

    def parse(self, filename):
        # Store filename extension
        filename_extension = filename.split('.')[-1]
        parser = self.mapping.get(filename_extension)
        return parser.parse(self, filename)




# The following code should works fine.
# Each `parse` method should return a dict object
# with configuration parsed from the configuration file.

parser = Parser()
xml_data = parser.parse("config.xml")
print (xml_data)
ini_data = parser.parse("config.ini")
print (ini_data)
"""yaml_data = parser.parse('config.yaml')"""
json_data = parser.parse('config.json')
print (json_data)