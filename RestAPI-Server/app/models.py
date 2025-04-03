from datetime import date
from typing import List
from pydantic import BaseModel

class Phone(BaseModel):
    TypeID: int
    CountryCode: int
    Operator: int
    Number: int

    def to_dict(self):
        return {
            'TypeID': self.TypeID,
            'CountryCode': self.CountryCode,
            'Operator': self.Operator,
            'Number': self.Number
        }

class Contact(BaseModel):
    ID: int
    Username: str
    GivenName: str
    FamilyName: str
    Phone: List[Phone] = []
    Email: List[str] = []
    Birthdate: date = None

    def to_dict(self):
        return {
            'ID': self.ID,
            'Username': self.Username,
            'GivenName': self.GivenName,
            'FamilyName': self.FamilyName,
            'Phone': [p.to_dict() for p in self.Phone],
            'Email': self.Email,
            'Birthdate': str(self.Birthdate) if self.Birthdate else None
        }

class Group(BaseModel):
    ID: int
    Title: str
    Description: str
    Contacts: List[int] = []

    def to_dict(self):
        return {
            'ID': self.ID,
            'Title': self.Title,
            'Description': self.Description,
            'Contacts': self.Contacts
        }