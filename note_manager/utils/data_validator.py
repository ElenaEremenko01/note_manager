from datetime import datetime as dt

def validate_data(data_str):
    try:
        dt.strptime(data_str,'%d.%m.%Y').date()
        return True
    except ValueError:
        return False