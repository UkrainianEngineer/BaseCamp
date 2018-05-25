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

import configparser
import json
import xml.etree.ElementTree as ET
import yaml


class XmlParser:
    def parse(self, file_name):
        tree = ET.parse(file_name)
        root = tree.getroot()
        my_dict = {}
        for child in root:
            child_dict = {}
            for child2 in child:
                s = child2.text
                if s.count(',')>0:
                    list_ = s.split(',')
                    new_list = []
                    for i in list_:
                        stripped = i.strip()
                        new_list.append(stripped)
                    child_dict[child2.tag] = new_list
                else:
                    child_dict[child2.tag] = child2.text
            section = child.tag
            my_dict[section] = child_dict
        return my_dict


class IniParser:
    def parse(self, file_name):
        config = configparser.ConfigParser()
        config.read(file_name)
        my_dict = {}
        for section in config.sections():
            my_dict[section] = dict(config.items(section))
        return my_dict


class YamlParser:
    def parse(self, file_name):
        file_ = open(file_name, 'r')
        yaml_ = yaml.load(file_)
        file_.close()
        return yaml_


class JsonParser:
    def parse(self, file_name):
        file_ = open(file_name, 'r')
        json_ = json.load(file_)
        file_.close()
        return json_


class Parser:
    def parse(self, file_name):
        if file_name.endswith('xml'):
            parser = XmlParser()
            return parser.parse(file_name)
        if file_name.endswith('ini'):
            parser = IniParser()
            return parser.parse(file_name)
        if file_name.endswith('yaml'):
            parser = YamlParser()
            return parser.parse(file_name)
        if file_name.endswith('json'):
            parser = JsonParser()
            return parser.parse(file_name)


# The following code should works fine.
# Each `parse` method should return a dict object
# with configuration parsed from the configuration file.
parser = Parser()
xml_data = parser.parse("config.xml")
ini_data = parser.parse("config.ini")
yaml_data = parser.parse('config.yaml')
json_data = parser.parse('config.json')
