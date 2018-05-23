#!/usr/bin/env python
"""
This module contains tasks related to object-oriented programming in Python.
Please read docstrings and complete this task.
"""

# to the .ini files
import configparser
# to the .xml files
from xml.etree import cElementTree as ET
# to the .json files
import json
# to the .yaml files
import yaml


__author__ = "Pavlo Ivanchyshyn"
__maintainer__ = "Pavlo Ivanchyshyn"
__email__ = "p.ivanchyshyn@gmail.com"

# You should create a custom configuration parser.
# It should be able to parse *.ini, *.json, *.yaml and *.xml files.
# You should implement an appropriate classes for each configuration format.


class XmlParser:

    @staticmethod
    def parse():
        tree = ET.parse('config.xml')
        root = tree.getroot()
        conf_dict = {}
        for item in root:
            d = {}
            for elem in item:
                d[elem.tag] = elem.text
                conf_dict.update(d)
        return conf_dict


# print(XmlParser.parse())


class IniParser:

    @staticmethod
    def parse():
        config = configparser.ConfigParser()
        config.read("config.ini")
        conf_dict = {section: dict(config.items(section)) for section in config.sections()}
        return conf_dict


# print(IniParser.parse())


class YamlParser:

    @staticmethod
    def parse():
        conf_dict = yaml.load(open('config.yaml'))
        return conf_dict


# print(YamlParser.parse())


class JsonParser:

    @staticmethod
    def parse():
        with open('config.json') as f:
            conf_dict = json.load(f)
        return conf_dict


# print(JsonParser.parse())


class Parser:
    """
    You should implement this class.
    """
    pass

# The following code should works fine.
# Each `parse` method should return a dict object
# with configuration parsed from the configuration file.


parser = Parser()
xml_data = parser.parse("config.xml")
ini_data = parser.parse("config.ini")
yaml_data = parser.parse('config.yaml')
json_data = parser.parse('config.json')
