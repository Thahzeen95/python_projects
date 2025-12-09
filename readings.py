readings = [
    {"id": "A1", "value": 30, "status": "OK"},
    {"id": "A2", "value": 40, "status": "ERROR"},
    {"id": "A3", "value": 50, "status": "OK"}
]
def process_readings(readings):
    ok = 0
    error = 0
    total = 0

    for item in readings:
        if item.get("status") == "OK":
            ok += 1
        elif item.get("status") == "ERROR":
            error += 1

        total += item.get("value", 0)

    average = total / len(readings) if readings else 0

    return {
        "ok_count": ok,
        "error_count": error,
        "average": average
    }