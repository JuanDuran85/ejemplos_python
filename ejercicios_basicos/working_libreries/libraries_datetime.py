"""_summary_

    Using datetime library

"""



import datetime

today: datetime.date = datetime.date.today()
print(today)
print(repr(today))

# fecha y hora
fecha_hora: datetime = datetime.datetime.now()
print(fecha_hora)

# year
print(fecha_hora.year)
# month
print(fecha_hora.month)
# day
print(fecha_hora.day)
# hora
print(fecha_hora.hour)
# minutos
print(fecha_hora.minute)
# segundos
print(fecha_hora.second)

# -----------------------------------------------------------------------------------------------
now: datetime = datetime.datetime.now()

# Here is a pretty "standard" way to format dates and times
print(f"{now.strftime('%Y-%m-%d')}")
print(f"{now.strftime('%H:%M:%S')}")

# But, you can also do things like this:
print(f"{now.strftime('Today is the %d of the month %m of %y')}")

# Deleted dates
print(f"7 days pass: {now - datetime.timedelta(days=7)}")

# -----------------------------------------------------------------------------------------------

time_utc: datetime = datetime.datetime.now(datetime.timezone.utc)
print(time_utc)
time_utc_minus: str = (time_utc - datetime.timedelta(seconds=600)).strftime("%H:%M:%S")
print(time_utc_minus)
