'''
CSCI 204 Lab 02 Class Design, Inheritance, and Exceptions
Lab section: CSCI 204, Tuesday 1:00pm - 2:50pm
Student name(s): Aleena Sultan, Khanh Cao 
Instructor name: Professor Todd Schmid 
'''

import unittest
from pet import *

class TestPet(unittest.TestCase) :
    """
    A class used to perform unit tests on the Pet class.

    Inherits from unittest.TestCase to provide test methods for testing 
    various functionalities of the Pet class, including validation of attributes 
    such as name, species, age, and activity, as well as the correctness of the 
    methods defined in Pet.
    """

    UNKNOWN = 0
    WALKING = 1
    EATING = 2
    SLEEPING = 3
    BARKING = 4
    MEOWING = 5

    def test_mabel(self) :
        test_pet = Pet("Mabel", "Dog")
        self.assertEqual(test_pet._name, "Mabel", "Wrong name!")
    def test_cat_age(self):
        cat = Pet('HIHI', 'Cat')
        self.assertEqual(cat._age, 0, 'Wrong age')
        cat.celebrate_birthday()
        self.assertEqual(cat._age, 1, 'Wrong age')
    def test_age(self):
        dog = Pet('HAHA','Dog')
        self.assertEqual(dog._age, 0, 'Wrong age')
        self.assertEqual(dog.get_human_age(), 0, 'Wrong age')
        dog.celebrate_birthday()
        self.assertEqual(dog._age, 1, 'Wrong age')
        self.assertEqual(dog.get_human_age(), 7, 'Wrong age')

    def test_species(self):
        dog = Pet('HAHA','Dog')
        self.assertIn(dog._species, ['Dog', 'Cat'], 'Wrong species')
        cat = Pet('HIHI', 'Cat')
        self.assertIn(cat._species, ['Dog', 'Cat'], 'Wrong species')

    def test_activities(self):
        dog = Pet('HAHA','Dog')
        self.assertEqual(dog._activity, 0, 'Wrong activity')
        dog = Pet('HAHA','Dog', activity= 1)
        self.assertEqual(dog._activity, 1, 'Wrong activity')
        dog = Pet('HAHA','Dog',activity= 2)
        self.assertEqual(dog._activity, 2, 'Wrong activity')
        dog = Pet('HAHA','Dog',activity= 3)
        self.assertEqual(dog._activity, 3, 'Wrong activity')
        dog = Pet('HAHA','Dog',activity= 4)
        self.assertEqual(dog._activity, 4, 'Wrong activity')

        cat = Pet('HIHI', 'Cat')
        self.assertEqual(cat._activity, 0, 'Wrong activity')
        cat = Pet('HIHI', 'Cat', activity= 1)
        self.assertEqual(cat._activity, 1, 'Wrong activity')
        cat = Pet('HIHI', 'Cat', activity= 2)
        self.assertEqual(cat._activity, 2, 'Wrong activity')
        cat = Pet('HIHI', 'Cat', activity= 3)
        self.assertEqual(cat._activity, 3, 'Wrong activity')
        cat = Pet('HIHI', 'Cat', activity= 5)
        self.assertEqual(cat._activity, 5, 'Wrong activity')



unittest.main()