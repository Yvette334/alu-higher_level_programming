#!/usr/bin/python3
"""This module defines a class Student"""


class Student:
    """Represent a student."""

    def __init__(self, fname, lname, age):
        """Initializes a new Student
        """
        self.first_name = fname
        self.last_name = lname
        self.age = age

    def to_json(self):
        """Gets a dictionary representation of the Student"""
        return self.__dict__
