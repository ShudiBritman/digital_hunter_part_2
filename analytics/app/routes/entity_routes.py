from fastapi import APIRouter, HTTPException
from app.services.entity_service import Processor



router = APIRouter()


@router.get("/target_location_by_day/{entity_id}")
def get_location_by_day(entity_id):
    try: 
        Processor.process(entity_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))