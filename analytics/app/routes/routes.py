from fastapi import APIRouter
from dal.sql_dal import *



router = APIRouter()

@router.get("/high_priority_moved_targets")
def get_high_priority_moved_targets():
    try:
        return high_priority_moved_targets()
    except Exception as e:
        return e
