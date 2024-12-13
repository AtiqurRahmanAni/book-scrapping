from pymongo import MongoClient
import pytz
from datetime import datetime

utc_time = datetime.utcnow()
dhaka_tz = pytz.timezone("Asia/Dhaka")
dhaka_time = pytz.utc.localize(utc_time).astimezone(dhaka_tz)
print(dhaka_time)

timezone = pytz.timezone("Asia/Dhaka")
current_time = datetime.now(timezone)
print(current_time)
