from sqlalchemy import Column, Date, DateTime, ForeignKey, Integer, String, func

from app.db.base import Base


class Forecast(Base):
    __tablename__ = "forecasts"

    id = Column(Integer, primary_key=True, index=True)
    district_id = Column(Integer, ForeignKey("districts.id"), nullable=False)
    disease = Column(String, nullable=False)
    predicted_cases = Column(Integer, nullable=False)
    forecast_date = Column(Date, nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=func.now())
