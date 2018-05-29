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

import json
import yaml
import configparser
import xmltodict

class XmlParser:
    
    def parse(config_file):

        parsed_file = xmltodict.parse(config_file)
        return dict(parsed_file)
        


class IniParser:
    
    def parse(config_file):
        
        parsed_file = configparser.ConfigParser()
        return parsed_file.read(config_file)


class YamlParser:
    def parse(config_file):
        
        parsed_file = yaml.load(config_file)
        return parsed_file


class JsonParser:
    
    def parse(config_file):
        
        
        parsed_file = json.loads(config_file)
        return parsed_file


class Parser:
    """
    You should implement this class.
    """
    def __init__(self):
        pass
    
    def parse(self, config_file):

        with open(config_file, 'r') as stream:
            a_file = stream.read()
        
        file_type = config_file.split('.')[1]

        if file_type == 'xml':
           parsed_config = XmlParser.parse(a_file)
        elif file_type == 'ini':
           parsed_config = IniParser.parse(a_file)
        elif file_type == 'yaml':
           parsed_config = YamlParser.parse(a_file)
        elif file_type == 'json':
           parsed_config = JsonParser.parse(a_file)
        
        return parsed_config

  
# The following code should works fine.
# Each `parse` method should return a dict object
# with configuration parsed from the configuration file.
parser = Parser()
xml_data = parser.parse("config.xml")
ini_data = parser.parse("config.ini")
yaml_data = parser.parse('config.yaml')
json_data = parser.parse('config.json')

'''
print(xml_data)
print(ini_data)
print(yaml_data)
print(json_data)
'''
