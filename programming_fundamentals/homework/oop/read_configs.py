#!/usr/bin/env python
"""
This module contains tasks related to object-oriented programming in Python.
Please read docstrings and complete this task.
"""
import xml.etree.ElementTree as Payload
import json
import configparser
import yaml

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
        This function is for parsing XML file into dictionary.
        Args:
            filename (str): Name of XML file.
        Returns:
            dict: Config converted from the XML file.
        """
        def payload_to_dict(payload):
            """
            Function converts passed file into dictionary.
            Args:
                payload (xml.etree.ElementTree): File payload for parsing.
            Returns:
                dict: Parsed config.
            """
            config = {}
            for item in payload.getchildren():
                if not item.getchildren():
                    parse_items = [item.strip() for item in item.text.split(',')]
                    if len(parse_items) > 1:
                        config[item.tag] = parse_items
                    else:
                        config[item.tag] = item.text
                else:
                    config.update({item.tag: payload_to_dict(item)})
            return config
        payload = Payload.parse(filename).getroot()
        return payload_to_dict(payload)


class IniParser:
    @staticmethod
    def parse(filename):
        """
        This function is for parsing INI file into dictionary.
        Args:
            filename (str): Name of INI file.
        Returns:
            dict: Converted config from INI file.
        """
        config = configparser.ConfigParser()
        config.read(filename)
        output_dict = {}
        for section in config.sections():
            output_dict.update({section: {}})
            for key in config.options(section):
                value = config.get(section, key)
                value_list = [item.strip() for item in value.split(',')]
                if len(value_list) > 1:
                    output_dict[section].update({key: value_list})
                else:
                    output_dict[section].update({key: value})
        return output_dict


class YamlParser:
    @staticmethod
    def parse(filename):
        """
        This function is for parsing yaml file into dictionary.
        Args:
            filename (str): Name of yaml file.
        Returns:
            dict: Converted config from yaml file.
        """
        config = {}
        try:
            with open(filename, 'r') as file:
                config = yaml.load(file)
        except (IOError, yaml.YAMLError) as e:
            print("File {} can't be open with the exception:\n{}".format(filename, e))
        return config


class JsonParser:
    @staticmethod
    def parse(filename):
        """
        This function is for parsing JSON file into dictionary.
        Args:
            filename (str): Name of JSON file.
        Returns:
            dict: Converted config from JSON file.
        """
        config = {}
        try:
            with open(filename, 'r') as file:
                config = json.load(file)
        except (IOError, ValueError) as e:
            print("File {} can't be open with the exception:\n{}".format(filename, e))
        return config


class Parser:
    parsers = {'ini': IniParser,
               'json': JsonParser,
               'yaml': YamlParser,
               'xml': XmlParser
               }

    @staticmethod
    def parse(filename):
        for item in Parser.parsers:
            if item in filename:
                parser = Parser.parsers.get(item)
        if parser is not None:
            return parser.parse(filename)
        else:
            print('No parser found for {}'.format(filename))


# The following code should works fine.
# Each `parse` method should return a dict object
# with configuration parsed from the configuration file.
parser = Parser()
xml_data = parser.parse("config.xml")
ini_data = parser.parse("config.ini")
yaml_data = parser.parse('config.yaml')
json_data = parser.parse('config.json')
