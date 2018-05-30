#!/usr/bin/env python
"""
This module contains tasks related to object-oriented programming in Python.
Please read docstrings and complete this task.
"""
import xml.etree.ElementTree as ET
import json
import configparser
import yaml
from collections import defaultdict

__author__ = "Pavlo Ivanchyshyn"
__maintainer__ = "Pavlo Ivanchyshyn"
__email__ = "p.ivanchyshyn@gmail.com"

# You should create a custom configuration parser.
# It should be able to parse *.ini, *.json, *.yaml and *.xml files.
# You should implement an appropriate classes for each configuration format.


class XmlParser:
    @staticmethod
    def parse(filename):
        """
        Function parses passed file into dictionary.

        Args:
            filename (str): Name of file for reading .

        Returns:
            dict: Converted from xml-file config.
        """
        def tree_to_dict(tree):
            """
            Function converts passed tree into dictionary.

            Args:
                tree (xml.etree.ElementTree): Tree root for parsing.

            Returns:
                dict: Parsed from tree config.
            """
            config = {}
            for tree_tag in tree.getchildren():
                if not tree_tag.getchildren():
                    tree_tag_items = [item.strip() for item in tree_tag.text.split(',')]
                    if len(tree_tag_items) > 1:
                        config[tree_tag.tag] = tree_tag_items
                    else:
                        config[tree_tag.tag] = tree_tag.text
                else:
                    config.update({tree_tag.tag: tree_to_dict(tree_tag)})
            return config
        tree = ET.parse(filename).getroot()
        return tree_to_dict(tree)


class IniParser:
    @staticmethod
    def parse(filename):
        """
        Function parses passed file into dictionary.

        Args:
            filename (str): Name of file for reading .

        Returns:
            dict: Converted from ini-file config.
        """
        config_obj = configparser.ConfigParser()
        config_obj.read(filename)
        config = {}
        for section in config_obj.sections():
            config.update({section: {}})
            for key in config_obj.options(section):
                value = config_obj.get(section, key)
                value_list = [item.strip() for item in value.split(',')]
                if len(value_list) > 1:
                    config[section].update({key: value_list})
                else:
                    config[section].update({key: value})
        return config


class YamlParser:
    @staticmethod
    def parse(filename):
        """
        Function parses passed file into dictionary.

        Args:
            filename (str): Name of file for reading .

        Returns:
            dict: Converted from yaml-file config.
        """
        config = {}
        try:
            with open(filename, 'r') as file:
                try:
                    config = yaml.load(file)
                except yaml.YAMLError as exc:
                    print(exc)
        except (OSError, IOError):
            print('File "{}" cannot be opened.'.format(filename))
        return config


class JsonParser:
    @staticmethod
    def parse(filename):
        """
        Function parses passed file into dictionary.

        Args:
            filename (str): Name of file for reading .

        Returns:
            dict: Converted from json-file config.
        """
        config = {}
        try:
            with open(filename, 'r') as file:
                config = json.load(file)
        except (OSError, IOError):
            print('File "{}" cannot be opened.'.format(filename))
        return config


class Parser:
    parsers = {'ini': IniParser,
               'json': JsonParser,
               'yaml': YamlParser,
               'xml': XmlParser}

    def parse(self, filename):
        extension_position = -1
        file_extension = filename.split('.')[extension_position]
        parser = self.parsers.get(file_extension)
        if parser is not None:
            return parser.parse(filename)
        else:
            raise Exception('No suitable parser found for {}'.format(filename))


# The following code should works fine.
# Each `parse` method should return a dict object
# with configuration parsed from the configuration file.
parser = Parser()
xml_data = parser.parse("config.xml")
ini_data = parser.parse("config.ini")
yaml_data = parser.parse('config.yaml')
json_data = parser.parse('config.json')
