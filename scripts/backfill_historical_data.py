import random
from datetime import date

from app.db.models.climate_signal import ClimateSignal
from app.db.models.district import District
from app.db.models.outbreak_signal import OutbreakSignal
from app.db.session import SessionLocal


def backfill_historical_data():
    db = SessionLocal()
    try:
        if db.query(OutbreakSignal).first():
            print("Outbreak signals already exist. Skipping backfill.")
            return

        districts = db.query(District).all()
        if not districts:
            print("No districts found. Nothing to backfill.")
            return

        today = date.today()
        diseases = ["dengue", "malaria"]

        outbreak_records = []
        climate_records = []

        for district in districts:
            for _ in range(3):
                outbreak_records.append(
                    OutbreakSignal(
                        district_id=district.id,
                        disease=random.choice(diseases),
                        case_count=random.randint(5, 50),
                        source_type="news",
                        credibility_score=round(random.uniform(0.6, 0.9), 2),
                        reported_date=today,
                    )
                )

                climate_records.append(
                    ClimateSignal(
                        district_id=district.id,
                        temperature=round(random.uniform(25, 35), 1),
                        rainfall=round(random.uniform(0, 200), 1),
                        humidity=round(random.uniform(60, 90), 1),
                        recorded_date=today,
                    )
                )

        db.add_all(outbreak_records)
        db.add_all(climate_records)
        db.commit()

        print("Historical outbreak and climate signals backfill complete.")
    finally:
        db.close()


if __name__ == "__main__":
    backfill_historical_data()
