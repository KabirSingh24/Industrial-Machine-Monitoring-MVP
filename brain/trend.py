def detect_trend(history):
    if len(history) < 4:
        return "No Trend"
    
    last=history[-4:]

    if last[0] < last[1] < last[2] < last[3]:
        return "RISING"
    
    if last[0] > last[1] > last[2] > last[3]:
        return "FALLING"
    else :
        return "STABLE"

    
