from sqlalchemy import Column, Date, DateTime, Float, ForeignKey, Integer, func

from app.db.base import Base


class ClimateSignal(Base):
    __tablename__ = "climate_signals"

    id = Column(Integer, primary_key=True, index=True)
    district_id = Column(Integer, ForeignKey("districts.id"), nullable=False)
    temperature = Column(Float, nullable=False)
    rainfall = Column(Float, nullable=False)
    humidity = Column(Float, nullable=False)
    recorded_date = Column(Date, nullable=False)
    ingested_at = Column(DateTime, nullable=False, server_default=func.now())
