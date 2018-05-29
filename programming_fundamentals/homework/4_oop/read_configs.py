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

import xml.etree.cElementTree as ET
import configparser
from yaml import load
import json

class XmlParser:
    def xml_parser(self, file_name):
        tree = ET.parse(file_name)
        root = tree.getroot()
        appointments = root.getchildren()

        config_data = {}

        for appointment in appointments:
            appt_children = appointment.getchildren()
            for appt_child in appt_children:
                config_data[appt_child.tag] = appt_child.text
        return config_data


class IniParser:
    def ini_parser(self, file_name):
        config_data = {}
        config = configparser.ConfigParser()
        config.read(file_name)
        for main_key in config.sections():
            for child_key in config[main_key]:
                config_data[child_key] = config[main_key][child_key]
        return config_data


class YamlParser:
    def yaml_parser(self, file_name):
        with open(file_name) as fp:
            return load(fp)


class JsonParser:
    def json_parser(self, file_name):
        with open(file_name) as fp:
            confi_data = json.load(fp)
            return confi_data


class Parser(XmlParser, IniParser, YamlParser, JsonParser):
    def parse(self, input_file):
        format_file = input_file.split(".")
        format_file = format_file[-1].lower()
        if format_file == "xml":
            return super().xml_parser(input_file)
        elif format_file == "ini":
            return super().ini_parser(input_file)
        elif format_file == "yaml":
            return  super().yaml_parser(input_file)
        elif format_file == "json":
            return  super().json_parser(input_file)

# The following code should works fine.
# Each `parse` method should return a dict object
# with configuration parsed from the configuration file.
parser = Parser()
xml_data = parser.parse("config.xml")
ini_data = parser.parse("config.ini")
yaml_data = parser.parse('config.yaml')
json_data = parser.parse('config.json')