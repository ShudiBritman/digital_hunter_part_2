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


@router.get("/detecting_sensitive_targets")
def get_detecting_sensitive_targets():
    try:
        return detecting_sensitive_targets()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@router.get("/active_after_dormant")
def get_active_after_dormant():
    try:
        return find_active_after_dormant()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))