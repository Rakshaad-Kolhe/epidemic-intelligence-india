from fastapi import APIRouter, Depends

from app.db.models.forecast import Forecast
from app.db.session import get_db

router = APIRouter()


@router.get("/forecast/{district_id}")
def get_forecast(district_id: int, db=Depends(get_db)):
    forecasts = db.query(Forecast).filter(Forecast.district_id == district_id).all()
    return [
        {
            "district_id": forecast.district_id,
            "disease": forecast.disease,
            "predicted_cases": forecast.predicted_cases,
            "forecast_date": forecast.forecast_date,
        }
        for forecast in forecasts
    ]
