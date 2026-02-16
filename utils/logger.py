import csv
import os
from datetime import datetime

def log_data(machine_id, area, temperature, status):
    file_path = "data/logs.csv"
    file_exists = os.path.isfile(file_path)

    with open(file_path, mode="a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "timestamp",
                "machine_id",
                "area",
                "temperature",
                "status"
            ])

        writer.writerow([
            datetime.now(),
            machine_id,
            area,
            temperature,
            status
        ])
