"""_summary_

"""
import datetime

full_date_hour: datetime.datetime = datetime.datetime.now() - \
    datetime.timedelta(days=14)
only_date_pass: str = f"{full_date_hour.strftime('%Y-%m-%d')}"

print(f" Date to delete: {only_date_pass}")

print("--------------------------------------------------------------")
print("Using datetime library with timedelta and datetime.now")
print(datetime.datetime.now().date() + datetime.timedelta(days=3))
print(datetime.date(2025, 5, 23))
print(datetime.date(2025, 5, 23) + datetime.timedelta(days=3))

print("--------------------------------------------------------------")
print("Using datetime library with ternary operator")
print(str(
    datetime.datetime.now().date() + datetime.timedelta(days=1)
) if datetime.datetime.now().weekday() != 4 else str(
    datetime.datetime.now().date() + datetime.timedelta(days=3)
))
