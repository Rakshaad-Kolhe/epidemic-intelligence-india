from app.db.models.district import District


def normalize_location(location_name, db):
    if location_name is None:
        return None

    district = (
        db.query(District)
        .filter(District.name.ilike(location_name.strip()))
        .first()
    )

    if district:
        return district.id

    return None
