#!/usr/bin/python3
"""Unit tests for the console"""

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand

class TestConsole(unittest.TestCase):
    """Test the console module"""
    
    def test_help(self):
        """Test help output"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            self.assertGreater(len(f.getvalue()), 0)
            
    def test_create(self):
        """Test create command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            self.assertEqual("** instance id missing **\n", f.getvalue())
            
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State name=California")
            self.assertEqual(36, len(f.getvalue()))
            
    def test_show(self):
        """Test show command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
            self.assertEqual("** class name missing **\n", f.getvalue())
            
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel")
            self.assertEqual("** instance id missing **\n", f.getvalue())
            
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel abcd-123")
            self.assertEqual("** no instance found **\n", f.getvalue())

    # more test cases...
            
if __name__ == "__main__":
    unittest.main()

    