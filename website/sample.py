from datetime import datetime, timedelta

nine_hours_from_now = datetime.utcnow() + timedelta(hours=5, minutes=30)
print('{:%H:%M:%S}'.format(nine_hours_from_now))

