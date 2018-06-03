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
            except Exception as errors:
                print('Unable to parse {} file: {}'.format(file_name, errors))


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
        except Exception as errors:
            print('Unable to parse {} file: {}'.format(file_name, errors))


class YamlParser:
    '''
    Method converts passed .yaml file into dictionary.
    Args: filename (str) - file name, that should be converted into distionary.
    Returns: dict - dictionary with data from .yaml file.
    '''

    def parse(self, file_name):
        try:
            with open(file_name, 'r') as yaml_file:
                return yaml.load(yaml_file)
        except Exception as errors:
            print('Unable to parse {} file: {}'.format(file_name, errors))


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
        except Exception as errors:
            print('Unable to parse {} file: {}'.format(file_name, errors))


class Parser:

    def parse(self, file_name):
        file_extension = file_name.split('.')[-1]
        if file_extension == 'xml':
            return XmlParser().parse(file_name)
        elif file_extension == 'ini':
            return IniParser().parse(file_name)
        elif file_extension == 'yaml':
            return YamlParser().parse(file_name)
        elif file_extension == 'json':
            return JsonParser().parse(file_name)


# The following code should works fine.
# Each `parse` method should return a dict object
# with configuration parsed from the configuration file.
parser = Parser()

xml_data = parser.parse("config.xml")
ini_data = parser.parse("config.ini")
yaml_data = parser.parse('config.yaml')
json_data = parser.parse('config.json')
