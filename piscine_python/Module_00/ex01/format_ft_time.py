
import time
import datetime

timestamp = time.time()
print(f"Seconds since January 1, 1970: {timestamp}\
      or {timestamp:.2e} in scientific notation")
dt = datetime.datetime.fromtimestamp(timestamp)
formatted_date = dt.strftime("%b %d %Y")
print(formatted_date)
