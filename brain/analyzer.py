from brain.trend import detect_trend
from brain.root_cause import detect_root_causes

def analyze_temperature(history, current):
    trend = detect_trend(history)
    causes = detect_root_causes(trend, current)

    score = anomaly_score(history, current)

    if score > 30:
        return "DANGER", f"High anomaly detected ({score}%). Possible causes: {', '.join(causes)}."

    if score > 15:
        return "WARNING", f"Moderate anomaly ({score}%). Monitor system."

    return "NORMAL", f"System stable. Anomaly score: {score}%."


def anomaly_score(history, current):
    if len(history) < 5:
        return 0

    avg = sum(history) / len(history)
    deviation = abs(current - avg)

    score = deviation / avg
    return round(score * 100, 2)
