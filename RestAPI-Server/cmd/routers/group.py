from fastapi import APIRouter, HTTPException
from typing import List
from pydantic import BaseModel

router = APIRouter(prefix="/api/v1/group", tags=["groups"])

class Group(BaseModel):
    ID: int
    Title: str
    Description: str
    Contacts: List[int]

groups_db = []
next_id = 1

@router.post("/", response_model=Group)
async def create_group(group: Group):
    global next_id
    
    new_group = Group(
        ID=next_id,
        Title=group.Title,
        Description=group.Description,
        Contacts=group.Contacts
    )
    
    groups_db.append(new_group)
    next_id += 1
    return new_group

@router.get("/", response_model=List[Group])
async def get_groups():
    return groups_db

@router.get("/{group_id}", response_model=Group)
async def get_group(group_id: int):
    group = next((g for g in groups_db if g.ID == group_id), None)
    if not group:
        raise HTTPException(status_code=404, detail="Group not found")
    return group

@router.put("/{group_id}", response_model=Group)
async def update_group(group_id: int, group: Group):
    global groups_db
    
    group_index = next((i for i, g in enumerate(groups_db) if g.ID == group_id), None)
    if group_index is None:
        raise HTTPException(status_code=404, detail="Group not found")
    
    updated_group = Group(
        ID=group_id,
        Title=group.Title,
        Description=group.Description,
        Contacts=group.Contacts
    )
    
    groups_db[group_index] = updated_group
    return updated_group

@router.delete("/{group_id}")
async def delete_group(group_id: int):
    global groups_db
    
    group_index = next((i for i, g in enumerate(groups_db) if g.ID == group_id), None)
    if group_index is None:
        raise HTTPException(status_code=404, detail="Group not found")
    
    deleted_group = groups_db.pop(group_index)
    return {
        "message": "Group deleted successfully", 
        "deleted_group": deleted_group
    }