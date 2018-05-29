#!/usr/bin/env python
"""
This module contains tasks related to object-oriented programming in Python.
Please read docstrings and complete this task.
"""

import re
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

    def parse_xml(self, file):
        try:
            tree = ET.parse(file)
            root = tree.getroot()
            conf_dict = {}
            for item in root:
                d = {}
                for elem in item:
                    d[elem.tag] = elem.text
                    conf_dict.update(d)
            return conf_dict
        except (IOError, RuntimeError):
            print("Error: File does not appear to exist.")
            return {}


class IniParser:

    def parse_ini(self, file):
        config = configparser.ConfigParser()
        try:
            config.read(file)
            conf_dict = {section: dict(config.items(section))
                         for section in config.sections()}
            return conf_dict
        except (IOError, RuntimeError):
            print("Error: File does not appear to exist.")
            return {}


class YamlParser:

    def parse_yaml(self, file):
        try:
            conf_dict = yaml.load(open(file))
            return conf_dict
        except (IOError, RuntimeError):
            print("Error: File does not appear to exist.")
            return {}


class JsonParser:

    def parse_json(self, file):
        try:
            with open(file) as f:
                conf_dict = json.load(f)
            return conf_dict
        except (IOError, RuntimeError):
            print("Error: File does not appear to exist.")
            return {}


class Parser:

    def parse(self, file):
        pattern = "\w+\.(\w+)"
        file_type = re.findall(pattern, file, flags=re.IGNORECASE)
        if file_type[0] == "xml":
            value = XmlParser().parse_xml(file)
        elif file_type[0] == "ini":
            value = IniParser().parse_ini(file)
        elif file_type[0] == "yaml":
            value = YamlParser().parse_yaml(file)
        elif file_type[0] == "json":
            value = JsonParser().parse_json(file)
        else:
            raise Exception("Not implemented from this file type")
        return value

# The following code should works fine.
# Each `parse` method should return a dict object
# with configuration parsed from the configuration file.


parser = Parser()
xml_data = parser.parse("config.xml")
ini_data = parser.parse("config.ini")
yaml_data = parser.parse('config.yaml')
json_data = parser.parse('config.json')
