from fastapi import APIRouter
from .model import Business, Skill_up_africa
from .query import insert_query
import json

router = APIRouter()
@router.post("/business")
def business(business: Business):
    data = insert_query(business)
    return data

@router.post("/skillupafrica")
def skill_up_africa(skill:Skill_up_africa):
    return skill
    
@router.post("/blog")
def blog():
    pass

