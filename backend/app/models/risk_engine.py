from typing import Any, Iterable, Tuple


def _get_value(item: Any, key: str, default: float = 0.0) -> float:
    if isinstance(item, dict):
        value = item.get(key, default)
    else:
        value = getattr(item, key, default)

    try:
        if value is None:
            return float(default)
        return float(value)
    except (TypeError, ValueError):
        return float(default)


def calculate_risk(outbreak_signals: Iterable[Any], climate_signals: Iterable[Any]) -> Tuple[float, float]:
    outbreak_list = list(outbreak_signals or [])
    climate_list = list(climate_signals or [])

    outbreak_count = len(outbreak_list)
    total_cases = sum(_get_value(signal, "case_count", 0.0) for signal in outbreak_list)

    avg_rainfall = 0.0
    avg_humidity = 0.0
    if climate_list:
        avg_rainfall = sum(_get_value(signal, "rainfall", 0.0) for signal in climate_list) / len(climate_list)
        avg_humidity = sum(_get_value(signal, "humidity", 0.0) for signal in climate_list) / len(climate_list)

    risk = 0.0
    risk += outbreak_count * 8.0
    risk += total_cases * 0.25
    risk += max(avg_rainfall, 0.0) * 0.10
    risk += max(avg_humidity - 50.0, 0.0) * 0.30
    risk = max(0.0, min(100.0, risk))

    data_points = outbreak_count + len(climate_list)
    confidence = min(1.0, 0.2 + (data_points * 0.08)) if data_points > 0 else 0.0
    confidence = max(0.0, min(1.0, confidence))

    return round(risk, 2), round(confidence, 2)
