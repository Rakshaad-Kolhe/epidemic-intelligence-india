from sqlalchemy import Column, Date, DateTime, Float, ForeignKey, Integer, String, func

from app.db.base import Base


class OutbreakSignal(Base):
    __tablename__ = "outbreak_signals"

    id = Column(Integer, primary_key=True, index=True)
    district_id = Column(Integer, ForeignKey("districts.id"), nullable=False)
    disease = Column(String, nullable=False)
    case_count = Column(Integer, nullable=True)
    source_type = Column(String, nullable=False)
    credibility_score = Column(Float, nullable=False)
    reported_date = Column(Date, nullable=False)
    ingested_at = Column(DateTime, nullable=False, server_default=func.now())
