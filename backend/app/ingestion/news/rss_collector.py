import random
from datetime import date
from xml.etree import ElementTree

import requests

from app.db.models.district import District
from app.db.models.outbreak_signal import OutbreakSignal
from app.db.session import SessionLocal

RSS_URL = "https://news.google.com/rss/search?q=dengue+OR+malaria+OR+outbreak+OR+virus"
KEYWORDS = ["dengue", "malaria", "outbreak", "virus"]


def collect_rss_outbreak_signals():
    db = SessionLocal()
    try:
        districts = db.query(District).all()
        if not districts:
            print("No districts found. Skipping RSS collection.")
            return

        response = requests.get(RSS_URL, timeout=20)
        response.raise_for_status()

        root = ElementTree.fromstring(response.content)
        items = root.findall("./channel/item")

        created = 0
        for item in items:
            title = item.findtext("title") or ""
            description = item.findtext("description") or ""
            text = f"{title} {description}".lower()

            if not any(keyword in text for keyword in KEYWORDS):
                continue

            district = random.choice(districts)
            signal = OutbreakSignal(
                district_id=district.id,
                disease="dengue" if "dengue" in text else "malaria" if "malaria" in text else "virus",
                case_count=None,
                source_type="rss",
                credibility_score=0.7,
                reported_date=date.today(),
            )
            db.add(signal)
            created += 1

        db.commit()
        print(f"RSS collection complete. Inserted {created} outbreak signals.")
    finally:
        db.close()


if __name__ == "__main__":
    collect_rss_outbreak_signals()
