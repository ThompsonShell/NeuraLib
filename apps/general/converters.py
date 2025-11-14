from datetime import datetime, time

class TimeConverter:
    regex = r'\d{2}:\d{2}:\d{2}'
    
    def to_python(self, value: str) -> time:
        return datetime.strptime(value, '%H:%M:%S').time()
    
    def to_url(self, value: time) -> str:
        return value.strftime(value, '%H:%M:%S')                