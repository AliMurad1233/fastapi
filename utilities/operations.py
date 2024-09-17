from datetime import datetime




def date_format():
    now = datetime.now()

    month = now.month
    day = now.day
    hour = now.hour
    minute = now.minute

    dt = f"{month}_{day}_{hour}_{minute}"

    return dt




