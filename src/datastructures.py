"""
Update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- get_member: Should return a member from the self._members list
"""

import random

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._id_counter = 1
        self._members = [
            {
                "id": self._generateId(),
                "first_name": "John",
                "last_name": last_name,
                "age": 33,
                "lucky_numbers": [7, 13, 22]
            },
            {
                "id": self._generateId(),
                "first_name": "Jane",
                "last_name": last_name,
                "age": 35,
                "lucky_numbers": [3, 10, 14]
            },
            {
                "id": self._generateId(),
                "first_name": "Jimmy",
                "last_name": last_name,
                "age": 5,
                "lucky_numbers": [1]
            }
        ]

    def _generateId(self): #evite el randint ya que generaba numeros al azar y a la hora de sacar o traer un miembro tenias que poner "x" numeros y randoms
        new_id = self._id_counter
        self._id_counter += 1
        return new_id

    def add_member(self, member):
        if 'id' not in member or member['id'] is None:
            member['id'] = self._generateId()
        member['last_name'] = self.last_name
        self._members.append(member)
        return member

    def delete_member(self, id: int):
        member = self.get_member(id)
        if member:
            self._members.remove(member)
            return True
        return False

    def get_member(self, id: int):
        for member in self._members:
            if member["id"] == id:
                return member
        return None

    def get_all_members(self):
        return self._members
