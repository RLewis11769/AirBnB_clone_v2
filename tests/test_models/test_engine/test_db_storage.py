#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
from models.base_model import BaseModel, Base
from models.state import State
from os import environ
import models
import MySQLdb
from io import StringIO
from console import HBNBCommand
from unittest.mock import patch


args = {'user': environ.get('HBNB_MYSQL_USER'), 'pwd': environ.get('HBNB_MYSQL_PWD'), 'daba': environ.get('HBNB_MYSQL_DB'),'host': environ.get('HBNB_MYSQL_HOST')
       }


@unittest.skipIf(environ.get('HBNB_TYPE_STORAGE') != 'db', 'Database Storage')
class test_dbStorage(unittest.TestCase):
    """ Class to test DBStorage method """

    def test_all(self):
        """ Open test db and run tests """
        self.dbas = MySQLdb.connect(**args)
        self.cursor = self.dbas.cursor()
        self.cursor.execute("SELECT count(*) FROM STATES")
        leng = self.cursor.fetchone()[0]
        self.cursor.reload()
        with patch('sys.stdout', new=StringIO()) as x:
            HBNBCommand().onecmd("Create State name=\"Fugue\"")
        self.cursor = self.dbas.cursor()
        self.cursor.execute("SELECT count(*) FROM STATES")
        lengt = self.cursor.fetchone()[0]
        self.assertEqual(lengt, leng + 1)
