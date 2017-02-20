"""Allows tests to find the VideoProcessor module for testing
   This is required as the modules are in different directories"""
#pylint: disable=wrong-import-position,unused-import
#   Above pylint disables are required as this is a context file and
#   is only used by other files to set namespace and resovle modules.

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import vpa

#http://docs.python-guide.org/en/latest/writing/structure/
