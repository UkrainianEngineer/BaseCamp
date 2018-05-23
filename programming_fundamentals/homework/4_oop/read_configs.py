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
import configparser
import yaml
import json


class XmlParser:
    def parse_xml(self, filename):
        with open(filename) as data:
            config = xmltodict.parse(data.read(), process_namespaces=True)
            # http://docs.python-guide.org/en/latest/scenarios/xml/
        return config


class IniParser:
    def parse_ini(self, filename):
        # https://stackoverflow.com/questions/3220670/read-all-the-contents-in-ini-file-into-dictionary-with-python
        pars = configparser.ConfigParser()
        pars.read(filename)
        config = pars.__dict__['_sections'].copy()
        return config


class YamlParser:
    def parse_yaml(self, filename):
        with open(filename, 'r') as data:
            config = (yaml.load(data))
        return config


class JsonParser:
    def parse_json(self, filename):
        with open(filename) as data:
            config = json.loads(data.read())
        return config


class Parser(XmlParser, IniParser, YamlParser, JsonParser):
    def parse(self, filename):
        file_type = filename.split('.')[-1]
        if file_type == "xml":
            result_config = super(Parser, self).parse_xml(filename)
        elif file_type == "ini":
            result_config = super(Parser, self).parse_ini(filename)
        elif file_type == "yaml":
            result_config = super(Parser, self).parse_yaml(filename)
        elif file_type == "json":
            result_config = super(Parser, self).parse_json(filename)
        return result_config


# The following code should works fine.
# Each `parse` method should return a dict object
# with configuration parsed from the configuration file.
parser = Parser()
xml_data = parser.parse("config.xml")
print('xml: ',xml_data)
ini_data = parser.parse("config.ini")
print('ini: ',ini_data)
yaml_data = parser.parse('config.yaml')
print('yaml: ',yaml_data)
json_data = parser.parse('config.json')
print('json: ',json_data)
