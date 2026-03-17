from fastapi import APIRouter, HTTPException
from app.dal.sql_dal import *



router = APIRouter()

@router.get("/high_priority_moved_targets")
def get_high_priority_moved_targets():
    try:
        return high_priority_moved_targets()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/count_signal_type")
def get_count_signal_type():
    try:
        return count_signal_type()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
