from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, func

from app.db.base import Base


class RiskScore(Base):
    __tablename__ = "risk_scores"

    id = Column(Integer, primary_key=True, index=True)
    district_id = Column(Integer, ForeignKey("districts.id"), nullable=False)
    risk_score = Column(Float, nullable=False)
    confidence = Column(Float, nullable=False)
    calculated_at = Column(DateTime, nullable=False, server_default=func.now())
