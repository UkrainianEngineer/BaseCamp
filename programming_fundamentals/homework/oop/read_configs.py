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
    def parse_xml(self, filesname):
        # Plug in a function that is able to parse a text file into an xml document.
        from xml.dom.minidom import parse
        # Parse text into xml document.
        doc = parse(filesname)
        # Take out all elements.
        config_element = doc.getElementsByTagName("config")[0]
        server_element = config_element.getElementsByTagName("server")[0]
        hostname_element = server_element.getElementsByTagName("hostname")[0]
        hostname_value = hostname_element.firstChild.nodeValue
        port_element = server_element.getElementsByTagName("port")[0]
        port_value = port_element.firstChild.nodeValue
        os_element = server_element.getElementsByTagName("os")[0]
        os_value = os_element.firstChild.nodeValue
        default_element = config_element.getElementsByTagName("default")[0]
        configuration_folder_element = default_element.getElementsByTagName("configuration_folder")[0]
        configuration_folder_value = configuration_folder_element.firstChild.nodeValue
        version_element = default_element.getElementsByTagName("version")[0]
        version_value = version_element.firstChild.nodeValue
        supported_os_element = default_element.getElementsByTagName("supported_os")[0]
        supported_os_value = supported_os_element.firstChild.nodeValue
        return {
                'server': {
                    'hostname': hostname_value,
                    'port': port_value,
                    'os': os_value
                    },
                'default': {
                   'configuration_folder': configuration_folder_value,
                    'version': version_value,
                    'supported_os': supported_os_value
                    }
                }



class IniParser:
    def parse_ini(self, filesname):
        # http: // pyyaml.org / wiki / PyYAMLDocumentation
        # Connect parser of ini file.
        import configparser
        # Create an object parser.
        config = configparser.ConfigParser()
        # Parse a file.
        config.read(filesname)
        # Extract the value from the configuration.
        server_hostname_value = config.get('server', 'hostname')
        server_port_value = config.get('server', 'port')
        server_os_value = config.get('server', 'OS')
        default_configuration_folder_value = config.get('default', 'configuration_folder')
        default_version_value = config.get('default', 'version')
        default_supported_os_value = config.get('default', 'supported_os')
        return {
                'server': {
                    'hostname': server_hostname_value,
                    'port': server_port_value,
                    'OS': server_os_value
                    },
                'default': {
                    'configuration_folder': default_configuration_folder_value,
                    'version': default_version_value,
                    'supported_os': default_supported_os_value
                    }
                }




class YamlParser:
    def parse_yaml(self, filesname):
        # http://pyyaml.org/wiki/PyYAMLDocumentation
        import yaml
        with open(filesname, 'r') as stream:
            data_loaded = yaml.load(stream)
            return data_loaded


class JsonParser:
    def parse_json(self, filesname):
        # http://developer.rhino3d.com/guides/rhinopython/python-xml-json/
        import json
        with open(filesname, 'r') as stream:
            datastore = json.loads(stream.read())
            return datastore

class Parser:
    """
    You should implement this class.
    """

    def parse(self, filesname):
        if filesname.endswith(".xml"):
            xml_parser = XmlParser()
            return xml_parser.parse_xml(filesname)
        elif filesname.endswith(".ini"):
            ini_parser = IniParser()
            return ini_parser.parse_ini(filesname)
        elif filesname.endswith(".yaml"):
            yaml_data = YamlParser()
            return yaml_data.parse_yaml(filesname)
        elif filesname.endswith(".json"):
            json_data = JsonParser()
            return json_data.parse_json(filesname)
        else:
            raise Exception('Unknown config type')

# The following code should works fine.
# Each `parse` method should return a dict object
# with configuration parsed from the configuration file.
parser = Parser()
xml_data = parser.parse("config.xml")
ini_data = parser.parse("config.ini")
yaml_data = parser.parse('config.yaml')
json_data = parser.parse('config.json')

print(xml_data)
print(ini_data)
print(yaml_data)
print(json_data)