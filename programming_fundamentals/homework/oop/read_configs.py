#!/usr/bin/env python
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

import xmltodict
import json
import configparser
import yaml


class XmlParser:
    '''
    Method converts passed .xml file into dictionary.
    Args: filename (str) - file name, that should be converted into distionary.
    Returns: dict - dictionary with data from .xml file.
    '''

    def parse(self, file_name):
        with open(file_name) as xml_file:
            try:
                data_from_xml = xmltodict.parse(xml_file.read())
                xml_to_dict = json.loads(json.dumps(data_from_xml))['config']
                return xml_to_dict
            except:
                pass


class IniParser:
    '''
    Method converts passed .ini file into dictionary.
    Args: filename (str) - file name, that should be converted into distionary.
    Returns: dict - dictionary with data from .ini file.
    '''

    def parse(self, file_name):
        try:
            ini_config = configparser.ConfigParser()
            ini_config.read(file_name)
            ini_to_dict = json.loads(json.dumps(ini_config.__dict__['_sections']))
            return ini_to_dict
        except:
            pass


class YamlParser:
    '''
    Method converts passed .yaml file into dictionary.
    Args: filename (str) - file name, that should be converted into distionary.
    Returns: dict - dictionary with data from .yaml file.
    '''

    def parse(self, file_name):
        try:
            with open(file_name, 'r') as yaml_file:
                yaml_to_dict = yaml.load(yaml_file)
            return yaml_to_dict
        except:
            pass


class JsonParser:
    '''
    Method converts passed .json file into dictionary.
    Args: filename (str) - file name, that should be converted into distionary.
    Returns: dict - dictionary with data from .json file.
    '''

    def parse(self, file_name):
        try:
            with open(file_name, 'r') as json_file:
                json_to_dict = json.loads(json_file.read())
                return json_to_dict
        except:
            pass


class Parser:

    def __init__(self):
        self.parsers = [XmlParser(), IniParser(), YamlParser(), JsonParser()]

    def parse(self, file_name):
        final_data = None
        for parser in self.parsers:
            if isinstance(parser.parse(file_name), dict):
                final_data = parser.parse(file_name)
        return final_data

# The following code should works fine.
# Each `parse` method should return a dict object
# with configuration parsed from the configuration file.
parser = Parser()

xml_data = parser.parse("config.xml")
ini_data = parser.parse("config.ini")
yaml_data = parser.parse('config.yaml')
json_data = parser.parse('config.json')
