import xml.etree.ElementTree
import json
import yaml
import configparser

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


class XmlParser:
    """This XmlParser class reads file 'xml' type and return file context as a dictionary.

    Arg: filename(str) - file name for reading

    Return: data(dict) - file context
    """
    def parse(self, filename):
        try:
            file_text = xml.etree.ElementTree.parse(filename).getroot()
            data = {}
            for key in file_text:
                data[key.tag] = {}
                for sub_key in key:
                    data[key.tag][sub_key.tag] = sub_key.text
            return data
        except (KeyError, TypeError, ValueError):
            print("An Error has occurred!")
    # "https://docs.python.org/3/library/xml.etree.elementtree.html"


class IniParser:
    """This IniParser class reads file 'ini' type and return file context as a dictionary.

    Arg: filename(str) - file name for reading

    Return: data(dict) - file context
    """
    def parse(self, filename):
        try:
            config = configparser.ConfigParser()
            config.read(filename)
            data = {}
            for section in config.sections():
                data[section] = {}
                for key in config[section]:
                    data[section][key] = config[section][key]
            return data
        except (OSError, IOError, KeyError, TypeError):
            print("An Error has occurred!")
        # "https://docs.python.org/3/library/configparser.html"


class YamlParser:
    """This YamlParser class reads file 'yaml' type and return file context as a dictionary.

    Arg: filename(str) - file name for reading

    Return: data(dict) - file context
    """
    def parse(self, filename):
        try:
            with open(filename) as file:
                data = yaml.load(file)
            return data
        except (OSError, IOError):
            print("An Error has occurred!")
    # "https://stackoverflow.com/questions/25814568/is-it-possible-to-use-pyyaml-to-read-a-text-file-written-with-a-yaml-front-matt"


class JsonParser:
    """This JsonParser class reads file 'json' type and return file context as a dictionary.

        Arg: filename(str) - file name for reading

        Return: data(dict) - file context
        """
    def parse(self, filename):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
            return data
        except (OSError, IOError):
            print("An Error has occurred!")
    # "https://stackoverflow.com/questions/2835559/parsing-values-from-a-json-file"


class Parser:

    def parse(self, filename):
        """    This 'parse' function reads files of different formats (like 'yaml', 'json', 'ini' or 'xml')
        and return file context as a dictionary.

        Arg: filename(str) - file name for reading

        Return: (dict) - file context
        """
        extension = filename.split(".")[-1]
        mapping = {
            "xml": XmlParser(),
            "ini": IniParser(),
            "yaml": YamlParser(),
            "json": JsonParser()
            }
        return mapping[extension].parse(filename)

# The following code should works fine.
# Each `parse` method should return a dict object
# with configuration parsed from the configuration file.

parser = Parser()
xml_data = parser.parse("config.xml")
ini_data = parser.parse("config.ini")
yaml_data = parser.parse('config.yaml')
json_data = parser.parse('config.json')
