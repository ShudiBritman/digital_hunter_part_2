from fastapi import APIRouter
from app.services.entity_service import Processor



router = APIRouter()


@router.get("/target_location_by_day")