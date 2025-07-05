#!/usr/bin/env python3
"""pickle"""


import pickle

class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Display the attributes of the object in a formatted manner.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current instance to the given file using pickle.
        Overwrites the file if it already exists.
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception as e:
            pass  # You can log the error if needed

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an instance of CustomObject from the given file using pickle.
        Returns the object instance or None if an error occurs.
        """
        try:
            with open(filename, 'rb') as f:
                obj = pickle.load(f)
                if isinstance(obj, cls):
                    return obj
        except (FileNotFoundError, pickle.UnpicklingError, EOFError):
            pass
        return None
