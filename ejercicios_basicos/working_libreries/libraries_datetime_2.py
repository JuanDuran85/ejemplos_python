
import datetime

full_date_hour: datetime = datetime.datetime.now() - datetime.timedelta(  # type: ignore
        days=14
)  # type: ignore
only_date_pass: str = f"{full_date_hour.strftime('%Y-%m-%d')}"  # type: ignore

print(f" Date to delete: {only_date_pass}") 