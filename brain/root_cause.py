def detect_root_causes(trend, temp):
    causes = []

    if trend == "RISING" and temp > 80:
        causes.append("Cooling issue")

    if trend == "RISING" and temp < 80:
        causes.append("Bearing friction")

    if temp > 90:
        causes.append("Overload")

    if not causes:
        causes.append("Normal operation")

    return causes
