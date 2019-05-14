# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def __repr__(self):
        self_object = {
            'name': self.name,
            'description': self.description
        }
        return self_object
    
    def __getitem__(self, key):
        self_object = {
            'name': self.name,
            'description': self.description
        }
        return self_object[key]