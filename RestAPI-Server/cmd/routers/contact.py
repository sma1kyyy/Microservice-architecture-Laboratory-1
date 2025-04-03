from fastapi import APIRouter, HTTPException
from typing import List
from datetime import date
from pydantic import BaseModel

router = APIRouter(prefix="/api/v1/contact", tags=["contacts"])

class Phone(BaseModel):
    TypeID: int
    CountryCode: int
    Operator: int
    Number: int

class Contact(BaseModel):
    ID: int
    Username: str
    GivenName: str
    FamilyName: str
    Phone: List[Phone]
    Email: List[str]
    Birthdate: date

contacts_db = []
next_id = 1

@router.post("/", response_model=Contact)
async def create_contact(contact: Contact):
    global next_id
    new_contact = Contact(
        ID=next_id,
        Username=contact.Username,
        GivenName=contact.GivenName,
        FamilyName=contact.FamilyName,
        Phone=contact.Phone,
        Email=contact.Email,
        Birthdate=contact.Birthdate
    )
    contacts_db.append(new_contact)
    next_id += 1
    return new_contact

@router.get("/", response_model=List[Contact])
async def get_contacts():
    return contacts_db

@router.get("/{contact_id}", response_model=Contact)
async def get_contact(contact_id: int):
    contact = next((c for c in contacts_db if c.ID == contact_id), None)
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    return contact

@router.put("/{contact_id}", response_model=Contact)
async def update_contact(contact_id: int, contact: Contact):
    global contacts_db
    contact_index = next((i for i, c in enumerate(contacts_db) if c.ID == contact_id), None)
    if contact_index is None:
        raise HTTPException(status_code=404, detail="Contact not found")
    
    updated_contact = Contact(
        ID=contact_id,
        Username=contact.Username,
        GivenName=contact.GivenName,
        FamilyName=contact.FamilyName,
        Phone=contact.Phone,
        Email=contact.Email,
        Birthdate=contact.Birthdate
    )
    
    contacts_db[contact_index] = updated_contact
    return updated_contact

@router.delete("/{contact_id}")
async def delete_contact(contact_id: int):
    global contacts_db
    contact_index = next((i for i, c in enumerate(contacts_db) if c.ID == contact_id), None)
    if contact_index is None:
        raise HTTPException(status_code=404, detail="Contact not found")
    
    deleted_contact = contacts_db.pop(contact_index)
    return {"message": "Contact deleted successfully", "deleted_contact": deleted_contact}