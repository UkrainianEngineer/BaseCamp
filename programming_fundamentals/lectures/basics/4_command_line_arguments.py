"""
This module describes basic examples of slicing in Python.
"""
import argparse
import sys

__author__ = "Pavlo Ivanchyshyn"
__maintainer__ = "Pavlo Ivanchyshyn"
__email__ = "p.ivanchyshyn@gmail.com"

print(sys.argv)
# How to run this script: `python <script_name> 1 2 3 4 5`

parser = argparse.ArgumentParser(add_help=True)
parser.add_argument('-c', '--config', help="Configuration file path")
parser.add_argument('-p', '--port', type=int, help="Port number")
args = parser.print_help()

# How tu execute a program: `python parse_arguments.py -c config.yaml -p 8080`
