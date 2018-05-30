#!/usr/bin/env python
"""
This module contains tasks related to object-oriented programming in Python.
Please read docstrings and complete this task.
"""
import json
import configparser
import yaml
import xml.etree.ElementTree as ET

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
        Function implements parsing XMl-file.

        Args:
            filename (str): File's name for parsing.

        Returns:
            dict: Parsed XML-file
        """
        xml_dict = {}

        tree = ET.parse(filename)
        root = tree.getroot()

        for child in root:
            xml_dict[child.tag] = {}
            for elem in child:
                elem_list = [item.strip() for item in elem.text.split(',')]
                if len(elem_list) > 1:
                    xml_dict[child.tag][elem.tag] = elem_list
                else:
                    xml_dict[child.tag][elem.tag] = elem.text

        return xml_dict


class IniParser:

    @staticmethod
    def parse(filename):
        """
        Function implements parsing ini-file.

        Args:
             filename (str): File's name for parsing.

        Returns:
            dict: Parsed ini-file.
        """
        config_dict = {}

        config = configparser.ConfigParser()
        config.read(filename)

        for section_name in config.sections():
            config_dict[section_name] = {}
            for key, value in config.items(section_name):
                value_list = [elem.strip() for elem in value.split(',')]
                if len(value_list) > 1:
                    config_dict[section_name][key] = value_list
                else:
                    config_dict[section_name][key] = value

        return config_dict


class YamlParser:

    @staticmethod
    def parse(filename):
        """
        Function implements parsing yaml-file.

        Args:
            filename (str): File's name for parsing.

        Returns:
            dict: Parsed yaml-file.
        """
        yaml_dict = {}
        try:
            with open(filename) as file:
                yaml_dict = yaml.load(file)
        except (OSError, IOError) as err:
            print('Could not read file:', err)

        return yaml_dict


class JsonParser:

    @staticmethod
    def parse(filename):
        """
        Function implements parsing json-file.

        Args:
             filename (str): File's name for parsing.

        Returns:
            dict: Parsed json-file.
        """
        json_dict = {}
        try:
            with open(filename) as file:
                json_dict = json.load(file)
        except (OSError, IOError) as err:
            print('Could not read file:', err)

        return json_dict


class Parser:
    """
    You should implement this class.
    """
    file_types = {
        'xml': XmlParser,
        'ini': IniParser,
        'yaml': YamlParser,
        'json': JsonParser
    }

    @staticmethod
    def parse(filename):

        file_type = filename.split('.')[-1]
        parser = Parser.file_types.get(file_type)

        try:
            return parser.parse(filename)
        except AttributeError as err:
            print('Error occurred in file \'{}\':'.format(filename), err)


# The following code should works fine.
# Each `parse` method should return a dict object
# with configuration parsed from the configuration file.
parser = Parser()
xml_data = parser.parse("config.xml")
ini_data = parser.parse("config.ini")
yaml_data = parser.parse('config.yaml')
json_data = parser.parse('config.json')
