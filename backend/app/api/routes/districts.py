from fastapi import APIRouter, Depends, HTTPException

from app.db.models.district import District
from app.db.session import get_db

router = APIRouter()


@router.get("/districts")
def list_districts(db=Depends(get_db)):
    districts = db.query(District).all()
    return [
        {
            "id": district.id,
            "name": district.name,
            "state": district.state,
            "population": district.population,
            "latitude": district.latitude,
            "longitude": district.longitude,
        }
        for district in districts
    ]


@router.get("/districts/{district_id}")
def get_district(district_id: int, db=Depends(get_db)):
    district = db.query(District).filter(District.id == district_id).first()
    if not district:
        raise HTTPException(status_code=404, detail="District not found")

    return {
        "id": district.id,
        "name": district.name,
        "state": district.state,
        "population": district.population,
        "latitude": district.latitude,
        "longitude": district.longitude,
    }
