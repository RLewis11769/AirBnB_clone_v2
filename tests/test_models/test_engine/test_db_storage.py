#!/usr/bin/python3
"""tests for db storage"""
import unittest
import sys
from os import environ
from io import StringIO
from console import HBNBCommand
from unittest.mock import patch


class test_db_storage(unittest.TestCase):
    """ Class to test DBStorage methods """

    @unittest.skipIf(environ.get('HBNB_TYPE_STORAGE') == 'db',
                     "Database Storage")
    def test_all(self):
        """ Tests for all of db """
        with patch('sys.stdout', new=StringIO()) as x:
            HBNBCommand().onecmd("create State name='Altered'")
            state = x.getvalue()
            state = state[:-1]
        with patch('sys.stdout', new=StringIO()) as x:
            HBNBCommand().onecmd("show State {}".format(state))
            state_all = x.getvalue()
        self.assertIn(state, state_all)

    @unittest.skipIf(environ.get('HBNB_TYPE_STORAGE') == 'db',
                     "Database Storage")
    def test_city_in_cities(self):
        """A note"""
        with patch('sys.stdout', new=StringIO()) as x:
            HBNBCommand().onecmd("create State name='Altered'")
            state = x.getvalue()
            state = state[:-1]
        with patch('sys.stdout', new=StringIO()) as x:
            HBNBCommand().onecmd("create City name='Bank' state_id={}"
                                 .format(state))
            city = x.getvalue()
            city = city[:-1]
        with patch('sys.stdout', new=StringIO()) as x:
            HBNBCommand().onecmd("show City {}".format(city))
            cities = x.getvalue()
        self.assertIn(city, cities)


if __name__ == '__main__':
    unittest.main()
