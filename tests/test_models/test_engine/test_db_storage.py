#!/usr/bin/python3
"""
Unit tests for the DBStorage class
"""
import unittest
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models import storage
import os

@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', "DBStorage tests")
class TestDBStorage(unittest.TestCase):
    """Class to test the DBStorage method"""

    def setUp(self):
        """Set up test environment"""
        self.storage = storage
        self.storage.reload()
        for obj in self.storage.all().values():
            self.storage.delete(obj)
        self.storage.save()

    def tearDown(self):
        """Tear down test environment"""
        for obj in self.storage.all().values():
            self.storage.delete(obj)
        self.storage.save()

    def test_obj_list_empty(self):
        """__objects is initially empty"""
        self.assertEqual(len(self.storage.all()), 0)

    def test_new(self):
        """New object is correctly added to __objects"""
        new = BaseModel()
        self.storage.new(new)
        self.storage.save()
        temp = None
        for obj in self.storage.all().values():
            temp = obj
        self.assertTrue(temp is new)

    def test_all(self):
        """__objects is properly returned"""
        new = BaseModel()
        self.storage.new(new)
        self.storage.save()
        temp = self.storage.all()
        self.assertIsInstance(temp, dict)

    def test_base_model_instantiation(self):
        """Database is not changed on BaseModel instantiation"""
        new = BaseModel()
        self.assertEqual(len(self.storage.all()), 0)

    def test_empty(self):
        """Data is saved to database"""
        new = BaseModel()
        thing = new.to_dict()
        new.save()
        new2 = BaseModel(**thing)
        self.assertTrue(new.id in [obj.id for obj in self.storage.all().values()])

    def test_save(self):
        """DBStorage save method"""
        new = BaseModel()
        self.storage.new(new)
        self.storage.save()
        self.assertTrue(new.id in [obj.id for obj in self.storage.all().values()])

    def test_reload(self):
        """DBStorage reload method"""
        new = BaseModel()
        self.storage.new(new)
        self.storage.save()
        self.storage.reload()
        loaded = None
        for obj in self.storage.all().values():
            if obj.id == new.id:
                loaded = obj
        self.assertEqual(new.to_dict()['id'], loaded.to_dict()['id'])

    def test_delete_existing_object(self):
        """Test that delete removes the object from __objects"""
        state = State(name="California")
        self.storage.new(state)
        self.storage.save()
        self.assertIn("State." + state.id, self.storage.all())
        self.storage.delete(state)
        self.storage.save()
        self.assertNotIn("State." + state.id, self.storage.all())

    def test_delete_non_existing_object(self):
        """Test that delete does nothing if the object is not in __objects"""
        state = State(name="California")
        initial_count = len(self.storage.all())
        self.storage.delete(state)  # Try to delete an object not in __objects
        self.storage.save()
        self.assertEqual(len(self.storage.all()), initial_count)

    def test_delete_none(self):
        """Test that delete does nothing if obj is None"""
        initial_count = len(self.storage.all())
        self.storage.delete(None)  # Should not change the objects count
        self.storage.save()
        self.assertEqual(len(self.storage.all()), initial_count)

if __name__ == "__main__":
    unittest.main()
