#!/usr/bin/env python
try :
    import xml.etree.cElementTreex as ET
except :
    import xml.etree.ElementTree as ET
import yaml
import json
#from pprint import pprint
from configparser import ConfigParser


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
    def parse (self, filename):
        main_tree = ET.parse(filename)   #main branch
        root = main_tree.getroot()
        xdict = {}
        for chld in root:
            ch_dict = {}
            for g_ch in chld:
                ch_dict[g_ch.tag] = g_ch.text
            xdict[chld.tag] = ch_dict
        return xdict
    
class IniParser:
    def parse (self, filename):
        prs = ConfigParser()
        prs.read(filename)
        d = {}
        for sect in prs.sections() :
            d[sect] = dict(prs.items(sect))
        return d
        
class YamlParser:
    pass

class JsonParser:
    def parse(self, filename) :
        data = {}
        with open(filename) as f:
            data = json.load(f)
        return data
        #pprint(data)

class Parser(XmlParser, IniParser, YamlParser, JsonParser) :
    def parse(self, file_name) :
        
        if file_name.lower().endswith('xml') == True :
            parser = XmlParser()
            return parser.parse(file_name)
        
        elif file_name.lower().endswith('ini') == True:
            parser = IniParser()
            return parser.parse(file_name)
        
        elif file_name.lower().endswith('yaml') == True :
            parser = YamlParser()
            return parser.parse(file_name)
        
        elif file_name.lower().endswith('json') == True:
            parser = JsonParser()
            return parser.parse(file_name)
        else :
            print("Unknown type of file!")
    """
    You should implement this class.
    """
    #def parse(self, filename):
        #parsed_dict = super().parse(filename)
        #return parsed_dict

# The following code should works fine.
# Each `parse` method should return a dict object
# with configuration parsed from the configuration file.

parser = Parser()
xml_data = parser.parse("config.xml")

ini_data = parser.parse("config.ini")
#yaml_data = parser.parse('config.yaml')
json_data = parser.parse('config.json')
