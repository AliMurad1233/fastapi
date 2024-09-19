from datetime import datetime
import os
import time
from pathlib import Path




def date_format():
    now = datetime.now()

    month = now.month
    day = now.day
    hour = now.hour
    minute = now.minute

    dt = f"{month}_{day}_{hour}_{minute}"

    return dt   



def delete_old_files(directory: str, days_old: int):
    now = time.time()
    cutoff = now - (days_old * 86400)  # 86400 seconds in a day
    for filename in os.listdir(directory):
        model_file = Path(directory) / filename
        if model_file.is_file():
            file_age = os.path.getmtime(model_file)
            if file_age < cutoff:
                os.remove(model_file)
                print(f"Deleted old file: {model_file}")


