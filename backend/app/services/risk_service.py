from app.db.models.climate_signal import ClimateSignal
from app.db.models.outbreak_signal import OutbreakSignal
from app.db.models.risk_score import RiskScore
from app.models.risk_engine import calculate_risk


def calculate_district_risk(db, district_id):
    outbreak_signals = db.query(OutbreakSignal).filter(OutbreakSignal.district_id == district_id).all()
    climate_signals = db.query(ClimateSignal).filter(ClimateSignal.district_id == district_id).all()

    risk_score, confidence = calculate_risk(outbreak_signals, climate_signals)

    risk_record = RiskScore(
        district_id=district_id,
        risk_score=risk_score,
        confidence=confidence,
    )
    db.add(risk_record)
    db.commit()
    db.refresh(risk_record)

    return risk_record.risk_score, risk_record.confidence
