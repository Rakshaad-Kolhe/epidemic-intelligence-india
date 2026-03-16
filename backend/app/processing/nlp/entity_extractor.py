import re


def extract_entities(text):
    text = text or ""
    lower_text = text.lower()

    disease = None
    if "dengue" in lower_text:
        disease = "dengue"
    elif "malaria" in lower_text:
        disease = "malaria"
    elif "virus" in lower_text:
        disease = "virus"

    case_count = None
    case_match = re.search(r"\b(\d+)\s+(?:cases|infected|patients)\b", text, flags=re.IGNORECASE)
    if case_match:
        case_count = int(case_match.group(1))

    location = None
    location_match = re.search(r"\b(?:in|at|from)\s+([A-Za-z]+)\b", text, flags=re.IGNORECASE)
    if location_match:
        location = location_match.group(1).title()

    return {
        "disease": disease,
        "case_count": case_count,
        "location": location,
    }
