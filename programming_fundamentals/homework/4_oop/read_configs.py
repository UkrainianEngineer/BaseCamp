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


import xml.etree.ElementTree as ET
import ConfigParser
import yaml
import ast


class XmlParser:
    @staticmethod
    def parse(file_name):
        """
        This method parses an xml file to a dictionary,
	converting string values with multiple components into a list.
        Args:
            file_name (str): Name of an xml file to be parsed.
        Returns:
            dict: Data parsed from an xml file and converted to dictionary.
        """
	tree = ET.parse(file_name)
	root = tree.getroot()
	main_dict = {}
	for element in root:
	    main_dict[element.tag] = {}
	    for item in element:
            # Split elements of string by comma to handle cases like `supported_os` etc.
                value = item.text.split(',')
                if len(value) == 1:
                # It's a simple field without lists of items.
                    value = item.text
                main_dict[element.tag][item.tag] = value
	return main_dict          


class IniParser:
    @staticmethod
    def parse(file_name):
        """
        This method parses an ini file to a dictionary,
	converting string values with multiple components into a list.
        Args:
            file_name (str): Name of an ini file to be parsed.
        Returns:
            dict: Data parsed from an ini file and converted to dictionary.
        """
	config = ConfigParser.ConfigParser()
	config.read(file_name)
	dictionary = {}
	for section in config.sections():
	    dictionary[section] = {}
	    for option in config.options(section):
		value = config.get(section, option).split(',')
                if len(value) == 1:
                # It's a simple field without lists of items.
                    value = config.get(section, option)
		dictionary[section][option] = value
	return dictionary


class YamlParser:
    @staticmethod
    def parse(file_name):
        """
        This method parses a yaml file to a dictionary.
        Args:
            file_name (str): Name of a yaml file to be parsed.
        Returns:
            dict: Data parsed from an yaml file and converted to dictionary.
        """
	stream = file(file_name, 'r')
	yaml_dict = yaml.load_all(stream)
	return yaml_dict


class JsonParser:
    @staticmethod
    def parse(file_name):
        """
        This method parses a json file to a dictionary.
        Args:
            file_name (str): Name of a json file to be parsed.
        Returns:
            dict: Data parsed from a json file and converted to dictionary.
        """
	with open(file_name) as f:
	    dict_in_string = f.read()
	# Using f.read(), a dictionary in string is returned.
	# If json library function load(), string values are returned in unicode type.
	json_in_dict = ast.literal_eval(dict_in_string)
	# literal_eval function is used to return dictionary from dictionary in string.
	return json_in_dict


class Parser:
    parser_options = {'xml': XmlParser,
		      'ini': IniParser,
		      'json': JsonParser,
		      'yaml': YamlParser}
    def parse(self, file_to_parse):
	"""
        This method parses a json file to a dictionary.
        Args:
            file_to_parse (str): Name of a file to be parsed.
        Returns:
            method: Calles method for an object with correspondng file parser class.
        """		
	filename, extension = file_to_parse.split('.')
	format_parser = self.parser_options.get(extension)
	try:
   	    return format_parser.parse(file_to_parse)
	except AttributeError as err:
	    print("Current object has no parse attribute")
	    print(err)

    """
    You should implement this class.
    """

# The following code should works fine.
# Each `parse` method should return a dict object
# with configuration parsed from the configuration file.
parser = Parser()
xml_data = parser.parse("config.xml")
ini_data = parser.parse("config.ini")
yaml_data = parser.parse('config.yaml')
json_data = parser.parse('config.json')
