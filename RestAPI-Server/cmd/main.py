from fastapi import FastAPI
from datetime import date
from typing import List, Optional
from pydantic import BaseModel

app = FastAPI()

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

class Group(BaseModel):
    ID: int
    Title: str
    Description: str
    Contacts: List[int]

@app.post("/api/v1/contact")
async def create_contact() -> Contact:
    return Contact(
        ID=0,
        Username="",
        GivenName="",
        FamilyName="",
        Phone=[],
        Email=[],
        Birthdate=date.today()
    )

@app.get("/api/v1/contact")
async def read_contact() -> Contact:
    return Contact(
        ID=0,
        Username="",
        GivenName="",
        FamilyName="",
        Phone=[],
        Email=[],
        Birthdate=date.today()
    )

@app.put("/api/v1/contact")
async def update_contact() -> Contact:
    return Contact(
        ID=0,
        Username="",
        GivenName="",
        FamilyName="",
        Phone=[],
        Email=[],
        Birthdate=date.today()
    )

@app.delete("/api/v1/contact")
async def delete_contact() -> Contact:
    return Contact(
        ID=0,
        Username="",
        GivenName="",
        FamilyName="",
        Phone=[],
        Email=[],
        Birthdate=date.today()
    )

@app.post("/api/v1/group")
async def create_group() -> Group:
    return Group(
        ID=0,
        Title="",
        Description="",
        Contacts=[]
    )

@app.get("/api/v1/group")
async def read_group() -> Group:
    return Group(
        ID=0,
        Title="",
        Description="",
        Contacts=[]
    )

@app.put("/api/v1/group")
async def update_group() -> Group:
    return Group(
        ID=0,
        Title="",
        Description="",
        Contacts=[]
    )

@app.delete("/api/v1/group")
async def delete_group() -> Group:
    return Group(
        ID=0,
        Title="",
        Description="",
        Contacts=[]
    )