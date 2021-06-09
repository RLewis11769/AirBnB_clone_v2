#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
from models.base_model import BaseModel
from models.state import State
from os import environ
import models
import MySQLdb

env = {
    'user': environ.get('HBNB_MYSQL_USER'),
    'pwd': environ.get('HBNB_MYSQL_PWD'),
    'daba': environ.get('HBNB_MYSQL_DB'),
    'host': environ.get('HBNB_MYSQL_HOST')
      }


@unittest.skipIf(environ.get('HBNB_TYPE_STORAGE') != 'db', 'Database Storage')
class test_dbStorage(unittest.TestCase):
    """ Class to test DBStorage method """

    def setUp(self):
        """ Set up test environment """
        self.db = MySQLdb.connect(**env)
        self.cursor = self.db.cursor()
    
    def tearDown(self):
        """ Remove storage file at end of tests """
        try:
            self.cursor.close()
        except:
            pass

    def test_obj_list_empty(self):
        """ database is initially empty """
        self.assertEqual(len(models.storage.all()), 0)

    def test_new(self):
        """ New record is correctly added to database """
        new = State(name="Oklahoma")
        new.save()
        for obj in models.storage.all().values():
            temp = obj
        self.assertTrue(temp is obj)
       
    def test_all(self):
        """ Record is properly returned """
        new = State(name="Louisiana")
        new.save()
        temp = models.storage.all()
        self.assertIsInstance(temp, dict)

    def test_save(self):
        """ DBStorage save method """
        new = State(name="Texas")
        leng = self.cursor.execute("SELECT * FROM STATE;")
        new.save()
        self.assertEqual(leng, len(new) + 1)

    def test_create_value(self):
        """ Adds to DB """
        new = State(name="Alaska")
        new.save()
        self.assertIn("Alaska", self.daba)
