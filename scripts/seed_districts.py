from app.db.models.district import District
from app.db.session import SessionLocal


def seed_districts():
    db = SessionLocal()
    try:
        if db.query(District).first():
            print("District table already has data. Skipping seeding.")
            return

        districts = [
            District(name="Mumbai", state="Maharashtra", population=12442373, latitude=19.0760, longitude=72.8777),
            District(name="Delhi", state="Delhi", population=16787941, latitude=28.7041, longitude=77.1025),
            District(name="Bengaluru", state="Karnataka", population=8443675, latitude=12.9716, longitude=77.5946),
            District(name="Kolkata", state="West Bengal", population=4486679, latitude=22.5726, longitude=88.3639),
            District(name="Chennai", state="Tamil Nadu", population=4646732, latitude=13.0827, longitude=80.2707),
        ]

        db.add_all(districts)
        db.commit()
        print("District seeding complete.")
    finally:
        db.close()


if __name__ == "__main__":
    seed_districts()
