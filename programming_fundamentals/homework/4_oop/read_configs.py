#!/usr/bin/env python
"""
This module contains tasks related to object-oriented programming in Python.
Please read docstrings and complete this task.
"""
import json
import xml.etree.ElementTree as ET
import yaml
from configparser import ConfigParser

__author__ = "Pavlo Ivanchyshyn"
__maintainer__ = "Pavlo Ivanchyshyn"
__email__ = "p.ivanchyshyn@gmail.com"


# You should create a custom configuration parser.
# It should be able to parse *.ini, *.json, *.yaml and *.xml files.
# You should implement an appropriate classes for each configuration format.


class XmlParser:
    def parse(self, filename):
        data = {}
        tree = ET.parse(filename).getroot()

        for tag in tree:
            data[tag.tag] = {}
            for child_tag in tag:
                key = child_tag.tag
                value = child_tag.text

                if ',' in value:
                    value_to_list = list(map(lambda x: x.strip(), value.split(',')))
                    data[tag.tag].update({key: value_to_list})
                else:
                    data[tag.tag].update({key: value})

        return data


class IniParser:
    def parse(self, filename):
        data = {}
        config = ConfigParser()
        config.read(filename, encoding='utf-8')

        for section in config.sections():
            data[section] = {}
            for option in config.options(section):
                value = config.get(section, option)

                if ',' in value:
                    value_to_list = list(map(lambda x: x.strip(), value.split(',')))
                    data[section].update({option: value_to_list})
                else:
                    data[section].update({option: value})

        return data


class YamlParser:
    def parse(self, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as yaml_data:
                data = yaml.load(yaml_data)
        except (OSError, IOError) as exc:
            print('Exception raised: ', exc)

        return data


class JsonParser:
    def parse(self, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as json_data:
                data = json.load(json_data)
        except (OSError, IOError) as exc:
            print('Exception raised: ', exc)

        return data


class Parser:
    """
    You should implement this class.
    """
    def parse(self, filename):
        file_extention = filename.split('.')[-1]

        if file_extention == 'ini':
            parser = IniParser()

            return parser.parse(filename)
        elif file_extention == 'json':
            parser = JsonParser()

            return parser.parse(filename)
        elif file_extention == 'xml':
            parser = XmlParser()

            return parser.parse(filename)
        elif file_extention == 'yaml':
            parser = YamlParser()

            return parser.parse(filename)


# The following code should works fine.
# Each `parse` method should return a dict object
# with configuration parsed from the configuration file.
parser = Parser()
xml_data = parser.parse("config.xml")
ini_data = parser.parse("config.ini")
yaml_data = parser.parse('config.yaml')
json_data = parser.parse('config.json')

print(xml_data)
print(ini_data)
print(yaml_data)
print(json_data)

