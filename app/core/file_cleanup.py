import os
import time
from pathlib import Path

model_file = "/Users/alimurad/my_fastAPI:/temp_file/"

def delete_old_files(directory: str, days_old: int):
    now = time.time()
    cutoff = now - (days_old * 172800)  # 86400 seconds in a day
    for filename in os.listdir(directory):
        model_file = Path(directory) / filename
        if model_file.is_file():
            file_age = os.path.getmtime(model_file)
            if file_age < cutoff:
                os.remove(model_file)
                print(f"Deleted old file: {model_file}")

if __name__ == "__main__":
    delete_old_files("temp_files", 2)
