from fastapi import APIRouter, Depends

from app.db.session import get_db
from app.services.risk_service import calculate_district_risk

router = APIRouter()


@router.get("/risk/{district_id}")
def get_district_risk(district_id: int, db=Depends(get_db)):
    risk_score, confidence = calculate_district_risk(db, district_id)
    return {
        "district_id": district_id,
        "risk_score": risk_score,
        "confidence": confidence,
    }
