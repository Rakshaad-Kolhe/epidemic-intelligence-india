def validate_signal(disease, case_count, district_id):
    if disease is None or district_id is None:
        return False

    if case_count is not None and case_count < 0:
        return False

    return True
